# QD001 con MicroPython: programa USB 0.1.1

Cargado el 27/10/2026 en el ESP32-D0WD-V3 del QD001 con Car Shield V2. El programa arranca detenido, con luces y buzzer apagados. No configura Wi-Fi ni el control infrarrojo. Esta primera versión permite usar el sensor ultrasónico, luces, una melodía breve y movimientos manuales por USB.

## Uso desde esta computadora

Cerrar ACECode y otros monitores serie. Desde la raíz del proyecto:

```powershell
.\.venv\Scripts\python.exe .\pc\control_qd001.py --port COM6
```

El puerto puede cambiar en otra computadora; detectarlo antes de usarlo. La consola usa 115200 baudios y requiere `pyserial`, ya disponible en el entorno local.

| Comando | Resultado |
| --- | --- |
| `estado` o `distancia` | Distancia en centímetros, validez del sensor y estado de movimiento |
| `ayuda` | Lista de órdenes |
| `luces on` / `luces off` | Enciende o apaga las luces y desarma motores |
| `musica` | Desarma motores y reproduce cuatro notas |
| `armar` | Habilita órdenes de movimiento durante 15 segundos si la distancia es válida y mayor a 25 cm |
| `adelante`, `atras` | Pulso manual hacia adelante o atrás |
| `izquierda`, `derecha` | Traslación lateral |
| `girar_izquierda`, `girar_derecha` | Giro sobre el eje |
| `parar` | Detiene y desarma |
| `salir` | El cliente envía parada y cierra el puerto |

La primera prueba física de movimiento debe hacerse con ruedas levantadas. Cada orden de movimiento tiene un límite nominal de 250 ms y velocidad fija 80/255, convertida al rango del Shield según el fabricante. La orientación real de las ruedas y el desplazamiento todavía no se probaron. No se aumenta automáticamente la potencia si no llega a moverse.

El programa exige sensor válido, reciente y distancia mayor a 25 cm para **todas** las direcciones. Ante obstáculo, dato inválido, orden inválida, vencimiento de autorización o error, ordena detenerse y desarma. No vuelve a moverse sin `armar` y una nueva orden. Una línea USB incompleta no bloquea el control de tiempo. `Ctrl+C` detiene y devuelve el intérprete.

Desde la versión 0.1.1, `estado` y `distancia` incluyen `motivo_bloqueo`. Los mensajes distinguen medición ausente, medición vencida, distancia fuera de rango, obstáculo medido y motores desarmados. La falta de eco válido no se presenta como un obstáculo confirmado; continúa bloqueando el movimiento. Para la prueba con ruedas levantadas se puede mantener una superficie plana a unos 50 cm frente al sensor. No se considera automáticamente libre el espacio por no recibir una distancia válida.

Los límites son de software: el tiempo de frenado físico no se midió y el Shield no tiene un watchdog de comunicación confirmado. Esta versión no promete parada independiente del ESP32 ante un bloqueo físico o pérdida de alimentación parcial.

## Conexiones usadas y fuente

Mapa obtenido del paquete oficial instalado de ACECode, no de un pinout de otro modelo:

| Función | Conexión |
| --- | --- |
| Motores Shield V2 | UART2: TX GPIO17, RX GPIO16, 9600, 8N1 |
| Ultrasónico | TRIG GPIO13, ECHO GPIO14 |
| Luces | GPIO2 y GPIO12 |
| Buzzer pasivo | GPIO33 |

Referencias locales: `C:/Program Files/ACECode/extraFiles/compile/sketch/ACB_CAR_ARM/ACB_CAR_ARM.cpp`, funciones `Vehicle_init_V2`, `motorControl` y `Ultrasonic_init`; pines de luces y buzzer del ejemplo oficial `QD001~QD010(V2)/QD001/4.4.2APPControlCar2(Final program).sb3`. No se modificó cableado. La lectura del ultrasónico funciona en la unidad conectada; no se afirma haber inspeccionado eléctricamente cada conexión.

La trama de cada motor es `[motor, sentido, velocidad, 13, 10]`. Los motores 3 y 4 invierten el sentido respecto de 1 y 2. La conversión de potencia reproduce el mapeo entero 0–255 a 40–100, con cero enviado como cero.

