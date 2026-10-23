# Cambios aplicados al informe

Se trabajó sobre el Word correspondiente a `Informe_Robotica_Educativa_noterminado.pdf`. El PDF de partida coincide con la última versión entregada. Ambos archivos de partida se conservaron sin modificaciones.

1. Se reescribió el texto con tono académico de estudiantes y voz afirmativa. Se retiraron las menciones al proceso de edición, al borrador, a auditorías y a la conservación del informe anterior. Las limitaciones experimentales se concentran en los apartados correspondientes.
2. Se fijó Arial en las declaraciones explícitas de fuente y se eliminaron los atributos de tema que podían sustituirla por Calibri. Los encabezados y el título utilizan Arial 14 en negrita; el cuerpo mantiene Arial 12, A4, márgenes de 2,5 cm, interlineado 1,5 y texto justificado. Las URL y las celdas conservan la alineación adecuada para su lectura.
3. Se incorporó la versión V2.0 confirmada mediante la caja y el video de montaje. Se actualizó la fila «Control y expansión» de la Tabla 1 con la redacción solicitada y se ajustó el Anexo D.3.
4. Se agregó el párrafo solicitado sobre la Car Shield, PWM y sentido de giro independiente de los motores. La identificación del circuito integrado de potencia permanece pendiente.
5. Se incorporó en 5.3 y D.4 la redacción solicitada sobre el sensor ACEBOTT compatible con la interfaz HC-SR04 y el rango documentado de los modelos QB042/QB093. Se mantuvo AccuDIY (2011) en 5.3 y en la bibliografía.
6. Se reemplazó la experiencia de armado por la secuencia informada: preparación del acrílico, sensor de línea, separadores, motores y soportes, placas y módulos, servo y sensor ultrasónico, portabaterías, placa superior, ruedas y cableado. Se redactó la resolución de las dificultades a partir de lo indicado por el grupo: pausar el video para estudiar la colocación de los motores y comparar los cables con el paso correspondiente.
7. Se mantuvo la comprobación manual por Wi-Fi. La instalación de MicroPython y el programa autónomo se describen como próximos pasos; el resguardo del firmware se explica de forma breve.
8. Se eliminó D.6 completo, incluidas las referencias a Raspberry Pi Pico, pyFirmata y L298 y sus enlaces. También se retiró su entrada del índice. El 74HC595 no aparecía en el documento y no se incorporó como componente confirmado.
9. La bibliografía comienza únicamente con «Fecha de consulta: 20 de octubre de 2026.». Todas las fuentes digitales muestran su URL completa y mantienen un hipervínculo al mismo destino.
10. Se agregaron las diez fuentes solicitadas y se mantuvo además la ficha comercial de la Car Shield V2.0 ya utilizada en el anexo. La bibliografía reúne 24 referencias. Las once fuentes de ACEBOTT sin fecha se diferencian con s. f.-a a s. f.-k y las citas se ajustaron a esa asignación.
11. Los enlaces de Dropbox se sustituyeron por `https://acebott.com/tutorial/`.
12. Se mantuvieron las 34 entradas y cantidades del inventario, las ocho fotografías, las ocho tablas y las siete ecuaciones. Las tablas de registro permanecen sin datos experimentales.
13. Se conservaron la institución, la docente, los cinco integrantes y la fecha de presentación del 30 de octubre de 2026.
14. Se actualizaron el índice y los números de página a partir de la versión exportada y se revisó la composición del PDF completo.

## Referencias de ACEBOTT sin fecha

| Sufijo | Fuente |
| --- | --- |
| s. f.-a | Ficha comercial ESP32 Car Shield V2.0 |
| s. f.-b | QA007/QA008/QA009 ESP32 Max V1.0 Controller Board |
| s. f.-c | QA052 ESP32 Car Shield, página titulada V1.0 |
| s. f.-d | QB001/QB073+QB053 Infrared Remote Control Module |
| s. f.-e | QB007/QB081 LED Module |
| s. f.-f | QB010/QB077 P-Buzzer Module |
| s. f.-g | QB042/QB093 Ultrasonic Sensor |
| s. f.-h | QB054 Servo SG90 9G Module 180 Degree |
| s. f.-i | QB060/QB080 Trace Sensor |
| s. f.-j | QD001 Smart Car Starter Kit for ESP32 |
| s. f.-k | Tutoriales de kits STEM y manuales del kit |

## Puntos pendientes y alcance

- Las secciones 7 y 8 mantienen pendientes los ensayos, sus resultados y la conclusión experimental. No se añadieron mediciones, cálculos ni resultados propios.
- La identificación específica del sensor, el circuito integrado de potencia y las comprobaciones eléctricas siguen pendientes, tal como se solicita. Esto no modifica la confirmación del kit V2.0.
- Se aplicaron todos los cambios solicitados. La única redacción libre fue la explicación de cómo se resolvieron las dificultades de armado, utilizando la información aportada en el pedido y sin añadir incidentes ni acciones técnicas.
- No se modificó el firmware ni se ejecutó código en el robot.

## Verificación

Se verificaron el contenido, los destinos y el texto visible de los enlaces, la correspondencia del índice con las páginas, la conservación del inventario, las fotografías y las ecuaciones, y el formato del documento. La revisión visual final y las huellas de los entregables se registran en `Verificacion_entrega.json`. Typecheck, lint, tests y build de aplicación no corresponden a esta corrección documental.


## Ajustes finales de enlaces y puntuación

- Se eliminó una de las dos URL idénticas bajo la Tabla 6 (página 24).
- Se retiró el punto anterior a la cita de ACEBOTT en 5.3 y D.4 (páginas 6 y 28).
- Se mantuvieron el resto del contenido, el inventario, las fotografías y las ecuaciones.
