# Preparación de MicroPython

Actualizado al 27/10/2026. MicroPython 1.29.0 ya está instalado y el programa Python USB 0.1.1 está cargado. Leer primero [el contexto vigente](docs/estado_sesion_2026-10-27.md) y [el registro de instalación](docs/instalacion_micropython_2026-10-27.md).

## Descarga realizada

- Candidato: MicroPython 1.29.0, ESP32_GENERIC, publicación 2026-08-24.
- Fuente: https://micropython.org/download/ESP32_GENERIC/
- Copia local: `downloads/micropython/ESP32_GENERIC-20260824-v1.29.0.bin`.
- Tamaño registrado: 1.790.544 bytes.
- SHA-256 local: `E67AD6015A0A504C1FEC9AA9BBF589D0432ED28E62546F4F8DD8A147F8BD95F6`.

La huella registra la copia local; no es un cotejo con una firma publicada. El binario no está incluido en esta rama documental y puede obtenerse de su fuente oficial.

## Estado

Se identificó ESP32-D0WD-V3 revisión 3.1 con 4 MB de flash. Se instaló ESP32_GENERIC 1.29.0, se verificó la escritura y se comprobó el intérprete por USB. Después se cargó el programa USB con arranque detenido. Luces, melodía y ultrasónico respondieron; los motores no giraron visiblemente y siguen en diagnóstico.

El usuario había informado funcionamiento correcto con un firmware estable tras restaurar desde ACECode. El 27/10 autorizó reemplazarlo por MicroPython y pidió omitir la captura del estado actual después de fallar un intento de lectura por USB. El respaldo anterior está íntegro, pero no debe confundirse con ese estado estable ni con una imagen de fábrica. No se probó restauración funcional.

El código está en `trabajo/micropython-respaldo` y las guías en `documentacion`. La [guía sin hardware](docs/continuidad_micropython_sin_robot.md) conserva el plan previo y orienta el trabajo en PC; el contexto del 27/10 prevalece para el estado del robot. La publicación de documentos no abre puertos ni cambia firmware.

## Integración pendiente

Resolver el control de motores: contrastar el circuito V2.0 real, alimentación efectiva y recepción de órdenes antes de cambiar el mapa de control. Después validar sentidos, desplazamiento y parada. Autonomía, registro CSV, calibración y ensayos estadísticos siguen pendientes; las pruebas locales no acreditan esos resultados.
