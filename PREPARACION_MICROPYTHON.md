# Preparación de MicroPython

Actualización 27/10/2026: MicroPython 1.29.0 ya está instalado y verificado por USB en el ESP32. El usuario autorizó reemplazar el programa ACEBOTT y luego indicó omitir el respaldo del estado actual. El respaldo anterior permanece conservado. Ver [registro de instalación](docs/instalacion_micropython_2026-10-27.md). El texto siguiente conserva el contexto de la preparación previa.

Se revisaron README.md y CONTEXTO_PARA_CODEX_ACEBOTT_QD001.md de origin/documentacion (la rama mencionada como documentos).

Proyecto: ACEBOTT QD001, ESP32 Max V1.0 y Car Shield V2.0. Objetivo: avance autónomo, detención ante obstáculos y registro USB/CSV para análisis estadístico. El control manual Wi-Fi funcionó según el grupo; autonomía y mediciones siguen pendientes.

Firmware descargado: MicroPython 1.29.0, ESP32_GENERIC, publicación 2026-08-24.
Página oficial: https://micropython.org/download/ESP32_GENERIC/
Archivo local: downloads/micropython/ESP32_GENERIC-20260824-v1.29.0.bin
Procedencia, tamaño y SHA-256 local: downloads/micropython/manifest.json.
La huella registra el archivo descargado; no constituye una comparación con una firma o huella publicada por el fabricante.

Es un candidato para el ESP-WROOM-32 indicado en la documentación. Antes de instalar hay que confirmar chip y flash reales, preservar el firmware original y revisar su recuperación. El firmware original permite usar la app ACEBOTT; reemplazarlo puede perder esa función mientras MicroPython esté instalado.

No se conectó al puerto serie, no se leyó ni escribió la flash y no se activaron motores. No se cambiaron ramas ni se modificó la documentación original.

Próximos pasos: identificar la unidad y puerto USB, preparar herramientas de diagnóstico y respaldo, confirmar GPIO del Shield V2.0 y luego desarrollar lectura del sensor con parada ante lecturas inválidas. Coordinar cualquier acceso al dispositivo según el contexto técnico antes de ejecutarlo.

Actualización 2026-10-23: el equipo conectado fue identificado como ESP32-D0WD-V3 revisión 3.1 con 4 MB de flash. Se creó un respaldo verificado del firmware original sin reemplazarlo. Se trabaja en trabajo/micropython-respaldo; origin/documentacion no fue modificada. El usuario pidió probar el firmware actual antes de cualquier reemplazo. Consultar docs/procedimiento_respaldo_y_restauracion.md para ubicaciones, verificaciones y límites del respaldo. MicroPython continúa solamente descargado, sin instalar. Los GPIO del Shield siguen pendientes de verificación.
