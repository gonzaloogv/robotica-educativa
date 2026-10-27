"""Carga el programa USB en MicroPython y verifica archivos y arranque detenido."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import serial


class Repl:
    def __init__(self, port):
        self.port = serial.Serial(port=None, baudrate=115200, timeout=0.1, write_timeout=5)
        self.port.dtr = False
        self.port.rts = False
        self.port.port = port
        self.port.open()

    def until(self, marker, timeout=15):
        result = b""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            result += self.port.read(4096)
            if marker in result:
                return result
        raise RuntimeError("No llego la respuesta esperada: " + repr(result[-600:]))

    def enter(self):
        self.port.write(b"\r\x03\x03\x01")
        self.until(b"raw REPL; CTRL-B to exit\r\n>")

    def execute(self, source):
        data = source.encode("utf-8")
        for offset in range(0, len(data), 128):
            self.port.write(data[offset:offset + 128])
            time.sleep(0.01)
        self.port.write(b"\x04")
        response = self.until(b"\x04>")
        if not response.startswith(b"OK"):
            raise RuntimeError("REPL rechazo el programa: " + repr(response))
        chunks = response[2:].split(b"\x04")
        if len(chunks) != 3 or chunks[1].strip():
            raise RuntimeError("Error en ESP32: " + response.decode("utf-8", errors="replace"))
        return chunks[0].decode("utf-8", errors="replace").strip()

    def command(self, command):
        self.port.write(command.encode("utf-8") + b"\n")
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            line = self.port.readline().decode("utf-8", errors="replace").strip()
            try:
                return json.loads(line)
            except ValueError:
                continue
        raise RuntimeError("El programa no respondio al comando: " + command)


def main():
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = [root / "firmware_micropython" / name for name in ("qd001.py", "safety.py", "main.py")]
    for file in files:
        compile(file.read_text(encoding="utf-8"), file.name, "exec")
    repl = Repl(args.port)
    record = {"port": args.port, "files": {}, "motor_movement_tested": False}
    try:
        repl.enter()
        identity = repl.execute('import sys\nprint(sys.implementation.name, sys.platform)')
        if identity != "micropython esp32":
            raise RuntimeError("No se encontro MicroPython ESP32: " + identity)
        for file in files:
            data = file.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            temporary = file.name + ".nuevo"
            code = (
                "import os, hashlib, binascii\n"
                f"data = {data!r}\n"
                f"compile(data.decode(), {file.name!r}, 'exec')\n"
                f"with open({temporary!r}, 'wb') as f:\n f.write(data)\n"
                f"with open({temporary!r}, 'rb') as f:\n result = binascii.hexlify(hashlib.sha256(f.read()).digest()).decode()\n"
                f"assert result == {digest!r}\n"
                f"os.rename({temporary!r}, {file.name!r})\n"
                "os.sync()\nprint(result)\ndel data\n"
            )
            if repl.execute(code) != digest:
                raise RuntimeError("No coincide el archivo escrito: " + file.name)
            record["files"][file.name] = digest
            print("OK archivo", file.name, digest)
        diagnostics = repl.execute(
            "import qd001, json, time\n"
            "r = qd001.Robot()\n"
            "try:\n"
            " samples = []\n"
            " for _ in range(3):\n"
            "  samples.append(r.distance_cm())\n"
            "  time.sleep_ms(100)\n"
            " print(json.dumps({'distancias_cm': samples}))\n"
            "finally:\n r.close()\n"
        )
        record["sensor_samples"] = json.loads(diagnostics)
        print("DIAGNOSTICO", diagnostics)
        repl.port.write(b"\x02")
        repl.until(b">>>")
        repl.port.write(b"\x04")
        startup = repl.until(b'"listo"', timeout=20).decode("utf-8", errors="replace")
        record["startup"] = startup
        # Esperar el resto del mensaje de arranque antes del primer comando.
        time.sleep(0.2)
        repl.port.reset_input_buffer()
        status = repl.command("estado")
        if status.get("armado") is not False or status.get("moviendo") is not False:
            raise RuntimeError("El arranque no quedo detenido: " + repr(status))
        record["status"] = status
        stop = repl.command("parar")
        if stop.get("estado") != "detenido" or stop.get("armado") is not False:
            raise RuntimeError("No se confirmo la parada: " + repr(stop))
        record["stop"] = stop
        destination = root / "downloads/programa-qd001-20261027.json"
        destination.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        print("OK arranque", json.dumps(status, ensure_ascii=False))
        print("OK parada", json.dumps(stop, ensure_ascii=False))
        print("Carga completada; no se probaron movimientos ni musica.")
    finally:
        repl.port.close()


if __name__ == "__main__":
    main()
