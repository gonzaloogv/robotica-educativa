# Preparación de MicroPython

Actualizado al 23/10/2026. Leer primero [el estado de continuidad](docs/estado_sesion_2026-10-23.md).

## Descarga realizada

- Candidato: MicroPython 1.29.0, ESP32_GENERIC, publicación 2026-08-24.
- Fuente: https://micropython.org/download/ESP32_GENERIC/
- Copia local: `downloads/micropython/ESP32_GENERIC-20260824-v1.29.0.bin`.
- Tamaño registrado: 1.790.544 bytes.
- SHA-256 local: `E67AD6015A0A504C1FEC9AA9BBF589D0432ED28E62546F4F8DD8A147F8BD95F6`.

La huella registra la copia local; no es un cotejo con una firma publicada. El binario no está incluido en esta rama documental y puede obtenerse de su fuente oficial.

## Estado

Se identificó ESP32-D0WD-V3 revisión 3.1 con 4 MB de flash, coherente con la familia ESP32_GENERIC. Faltan confirmar el montaje y sus adaptadores. MicroPython NO se instaló y no se implementó código del robot en esta sesión.

El usuario informó funcionamiento correcto con un firmware estable tras restaurar desde ACECode. Su nuevo respaldo y comparación se pospusieron al desconectar el equipo. El respaldo anterior está íntegro, pero no debe confundirse con ese estado estable ni con una imagen de fábrica.

La instrucción vigente es no modificar el robot. Se puede avanzar en lógica y pruebas en PC mediante [la guía sin hardware](docs/continuidad_micropython_sin_robot.md). La publicación de documentos no abre puertos ni cambia firmware.

## Integración pendiente

Identificar el proyecto estable; respaldar y verificar ese estado; documentar recuperación; confirmar protocolo del Shield V2, sensor, conexiones y niveles eléctricos; y recién entonces decidir la instalación y efectuar pruebas físicas graduales. Las pruebas en PC no reemplazan esos pasos.
