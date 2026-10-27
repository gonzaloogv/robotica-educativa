"""Pruebas de interbloqueos y protocolo sin acceder al robot."""
import importlib.util
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / "firmware_micropython"
sys.path.insert(0, str(SOURCE))
from safety import Safety


class Clock:
    PERIOD = 1 << 30

    def __init__(self):
        self.now = 0

    def ticks_ms(self):
        return self.now

    def ticks_add(self, tick, amount):
        return (tick + amount) % self.PERIOD

    def ticks_diff(self, a, b):
        return (a - b + self.PERIOD // 2) % self.PERIOD - self.PERIOD // 2


class SafetyTests(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()
        self.safe = Safety(self.clock)

    def test_boot_cannot_move(self):
        with self.assertRaises(ValueError):
            self.safe.start(80, 0)
        self.assertFalse(self.safe.armed())

    def test_near_invalid_or_old_sensor_blocks_movement(self):
        for distance, sampled_at in [(None, 0), (0, 0), (25, 0), (401, 0), (80, None), (80, -251)]:
            with self.subTest(distance=distance, sampled_at=sampled_at):
                self.safe.arm()
                with self.assertRaises(ValueError):
                    self.safe.start(distance, sampled_at)
                self.assertFalse(self.safe.armed())

    def test_pulse_stops_at_250_ms(self):
        self.safe.arm()
        self.safe.start(80, 0)
        self.clock.now = 249
        self.assertFalse(self.safe.must_stop(80, 200))
        self.clock.now = 250
        self.assertTrue(self.safe.must_stop(80, 200))

    def test_sensor_failure_or_obstacle_stops_current_movement(self):
        self.safe.arm()
        self.safe.start(80, 0)
        self.assertTrue(self.safe.must_stop(None, 0))
        self.assertTrue(self.safe.must_stop(10, 0))

    def test_arm_expires(self):
        self.safe.arm()
        self.clock.now = 15000
        self.assertFalse(self.safe.armed())
        with self.assertRaises(ValueError):
            self.safe.start(80, 15000)

    def test_disarm_cancels_authorization(self):
        self.safe.arm()
        self.safe.start(80, 0)
        self.safe.disarm()
        self.assertIsNone(self.safe.moving_until)
        with self.assertRaises(ValueError):
            self.safe.start(80, 0)

    def test_tick_wraparound(self):
        self.clock.now = self.clock.PERIOD - 10
        self.safe.arm()
        self.safe.start(80, self.clock.now)
        self.clock.now = 239
        self.assertFalse(self.safe.must_stop(80, 200))
        self.clock.now = 240
        self.assertTrue(self.safe.must_stop(80, 200))

    def test_missing_echo_is_not_reported_as_measured_obstacle(self):
        reason = self.safe.block_reason(None, 0, require_arm=False)
        self.assertIn("sin distancia valida", reason)
        self.assertNotIn("Obstaculo medido", reason)
        with self.assertRaisesRegex(ValueError, "sin distancia valida"):
            self.safe.start(None, 0)

    def test_near_obstacle_reports_measured_distance(self):
        self.assertIn("Obstaculo medido a 12.5 cm", self.safe.block_reason(12.5, 0))

    def test_fresh_clear_reading_reports_only_disarmed_state(self):
        self.assertIn("Motores desarmados", self.safe.block_reason(80, 0))
        self.assertIsNone(self.safe.block_reason(80, 0, require_arm=False))
        self.safe.arm()
        self.assertIsNone(self.safe.block_reason(80, 0))

    def test_pulse_end_is_not_reported_as_sensor_failure(self):
        self.safe.arm()
        self.safe.start(80, 0)
        self.clock.now = 250
        self.assertIn("Pulso terminado", self.safe.stop_reason(80, 200))


class ProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        machine = types.ModuleType("machine")
        for name in ("Pin", "PWM", "UART", "time_pulse_us"):
            setattr(machine, name, object)
        spec = importlib.util.spec_from_file_location("driver_under_test", SOURCE / "qd001.py")
        cls.driver = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"machine": machine}):
            spec.loader.exec_module(cls.driver)

    def test_zero_speed_for_all_motors(self):
        for motor, direction in [(1, 2), (2, 2), (3, 1), (4, 1)]:
            self.assertEqual(self.driver.motor_packet(motor, 0), bytes([motor, direction, 0, 13, 10]))

    def test_direction_inversion_and_manufacturer_scaling(self):
        self.assertEqual(self.driver.motor_packet(1, 80), b"\x01\x01\x3a\r\n")
        self.assertEqual(self.driver.motor_packet(3, 80), b"\x03\x02\x3a\r\n")
        self.assertEqual(self.driver.motor_packet(1, -255), b"\x01\x02\x64\r\n")
        self.assertEqual(self.driver.motor_packet(4, -255), b"\x04\x01\x64\r\n")

    def test_reject_invalid_motor_or_speed(self):
        for motor, speed in [(0, 0), (5, 0), (1, 256), (1, -256)]:
            with self.assertRaises(ValueError):
                self.driver.motor_packet(motor, speed)


if __name__ == "__main__":
    unittest.main()
