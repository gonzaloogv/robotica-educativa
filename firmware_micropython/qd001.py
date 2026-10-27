"""Control del QD001 con Car Shield V2; basado en el protocolo de ACECode."""
from machine import Pin, PWM, UART, time_pulse_us
import time

VERSION = "0.1.1-usb"
DIRECTIONS = {
    "adelante": (1, 1, 1, 1),
    "atras": (-1, -1, -1, -1),
    "izquierda": (-1, 1, 1, -1),
    "derecha": (1, -1, -1, 1),
    "girar_izquierda": (-1, -1, 1, 1),
    "girar_derecha": (1, 1, -1, -1),
}


def motor_packet(motor, speed):
    if motor not in (1, 2, 3, 4) or not -255 <= speed <= 255:
        raise ValueError("Motor o velocidad fuera de rango")
    direction = 1 if speed > 0 else 2
    if motor in (3, 4):
        direction = 3 - direction
    value = 0 if speed == 0 else 40 + abs(speed) * 60 // 255
    return bytes((motor, direction, value, 13, 10))


class Robot:
    def __init__(self):
        self.uart = UART(2, baudrate=9600, tx=17, rx=16, timeout=0)
        self.stop()
        self.trig = Pin(13, Pin.OUT, value=0)
        self.echo = Pin(14, Pin.IN)
        self.leds = (Pin(2, Pin.OUT, value=0), Pin(12, Pin.OUT, value=0))
        self.buzzer = PWM(Pin(33), freq=440, duty_u16=0)

    def stop(self):
        for motor in (1, 2, 3, 4):
            self.uart.write(motor_packet(motor, 0))
        self.uart.flush()

    def move(self, direction, speed=80):
        vector = DIRECTIONS[direction]
        for motor, sign in enumerate(vector, 1):
            self.uart.write(motor_packet(motor, sign * speed))
        self.uart.flush()

    def distance_cm(self):
        self.trig.value(0)
        time.sleep_us(2)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        pulse = time_pulse_us(self.echo, 1, 25000)
        if pulse <= 0:
            return None
        distance = pulse / 58.0
        return round(distance, 1) if 2 <= distance <= 400 else None

    def lights(self, enabled):
        for led in self.leds:
            led.value(1 if enabled else 0)

    def song(self):
        # El controlador desarma los motores antes de tocar esta melodia.
        try:
            for note in (262, 330, 392, 523):
                self.buzzer.freq(note)
                self.buzzer.duty_u16(12000)
                time.sleep_ms(180)
                self.buzzer.duty_u16(0)
                time.sleep_ms(40)
        finally:
            self.buzzer.duty_u16(0)

    def close(self):
        self.stop()
        self.buzzer.duty_u16(0)
        self.buzzer.deinit()
        self.lights(False)
