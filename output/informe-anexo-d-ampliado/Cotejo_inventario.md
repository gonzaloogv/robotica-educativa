# Cotejo del inventario del kit ACEBOTT QD001

Se recuperaron íntegramente las 34 entradas de la Tabla 4 original. Se leyeron visualmente los 34 recuadros de Product List del manual oficial V2 (página PDF 4, numerada 3). Coinciden las denominaciones y cantidades; las diferencias de guiones, espacios o mayúsculas son tipográficas.

| Componente original | Cantidad original | Cantidad oficial V2 | Resultado |
| --- | ---: | ---: | --- |
| ESP32 Max V1.0 Controller Board | 1 | 1 | Coincide |
| ESP32 Car Shield V2.0 | 1 | 1 | Coincide |
| Blue LED Module | 2 | 2 | Coincide |
| P-Buzzer Module | 1 | 1 | Coincide |
| IR Receiver Module | 1 | 1 | Coincide |
| Ultrasonic Sensor | 1 | 1 | Coincide |
| Trace Sensor | 1 | 1 | Coincide |
| TT DC Geared Motor | 4 | 4 | Coincide |
| Mecanum Wheel | 4 | 4 | Coincide |
| IR Remote Control | 1 | 1 | Coincide |
| Servo SG90 9G | 1 | 1 | Coincide |
| 18650 Battery Holder | 1 | 1 | Coincide |
| Motor Bracket | 4 | 4 | Coincide |
| Coupler | 4 | 4 | Coincide |
| USB Cable 1 m | 1 | 1 | Coincide |
| F-F 3P Dupont Wire | 6 | 6 | Coincide |
| F-F 4P Dupont Wire | 2 | 2 | Coincide |
| F-F 5P Dupont Wire | 2 | 2 | Coincide |
| Screwdriver | 1 | 1 | Coincide |
| Cross Wrench | 1 | 1 | Coincide |
| Ultrasonic Bracket | 1 | 1 | Coincide |
| Acrylic Board | 1 | 1 | Coincide |
| M3 × 10 mm Round Head Screws | 39 | 39 | Coincide |
| M3 × 30 mm Round Head Screws | 10 | 10 | Coincide |
| M2 × 10 mm Round Head Screws | 8 | 8 | Coincide |
| M2 × 25 mm Round Head Self-Tapping Screws | 5 | 5 | Coincide |
| M3 × 8 mm Flat Head Screws | 5 | 5 | Coincide |
| M1.4 × 5 mm Large Round Flat Head Tapping Screws | 3 | 3 | Coincide |
| M2 Nickel-Plated Nuts | 8 | 8 | Coincide |
| M3 Nickel-Plated Nuts | 31 | 31 | Coincide |
| M3 × 14 mm Single-pass Copper Pillar | 5 | 5 | Coincide |
| M3 × 40 mm Dual-pass Copper Pillar | 8 | 8 | Coincide |
| Nylon Cable Ties | 3 | 3 | Coincide |
| Black Tape | 1 | 1 | Coincide |

## Aclaraciones documentales

- Acrylic Board ×1 es el conjunto representado por dos placas. Los pasos 1 y 4 del manual identifican placa inferior y superior.
- Las dos celdas 18650 son de provisión separada. La Product List incluye un portabaterías, no las baterías.
- Las cantidades del paquete no se confunden con las cantidades usadas por paso. Por ejemplo, se declaran 5 tornillos M2 ×25 mm y se usan 4 en las ruedas.
- El Car Shield V2.0 coincide con el manual V2. La wiki QA052 titulada V1.0 y la tienda oficial V2.0 son documentos de variantes distintas; no se cambia silenciosamente la revisión del inventario.
- Los códigos QB de las fichas de módulos no aparecen en todas las entradas del inventario. La correspondencia física sigue pendiente cuando las inscripciones no se leen.
- La ficha del servo expresa el par como KG/cm. Se registra esa imprecisión y no se usa como especificación de diseño.
- La entrada de placa no es la tensión admisible en GPIO, y los 3 A publicados para el Shield no se interpretan como corriente continua por cada motor.
- No se encontró en las fuentes consultadas una ficha inequívoca con RPM, relación de reducción y corriente de bloqueo de los motores TT de este kit. No se inventan esos datos.

[Portal oficial de manuales](https://acebott.com/tutorial/)
[Paquete oficial V2](https://www.dropbox.com/scl/fo/nuvcm7jz61pyvkf2e6wqn/AL1zIzwhCVJPD_86wI9yRsY?rlkey=2sw5femcol2t2od43sqxhxaf9&st=oopqhoof&dl=0)
[Copia íntegra del manual consultado](fuentes-tecnicas/ACEBOTT_QD001_V2_Manual_de_montaje.pdf)
