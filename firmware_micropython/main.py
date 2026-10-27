"""Programa USB del QD001. Arranca detenido; Ctrl+C detiene y sale al REPL."""
import json
import select
import sys
import time
from qd001 import Robot, VERSION, DIRECTIONS
from safety import Safety

COMMANDS = "ayuda, estado, distancia, armar, parar, adelante, atras, izquierda, derecha, girar_izquierda, girar_derecha, luces on, luces off, musica"


def run():
    robot = None
    try:
        robot = Robot()
        safe = Safety(time)
        poll = select.poll()
        poll.register(sys.stdin, select.POLLIN)
        distance, sampled_at = None, None
        buffer = ""
        overflow = False

        def reply(**values):
            print(json.dumps(values))

        def stop(disarm=True):
            robot.stop()
            if disarm:
                safe.disarm()
            else:
                safe.moving_until = None

        reply(evento="listo", version=VERSION, estado="detenido", comandos=COMMANDS)
        while True:
            reason = safe.stop_reason(distance, sampled_at)
            if reason is not None:
                stop()
                reply(evento="parada_automatica", motivo=reason)
            now = time.ticks_ms()
            if sampled_at is None or time.ticks_diff(now, sampled_at) >= 100:
                distance = robot.distance_cm()
                sampled_at = time.ticks_ms()
            reason = safe.stop_reason(distance, sampled_at)
            if reason is not None:
                stop()
                reply(evento="parada_automatica", motivo=reason)
            for event in poll.poll(5):
                if event[1] & (select.POLLHUP | select.POLLERR):
                    raise OSError("Consola USB desconectada")
                if not event[1] & select.POLLIN:
                    continue
                char = sys.stdin.read(1)
                if not char:
                    raise OSError("Consola USB cerrada")
                if char not in "\r\n":
                    if len(buffer) >= 80:
                        overflow = True
                        stop()
                    elif not overflow:
                        buffer += char
                    continue
                if not buffer and not overflow:
                    continue
                command = buffer.strip().lower()
                buffer = ""
                if overflow:
                    overflow = False
                    reply(error="Comando demasiado largo; motores detenidos")
                    continue
                try:
                    if command in ("ayuda", "help", "?"):
                        reply(comandos=COMMANDS)
                    elif command in ("estado", "distancia"):
                        reply(version=VERSION, distancia_cm=distance, sensor_valido=distance is not None,
                              armado=safe.armed(), moviendo=safe.moving_until is not None,
                              motivo_bloqueo=safe.block_reason(distance, sampled_at))
                    elif command in ("parar", "stop", "s"):
                        stop()
                        reply(estado="detenido", armado=False)
                    elif command == "armar":
                        stop()
                        reason = safe.block_reason(distance, sampled_at, require_arm=False)
                        if reason is not None:
                            raise ValueError(reason)
                        safe.arm()
                        reply(armado=True, validez_segundos=15)
                    elif command in DIRECTIONS:
                        safe.start(distance, sampled_at)
                        robot.move(command)
                        reply(movimiento=command, duracion_ms=250, velocidad=80)
                    elif command in ("luces on", "luces off"):
                        stop()
                        robot.lights(command == "luces on")
                        reply(luces=command == "luces on")
                    elif command == "musica":
                        stop()
                        robot.song()
                        reply(musica="terminada")
                    else:
                        raise ValueError("Comando desconocido; usar ayuda")
                except Exception as exc:
                    stop()
                    reply(error=str(exc), estado="detenido")
    except KeyboardInterrupt:
        print("QD001 detenido; consola MicroPython disponible.")
    finally:
        if robot is not None:
            robot.close()


if __name__ == "__main__":
    run()
