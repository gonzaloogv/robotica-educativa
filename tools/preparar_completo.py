"""Amplía el ejemplo oficial V2 de ACECode sin ejecutar código en el robot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def build_project(project):
    project = deepcopy(project)
    assert project["mainboard"] == "ESP32"
    assert project["scratchMode"] == "upload"
    target = next(t for t in project["targets"] if t.get("blocks"))
    blocks = target["blocks"]
    original = deepcopy(blocks)
    stage = next(t for t in project["targets"] if t["isStage"])
    variables = stage["variables"]
    added = []

    def add(opcode, *, inputs=None, fields=None, **extra):
        key = f"completo_{len(added):03d}"
        assert key not in blocks
        blocks[key] = dict(opcode=opcode, next=None, parent=None,
                           inputs=inputs or {}, fields=fields or {},
                           shadow=False, topLevel=False)
        blocks[key].update(extra)
        added.append(key)
        for value in blocks[key]["inputs"].values():
            if isinstance(value[1], str):
                blocks[value[1]]["parent"] = key
        return key

    def chain(parent, *ids):
        for previous, current in zip([parent, *ids], ids):
            blocks[previous]["next"] = current
            blocks[current]["parent"] = previous
        return ids[0]

    def literal(value):
        return [1, [10, str(value)]]

    def reporter(key):
        return [3, key, [10, "0"]]

    def variable(name):
        return [3, [12, name, f"completo_var_{name}"], [10, "0"]]

    def set_value(name, value):
        return add("data_setvariableto", inputs={"VALUE": value},
                   fields={"VARIABLE": [name, f"completo_var_{name}"]})

    def equals(name, value):
        return add("operator_equals", inputs={"OPERAND1": variable(name),
                                              "OPERAND2": literal(value)})

    def condition(predicate, *body):
        key = add("control_if", inputs={"CONDITION": [2, predicate],
                                        "SUBSTACK": [2, body[0]]})
        chain(key, *body)
        # SUBSTACK is not the ordinary next connection of a conditional.
        blocks[key]["next"] = None
        return key

    def stop():
        return add("carMotorV2_carStop")

    def return_void():
        return add("return", inputs={"VALUE": literal("")})

    def ir_key(number):
        return add("IR_Receiver_Module", fields={"PIN_LIST": ["4", None],
                                                 "PIN_TYPE": [str(number), None]})

    def now():
        return reporter(add("GET_NOW_TIME"))

    ap = [b for b in blocks.values()
          if isinstance(b, dict) and b["opcode"] == "WIFI_AP"]
    assert len(ap) == 1, "Usar el ejemplo oficial AP, no la variante STA"
    assert ap[0]["inputs"]["NAME"][1][1] == "ESP32-CAR"
    for name in ("IR_activo", "IR_esperar_stop", "IR_ultima_orden"):
        variables[f"completo_var_{name}"] = [name, 0]

    # Inicialización explícita, antes de iniciar el servidor y su tarea de red.
    init = next(k for k, b in blocks.items() if isinstance(b, dict)
                and b["opcode"] == "carMotorV2_initCar")
    old_next = blocks[init]["next"]
    chain(init, stop(), *(set_value(n, literal(0)) for n in
                         ("IR_activo", "IR_esperar_stop", "IR_ultima_orden")), old_next)

    procedure = add("procedures_definition", topLevel=True, x=900, y=0)
    prototype = add("procedures_prototype", shadow=True, mutation={
        "tagName": "mutation", "children": [], "proccode": "CONTROL_IR",
        "argumentids": "[]", "argumentnames": "[]",
        "argumentdefaults": "[]", "warp": "false"
    })
    blocks[procedure]["inputs"] = {"custom_block": [1, prototype]}
    blocks[prototype]["parent"] = procedure

    release = condition(ir_key(11), stop(), set_value("IR_activo", literal(0)),
                        set_value("IR_esperar_stop", literal(1)), return_void())
    central = condition(ir_key(16), stop(), set_value("IR_activo", literal(1)),
                        set_value("IR_ultima_orden", now()), return_void())
    # Códigos del mando documentados en ACB_IR y direcciones del driver V2.
    directions = {
        12: "forward", 13: "backward", 14: "anticlockwise", 15: "clockwise",
        1: "left", 3: "right", 4: "leftUp", 6: "rightUp",
        7: "leftDown", 9: "rightDown"
    }
    moves = []
    for key, direction in directions.items():
        move = add("carMotorV2_carMove", fields={"ONE": [direction, None]},
                   inputs={"TWO": [1, [4, "255"]]})
        moves.append(condition(ir_key(key), set_value("IR_activo", literal(1)),
                               set_value("IR_ultima_orden", now()), move))
    chain(procedure, release, central, *moves)

    callback = next(k for k, b in blocks.items() if isinstance(b, dict)
                    and b["opcode"] == "carMotorV2_spiderExecute")
    first = blocks[callback]["inputs"]["SUBSTACK"][1]
    call = add("procedures_call", mutation={
        "tagName": "mutation", "children": [], "proccode": "CONTROL_IR",
        "argumentids": "[]", "warp": "false"
    })
    elapsed = add("operator_subtract", inputs={"NUM1": now(),
                                               "NUM2": variable("IR_ultima_orden")})
    expired = add("operator_gt", inputs={"OPERAND1": reporter(elapsed),
                                         "OPERAND2": literal(100)})
    ir_gate = condition(equals("IR_activo", 1), condition(expired, stop()), return_void())
    app_stop = add("carMotorV2_carGetInstruct", fields={"ONE": ["60", None]})
    app_gate = condition(equals("IR_esperar_stop", 1), stop(),
                         condition(app_stop, set_value("IR_esperar_stop", literal(0))),
                         return_void())
    blocks[callback]["inputs"]["SUBSTACK"] = [2, call]
    chain(callback, call, ir_gate, app_gate, first)
    blocks[callback]["next"] = None

    # La biblioteca interpreta estas cuatro órdenes, ausentes en los bloques
    # de movimiento del ejemplo final. Se agregan sin alterar los seis casos existentes.
    move_mode = next(k for k, b in blocks.items() if isinstance(b, dict)
                     and b["opcode"] == "carMotorV2_carMode"
                     and b["fields"]["ONE"][0] == "move")
    tail = move_mode
    while blocks[tail]["next"]:
        tail = blocks[tail]["next"]
    diagonal_cases = []
    speed_id = next(k for k, v in variables.items() if v[0] == "Speeds")
    for command, direction in ((74, "leftUp"), (71, "leftDown"),
                                (72, "rightUp"), (73, "rightDown")):
        command_block = add("carMotorV2_carGetInstruct",
                            fields={"ONE": [str(command), None]})
        move = add("carMotorV2_carMove", fields={"ONE": [direction, None]},
                   inputs={"TWO": [3, [12, "Speeds", speed_id], [4, "100"]]})
        diagonal_cases.append(condition(command_block, move))
    chain(tail, *diagonal_cases)

    for extension in ("IR", "GET"):
        if extension not in project["extensions"]:
            project["extensions"].append(extension)
    for key, text in ((procedure, "Mando IR: flechas y números mueven el auto; OK detiene. "
                      "# vuelve a la app: pulsar STOP en la app antes de continuar."),
                     (ir_gate, "El mando tiene prioridad hasta pulsar #. "
                      "Sin una nueva orden IR durante 100 ms, se ordena detener."),
                     (app_gate, "Esperar STOP evita retomar una orden anterior de la app.")):
        comment = f"completo_comment_{key}"
        target.setdefault("comments", {})[comment] = dict(
            blockId=key, x=1300, y=0, width=400, height=140,
            minimized=True, text=text)
        blocks[key]["comment"] = comment
    # ACECode puede interrumpir la importación al mostrar comentarios antes
    # de terminar de ubicar los bloques. Se conservan plegados al abrir.
    for comment in target.get("comments", {}).values():
        comment["minimized"] = True
    changed = [k for k, b in original.items() if blocks[k] != b]
    assert all(k in blocks for k in original), "No se eliminan bloques oficiales"
    return project, changed, len(added)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    assert not args.output.exists(), "El destino debe ser nuevo"
    with ZipFile(args.source) as source:
        original = json.loads(source.read("project.json"))
        project, changed, added = build_project(original)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(args.output, "x", ZIP_DEFLATED) as output:
            for entry in source.infolist():
                content = (json.dumps(project, ensure_ascii=False).encode("utf-8")
                           if entry.filename == "project.json" else source.read(entry))
                output.writestr(entry, content)
    manifest = dict(
        source_file=args.source.name,
        source_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest(),
        output_file=args.output.name,
        output_sha256=hashlib.sha256(args.output.read_bytes()).hexdigest(),
        original_blocks_preserved=True, changed_original_blocks=changed,
        added_blocks=added, network="AP: ESP32-CAR; clave pública del ejemplo: 12345678",
        comments_folded_for_editor_import=True,
        hardware_uploaded=False, hardware_tested=False)
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
