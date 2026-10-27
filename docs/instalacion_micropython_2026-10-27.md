# Instalación de MicroPython — 27/10/2026

Rama de trabajo: `trabajo/micropython-respaldo`.

Se instaló MicroPython 1.29.0, variante ESP32_GENERIC, en el ACEBOTT QD001 con ESP32-D0WD-V3 revisión 3.1 y 4 MB de flash. El usuario autorizó instalarlo y después indicó expresamente omitir el respaldo del firmware actual.

El intento de respaldo previo falló durante la lectura por una interrupción USB; no produjo una imagen completa validada. Tras reconectar el USB, se borró la flash y se escribió el firmware desde `0x1000` con esptool 5.6.0 a 115200 baudios. La herramienta confirmó `Hash of data verified` y reinició la placa.

Se comprobó por REPL en COM6: versión `1.29.0`, plataforma `esp32`, intérprete `micropython` y sistema de archivos con `boot.py`. El puerto se cerró al terminar esa comprobación. En esa etapa inicial no se cargó un programa del robot ni se enviaron órdenes a motores o GPIO. Luego se cargó y probó el programa USB; su evolución y el fallo pendiente de motores están en [el contexto de continuidad](estado_sesion_2026-10-27.md).

El programa ACEBOTT quedó reemplazado. Las funciones de la aplicación del fabricante requieren su firmware o una implementación compatible; instalar MicroPython por sí solo no implementa movimiento, sensores, música ni control Wi-Fi.

El respaldo cifrado del 23/10/2026 permanece intacto y corresponde al estado anterior a la restauración que hizo el usuario. No hay respaldo validado del estado estable inmediatamente anterior a esta instalación. No se probó restauración en hardware.

Firmware oficial: https://micropython.org/download/ESP32_GENERIC/

Archivo utilizado: `ESP32_GENERIC-20260824-v1.29.0.bin`, 1.790.544 bytes.

SHA-256: `e67ad6015a0a504c1fec9aa9bbf589d0432ed28e62546f4f8dd8a147f8bd95f6`.

Los registros de escritura y de verificación por REPL quedaron locales en `downloads/instalacion-micropython-20261027.log` y `downloads/instalacion-micropython-20261027.json`, excluidos de Git. Esta documentación conserva el resultado y los límites de la instalación sin publicar los archivos binarios.
