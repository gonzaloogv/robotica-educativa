"""Consola USB: python pc/control_qd001.py --port COM6 (requiere pyserial)."""
import argparse
import json
import time

import serial


def receive(port, seconds=0.7):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        line = port.readline().decode("utf-8", errors="replace").strip()
        if line:
            try:
                print(json.dumps(json.loads(line), ensure_ascii=False))
            except ValueError:
                print(line)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()
    port = serial.Serial(port=None, baudrate=115200, timeout=0.1, write_timeout=2)
    port.dtr = False
    port.rts = False
    port.port = args.port
    port.open()
    try:
        port.write(b"estado\n")
        receive(port)
        print("Escribi ayuda para ver comandos; salir o Ctrl+C cierra y detiene.")
        while True:
            command = input("QD001> ").strip()
            if command.lower() in ("salir", "exit"):
                break
            if command:
                port.write(command.encode("utf-8") + b"\n")
                receive(port, 1.3 if command.lower() == "musica" else 0.7)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        try:
            port.write(b"parar\n")
            port.flush()
            receive(port, 0.2)
        finally:
            port.close()


if __name__ == "__main__":
    main()
