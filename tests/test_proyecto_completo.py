"""Comprobaciones sin conectar el robot ni abrir puertos serie."""

import json
import os
from pathlib import Path
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / os.environ.get(
    "ACECODE_PROJECT", "acecode/versiones-ap-y-sta/QD001_V2_AP_IR_Completo.sb3"
)


class ProyectoCompletoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert PROJECT.is_file(), f"Falta el proyecto: {PROJECT}"
        with ZipFile(PROJECT) as archive:
            assert archive.testzip() is None, "El proyecto tiene un CRC incorrecto"
            cls.project = json.loads(archive.read("project.json"))
        cls.serialized_blocks = {
            key: block for target in cls.project["targets"]
            for key, block in target.get("blocks", {}).items()
        }
        cls.blocks = {
            key: block
            for target in cls.project["targets"]
            for key, block in target.get("blocks", {}).items()
            if isinstance(block, dict)
        }

    def test_inicia_la_red_propia_sin_depender_de_un_router(self):
        ap = [b for b in self.blocks.values() if b["opcode"] == "WIFI_AP"]
        self.assertEqual(len(ap), 1, "Debe crear la red del auto")
        self.assertEqual(ap[0]["inputs"]["NAME"][1][1], "ESP32-CAR")
        self.assertFalse(any(
            b["opcode"] in {"CONNECT_WIFI", "CLOSE_AP"}
            for b in self.blocks.values()
        ))

    def test_conserva_los_siete_modos_de_la_app(self):
        modes = {b["fields"]["ONE"][0] for b in self.blocks.values()
                 if b["opcode"] == "carMotorV2_carMode"}
        self.assertEqual(modes, {
            "move", "led", "buzzer", "follow", "avoidance", "roundTrack", "8track"
        })

    def test_cada_llamada_tiene_el_modo_original_y_los_comentarios_abren_plegados(self):
        for key, block in self.blocks.items():
            if block["opcode"] == "carMotorV2_carExecute":
                name = block["fields"]["ONE"][0]
                matches = [p for p in self.blocks.values()
                           if p["opcode"] == "carMotorV2_carMode"
                           and p["fields"]["ONE"][0] == name]
                self.assertEqual(len(matches), 1, name)
                self.assertIsNone(matches[0]["parent"])
        for target in self.project["targets"]:
            for comment in target.get("comments", {}).values():
                self.assertTrue(comment["minimized"])

    def test_incorpora_mando_y_mantiene_la_placa_v2(self):
        self.assertIn("IR", self.project["extensions"])
        self.assertIn("carMotorV2", self.project["extensions"])
        self.assertTrue(any(b["opcode"] == "IR_Receiver_Module"
                            for b in self.blocks.values()))
        self.assertFalse(any(b["opcode"].startswith("carMotor_")
                             for b in self.blocks.values()))

    def test_no_quedan_referencias_de_bloques_rotas(self):
        for key, block in self.blocks.items():
            refs = [block.get("parent"), block.get("next")]
            for value in block.get("inputs", {}).values():
                refs.extend(v for v in value[1:] if isinstance(v, str))
            for ref in filter(None, refs):
                self.assertIn(ref, self.blocks, f"Referencia rota en {key}: {ref}")

    def test_mando_cubre_todos_los_movimientos_mecanum(self):
        directions = {
            b["fields"]["ONE"][0] for key, b in self.blocks.items()
            if key.startswith("completo_") and b["opcode"] == "carMotorV2_carMove"
        }
        self.assertEqual(directions, {
            "forward", "backward", "left", "right", "clockwise", "anticlockwise",
            "leftUp", "rightUp", "leftDown", "rightDown"
        })

    def test_la_ampliacion_preserva_bloques_y_recursos_oficiales(self):
        with ZipFile(ROOT / "acecode/fuentes/QD001_V2_APP_Oficial.sb3") as source:
            with ZipFile(PROJECT) as output:
                for name in source.namelist():
                    if name != "project.json":
                        self.assertEqual(source.read(name), output.read(name), name)
            official = json.loads(source.read("project.json"))
        original = {k: b for t in official["targets"]
                    for k, b in t.get("blocks", {}).items()}
        for key, block in original.items():
            self.assertIn(key, self.serialized_blocks)
            if isinstance(block, dict):
                for field in ("opcode", "fields", "mutation"):
                    self.assertEqual(block.get(field), self.blocks[key].get(field), key)
            else:
                self.assertEqual(block, self.serialized_blocks[key])

    def run_control(self, key=None, elapsed=0, active=0, waiting=0, app_command=63):
        """Ejecuta los bloques de selección; los actuadores solo se registran."""
        values = {"IR_activo": active, "IR_esperar_stop": waiting,
                  "IR_ultima_orden": 1000, "Speeds": 255}
        actions = []
        remaining_key = key
        original_callback = next(
            b["inputs"]["SUBSTACK"][1] for b in self.blocks.values()
            if b["opcode"] == "carMotorV2_spiderExecute"
        )
        definitions = {}
        for block in self.blocks.values():
            if block["opcode"] == "procedures_definition":
                prototype = self.blocks[block["inputs"]["custom_block"][1]]
                definitions[prototype["mutation"]["proccode"]] = block["next"]

        def value(raw):
            if isinstance(raw, str):
                block = self.blocks[raw]
                op = block["opcode"]
                if op == "GET_NOW_TIME":
                    return 1000 + elapsed
                if op == "IR_Receiver_Module":
                    nonlocal remaining_key
                    match = remaining_key == int(block["fields"]["PIN_TYPE"][0])
                    if match:
                        remaining_key = None
                    return match
                if op == "carMotorV2_carGetInstruct":
                    return app_command == int(block["fields"]["ONE"][0])
                inputs = block["inputs"]
                if op == "operator_equals":
                    return value(inputs["OPERAND1"][1]) == value(inputs["OPERAND2"][1])
                if op == "operator_subtract":
                    return value(inputs["NUM1"][1]) - value(inputs["NUM2"][1])
                if op == "operator_gt":
                    return value(inputs["OPERAND1"][1]) > value(inputs["OPERAND2"][1])
                raise AssertionError(f"Expresión no cubierta: {op}")
            if raw[0] == 12:
                return values[raw[1]]
            return int(raw[1]) if str(raw[1]).isdigit() else raw[1]

        def execute(start):
            while start:
                if not start.startswith("completo_"):
                    actions.append("APP")
                    return False
                block = self.blocks[start]
                op = block["opcode"]
                if op == "data_setvariableto":
                    values[block["fields"]["VARIABLE"][0]] = value(block["inputs"]["VALUE"][1])
                elif op == "control_if":
                    if value(block["inputs"]["CONDITION"][1]):
                        if execute(block["inputs"]["SUBSTACK"][1]):
                            return True
                elif op == "procedures_call":
                    execute(definitions[block["mutation"]["proccode"]])
                elif op == "carMotorV2_carStop":
                    actions.append("STOP")
                elif op == "carMotorV2_carMove":
                    actions.append(block["fields"]["ONE"][0])
                elif op == "return":
                    return True
                else:
                    raise AssertionError(f"Instrucción no cubierta: {op}")
                start = block["next"]
            return False

        execute(original_callback)
        return actions, values

    def test_una_orden_ir_no_se_sobrescribe_con_la_orden_vieja_de_la_app(self):
        actions, values = self.run_control(key=12, app_command=63)
        self.assertEqual(actions, ["forward"])
        self.assertEqual(values["IR_activo"], 1)

    def test_cada_tecla_ir_envia_solo_el_movimiento_documentado(self):
        for key, direction in {
            12: "forward", 13: "backward", 14: "anticlockwise", 15: "clockwise",
            1: "left", 3: "right", 4: "leftUp", 6: "rightUp",
            7: "leftDown", 9: "rightDown"
        }.items():
            with self.subTest(key=key):
                actions, _ = self.run_control(key=key)
                self.assertEqual(actions, [direction])

    def test_sin_renovacion_ir_se_detiene_y_no_reanuda_la_app(self):
        actions, _ = self.run_control(active=1, elapsed=101, app_command=69)
        self.assertEqual(actions, ["STOP"])

    def test_ok_detiene_y_mantiene_seleccionado_el_mando(self):
        actions, values = self.run_control(key=16)
        self.assertEqual(actions, ["STOP"])
        self.assertEqual(values["IR_activo"], 1)

    def test_volver_a_app_exige_stop_antes_de_aceptar_movimiento(self):
        actions, values = self.run_control(key=11, active=1, app_command=69)
        self.assertNotIn("APP", actions)
        self.assertEqual(values["IR_esperar_stop"], 1)
        actions, values = self.run_control(waiting=1, app_command=60)
        self.assertEqual(actions, ["STOP"])
        self.assertEqual(values["IR_esperar_stop"], 0)
        actions, _ = self.run_control()
        self.assertEqual(actions, ["APP"])


if __name__ == "__main__":
    unittest.main()