Documentación de MicroPython: [UART](https://docs.micropython.org/en/v1.29.0/library/machine.UART.html), [referencia ESP32](https://docs.micropython.org/en/v1.29.0/esp32/quickref.html) y [select.poll](https://docs.micropython.org/en/v1.29.0/library/select.html).

## Verificación realizada

- Catorce pruebas locales aprobaron interbloqueos, vencimiento de pulso, desarme, rollover del reloj, tramas del Shield y distinción entre falta de medición y obstáculo medido. No usan hardware.
- Los tres archivos `qd001.py`, `safety.py` y `main.py` se compilaron en el ESP32; sus SHA-256 coincidieron con los archivos locales.
- Lecturas reales previas al arranque: 40,1; 40,1; 40,1 cm. No son una calibración contra una distancia de referencia.
- Tras reinicio por software: sensor válido, `armado=false`, `moviendo=false`.
- La orden `parar` devolvió `detenido`, `armado=false`.
- El agente no ensayó desplazamientos, luces ni música durante la carga. En la prueba manual posterior, el usuario confirmó que las luces encienden y apagan y que la melodía se reproduce. Informó que `distancia` devolvía `null`, lo que motivó el diagnóstico descrito a continuación. No hay desplazamiento físico confirmado.
- Revisión posterior del `null`: veinte lecturas sin la referencia terminaron con `time_pulse_us=-1` y ECHO alto al vencer 25 ms. Eso indica vencimiento de la medición del pulso, no una distancia corta confirmada, según la [API oficial](https://docs.micropython.org/en/v1.29.0/library/machine.html#machine.time_pulse_us). Con la superficie que colocó el usuario a 40–60 cm, doce lecturas dieron entre 52,0 y 52,1 cm, tanto con límite de 25 ms como de 45 ms. No se modificó el límite normal de 25 ms.
- Se cargó la versión 0.1.1 y se verificaron hashes, arranque detenido y lectura válida. En una prueba posterior dio 51,2 cm; `armar` habilitó, `estado` indicó `armado=true`, `moviendo=false`, y `parar` dejó ambos valores en falso. No se enviaron direcciones ni se ensayaron desplazamientos. Los registros locales están en `downloads/diagnostico-ultrasonico-20261027.json`, `downloads/diagnostico-ultrasonico-con-objeto-20261027.json` y `downloads/verificacion-armado-sin-movimiento-20261027.json`.
- No se instalaron funciones de autonomía, servomotor, seguimiento de línea, aplicación ACEBOTT o control IR.

## Diagnóstico de motores pendiente

El usuario informó que una orden `adelante` aceptada a velocidad 80, seguida de `Pulso terminado`, no hizo girar las ruedas. Confirmó batería conectada y preparación para la prueba con ruedas levantadas y consola cerrada. Se envió después un único pulso al motor 1, velocidad de entrada 150, límite nominal 250 ms y comprobación ultrasónica activa. La lectura inicial fue 51,9 cm y el tiempo registrado hasta completar la orden de parada fue 272 ms, incluyendo las operaciones del bucle y la transmisión. El usuario tampoco observó giro en esta prueba. No hay confirmación de movimiento físico.

Registro local: `downloads/prueba-motor1-20261027.json`. El programa instalado conserva velocidad 80 y el arranque detenido; el pulso de diagnóstico no se agregó al arranque. Se reinició el programa y quedó detenido al finalizar.

El usuario indicó que la placa de motores dice V2.0. La biblioteca oficial local y el generador Arduino de `carMotorV2` coinciden en `Car_init(2)` con UART TX17/RX16 a 9600 baudios; las tramas enviadas se comprobaron en pruebas locales. Eso no acredita recepción por el Shield, alimentación efectiva de los motores ni compatibilidad física de esta unidad. No se probó otro mapa de GPIO. Falta verificar el circuito y alimentación del Shield antes de atribuir la causa a potencia, protocolo o una avería.

Registro local de la carga: `downloads/programa-qd001-20261027.json`, excluido de Git. Rama técnica: `trabajo/micropython-respaldo`. El [contexto de continuidad](../docs/estado_sesion_2026-10-27.md) resume las pruebas, las autorizaciones y el diagnóstico pendiente.

Para repetir las pruebas locales:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Para volver a cargar esta versión autorizada, sin reinstalar MicroPython ni tocar `boot.py`:

```powershell
.\.venv\Scripts\python.exe .\tools\cargar_programa_qd001.py --port COM6
```
