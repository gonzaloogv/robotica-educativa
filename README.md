# Robótica educativa — proyecto completo de ACECode

Las dos versiones para elegir están juntas en
**[acecode/versiones-ap-y-sta](acecode/versiones-ap-y-sta/README.md)**:

| Archivo | Conexión |
| --- | --- |
| [QD001_V2_AP_IR_Completo.sb3](acecode/versiones-ap-y-sta/QD001_V2_AP_IR_Completo.sb3) | Crea `ESP32-CAR`, clave `12345678`. |
| [QD001_V2_STA_IR_Completo.sb3](acecode/versiones-ap-y-sta/QD001_V2_STA_IR_Completo.sb3) | Se conecta a una red existente de 2,4 GHz; completar SSID y clave en una copia local. |

Ambas conservan el mando IR y los mismos modos. Se carga una versión a la vez;
son candidatas para pruebas físicas. La carpeta incluye instrucciones y un
registro de verificación del 24/10/2026.

Rama de programación `trabajo/acecode-completo`. Para la conexión solicitada a una red
Wi-Fi existente, abrir **[QD001_V2_STA_IR_Completo.sb3](acecode/versiones-ap-y-sta/QD001_V2_STA_IR_Completo.sb3)**.
Consultar [la configuración STA y sus límites](acecode/sta-ir/README.md).
Hay que completar el nombre y la clave de la red en una copia local.

La [variante AP + IR](acecode/QD001_V2_AP_IR_Completo.sb3) y
[su guía](acecode/PROYECTO_COMPLETO.md) se conservan como alternativa.

La variante AP crea la red propia `ESP32-CAR`. Ambas variantes incluyen los siete modos del ejemplo oficial V2
(movimiento, luces, música, seguimiento de objeto, evasión y dos recorridos de línea)
y manejo con el mando infrarrojo. Conserva los 434 bloques originales y agrega
107 bloques para integrar el mando, detener durante el cambio de control y
completar las cuatro direcciones diagonales de la app. La variante STA agrega
otros ocho bloques para cerrar AP, conectar a la red, comprobar el estado y mostrar la IP.

La [variante STA anterior](acecode/QD001_V2_STA_Completo.sb3) y
[sus instrucciones](acecode/README.md) se conservan. Esa variante usa un router,
requiere completar SSID y clave en una copia local y no crea `ESP32-CAR`.

El trabajo se realiza en archivos y en la computadora. El proyecto nuevo no se
cargó en el robot; las comprobaciones físicas están pendientes. MicroPython
continúa como una etapa separada. El informe académico no se modifica con
resultados que todavía no se obtuvieron.

La [revisión de mejoras pendientes](acecode/versiones-ap-y-sta/Mejoras_pendientes.md)
registra los ajustes de parada, conexión, sensores y tiempos que todavía no se
aplicaron a estas versiones.

Verificación sin robot, con Python 3 y su biblioteca estándar:

```text
python -m unittest discover -s tests -v
python -m py_compile tools/preparar_completo.py tests/test_proyecto_completo.py tests/test_proyecto_sta_ir.py
node --check tools/preparar_sta.js
```

Documentación del proyecto en la rama [documentacion](https://github.com/gonzaloogv/robotica-educativa/tree/documentacion).
