"""Interbloqueos de movimiento sin dependencias de hardware."""
MIN_DISTANCE_CM = 25
MAX_SAMPLE_AGE_MS = 250
ARM_TIME_MS = 15000
PULSE_TIME_MS = 250


class Safety:
    def __init__(self, clock):
        self.clock = clock
        self.disarm()

    def disarm(self):
        self.armed_until = None
        self.moving_until = None

    def arm(self):
        self.armed_until = self.clock.ticks_add(self.clock.ticks_ms(), ARM_TIME_MS)

    def armed(self):
        return self.armed_until is not None and self.clock.ticks_diff(
            self.armed_until, self.clock.ticks_ms()
        ) > 0

    def block_reason(self, distance, sampled_at, require_arm=True):
        if distance is None or sampled_at is None:
            return "Ultrasonico sin distancia valida; no se confirma un obstaculo"
        age = self.clock.ticks_diff(self.clock.ticks_ms(), sampled_at)
        if not 0 <= age <= MAX_SAMPLE_AGE_MS:
            return "Medicion del ultrasonico vencida; esperar una lectura nueva"
        if not 2 <= distance <= 400:
            return "Distancia fuera del rango valido del programa"
        if distance <= MIN_DISTANCE_CM:
            return "Obstaculo medido a %.1f cm; minimo requerido: mas de 25 cm" % distance
        if require_arm and not self.armed():
            return "Motores desarmados; escribir armar antes de la direccion"
        return None

    def clear(self, distance, sampled_at):
        return self.block_reason(distance, sampled_at, require_arm=False) is None

    def start(self, distance, sampled_at):
        reason = self.block_reason(distance, sampled_at)
        if reason is not None:
            self.disarm()
            raise ValueError(reason)
        self.moving_until = self.clock.ticks_add(self.clock.ticks_ms(), PULSE_TIME_MS)

    def must_stop(self, distance, sampled_at):
        return self.stop_reason(distance, sampled_at) is not None

    def stop_reason(self, distance, sampled_at):
        if self.moving_until is None:
            return None
        if self.clock.ticks_diff(self.moving_until, self.clock.ticks_ms()) <= 0:
            return "Pulso terminado; volver a armar para otro movimiento"
        if not self.armed():
            return "Habilitacion de motores vencida"
        return self.block_reason(distance, sampled_at, require_arm=False)
