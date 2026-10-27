"""Verifica la variante solicitada: STA con los modos completos y el mando."""

from copy import deepcopy
import json
from pathlib import Path
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
STA = ROOT / "acecode/versiones-ap-y-sta/QD001_V2_STA_IR_Completo.sb3"
AP = ROOT / "acecode/versiones-ap-y-sta/QD001_V2_AP_IR_Completo.sb3"


def read_project(path):
    with ZipFile(path) as archive:
        assert archive.testzip() is None
        project = json.loads(archive.read("project.json"))
        assets = {name: archive.read(name) for name in archive.namelist()
                  if name != "project.json"}
    return project, assets


class ProyectoSTAIRTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project, cls.assets = read_project(STA)
        cls.original, cls.original_assets = read_project(AP)
        cls.blocks = next(t["blocks"] for t in cls.project["targets"] if t.get("blocks"))
        cls.original_blocks = next(t["blocks"] for t in cls.original["targets"] if t.get("blocks"))

    def test_se_conecta_como_estacion_y_no_crea_un_punto_de_acceso(self):
        opcodes = [b["opcode"] for b in self.blocks.values() if isinstance(b, dict)]
        self.assertNotIn("WIFI_AP", opcodes)
        self.assertEqual(opcodes.count("CONNECT_WIFI"), 1)
        self.assertEqual(opcodes.count("CLOSE_AP"), 1)

    def test_las_credenciales_son_marcadores_y_el_ap_se_cierra_antes(self):
        key, connect = next((k, b) for k, b in self.blocks.items()
                            if isinstance(b, dict) and b["opcode"] == "CONNECT_WIFI")
        self.assertEqual(connect["inputs"]["NAME"][1][1], "CONFIGURAR_WIFI_2_4_GHZ")
        self.assertEqual(connect["inputs"]["PASSWORD"][1][1], "CONFIGURAR_CLAVE_WIFI")
        preceding = self.blocks[self.blocks[connect["parent"]]["parent"]]
        self.assertEqual(preceding["opcode"], "CLOSE_AP")
        self.assertEqual(self.blocks[connect["parent"]]["next"], key)

    def test_la_espera_consulta_estado_real_e_imprime_ip(self):
        wait = self.blocks["sta_wait_connected"]
        self.assertEqual(wait["opcode"], "control_wait_until")
        condition = self.blocks[wait["inputs"]["CONDITION"][1]]
        self.assertEqual(condition["opcode"], "operator_equals")
        status = self.blocks[condition["inputs"]["OPERAND1"][1]]
        self.assertEqual(status["opcode"], "WIFI_INFO")
        self.assertEqual(status["fields"]["INFO"][0], "INFO")
        self.assertEqual(condition["inputs"]["OPERAND2"][1][1], "1")
        self.assertEqual(self.blocks["sta_ip"]["fields"]["INFO"][0], "IP")
        self.assertEqual(self.blocks["sta_log_ip"]["fields"]["BAUD_RATE"][0], "115200")

    def test_los_modos_el_mando_y_los_recursos_quedan_iguales(self):
        ap_key = next(k for k, b in self.original_blocks.items()
                      if isinstance(b, dict) and b["opcode"] == "WIFI_AP")
        changed = {ap_key, self.original_blocks[ap_key]["parent"],
                   self.original_blocks[ap_key]["next"]}
        for key, original in self.original_blocks.items():
            self.assertIn(key, self.blocks)
            actual = deepcopy(self.blocks[key])
            expected = deepcopy(original)
            if key in changed and key != ap_key:
                for field in ("parent", "next"):
                    actual.pop(field, None)
                    expected.pop(field, None)
            if key != ap_key:
                self.assertEqual(actual, expected, key)
        self.assertEqual(self.project["extensions"], self.original["extensions"])
        self.assertEqual(self.assets, self.original_assets)

    def test_no_quedan_referencias_rotas(self):
        for key, block in self.blocks.items():
            if not isinstance(block, dict):
                continue
            refs = [block.get("parent"), block.get("next")]
            refs += [v for values in block.get("inputs", {}).values()
                     for v in values[1:] if isinstance(v, str)]
            for ref in filter(None, refs):
                self.assertIn(ref, self.blocks, f"Referencia rota en {key}: {ref}")


if __name__ == "__main__":
    unittest.main()
