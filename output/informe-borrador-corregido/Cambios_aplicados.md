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


## Actualización del 30 de octubre de 2026

- Por decisión del grupo y con autorización de la docente, el informe pasa a utilizar y explicar el programa de fábrica de ACEBOTT. Se ajustaron título, introducción, pregunta, objetivos, marco teórico, desarrollo, metodología y anexos para mantener ese alcance.
- Se sustituyeron las propuestas de programación en Python/MicroPython y de análisis con sus bibliotecas por el estudio del programa del fabricante y el registro en planillas con hoja de cálculo. Se retiraron las dos referencias de MicroPython porque ya no se citan ni forman parte de la tecnología elegida. El resto de las fuentes se conserva.
- Se incorporó la confirmación del grupo de que el 27/10 el robot funcionó hasta agotarse las baterías. No se agregó un tiempo de autonomía ni una causa técnica del diagnóstico intermedio.
- Se corrigió el registro del 27/10 para distinguir el cierre confirmado, la nueva decisión académica y los antecedentes técnicos de las pruebas.
- Se conservan autores, docente, fecha de presentación, inventario de 34 entradas, ocho tablas, ocho fotografías y siete ecuaciones. Las secciones 7 y 8 mantienen pendientes los ensayos y la conclusión experimental.
- El anexo A queda preparado para completar la identificación exacta y la explicación del código del fabricante. No se atribuyen al grupo funciones autónomas implementadas ni resultados experimentales.
- Se actualizan índice, paginación y PDF tras la edición. No se modifica firmware ni se accede a puertos del robot.


## Comparación y revisión del programa de control

Se comparó el PDF de 33 páginas con el Word aportado `Informe_Robotica_Educativa_borrador_fabrica.docx`, cuya exportación tenía 35 páginas y 16 páginas de desarrollo y bibliografía. El Word aportado se eligió como base por su metodología de observación, video y planillas, más adecuada para evaluar el programa sin depender de un registro interno de datos. Se conservaron los archivos aportados sin modificarlos.

- Se retiraron del borrador las menciones al permiso docente y la denominación «programa de fábrica», también en los metadatos; se utiliza «programa de control» y se conservan las fuentes técnicas.
- Se identificó el procedimiento confirmado por el grupo: ACECode, firmware QD y programa final 4.4.2APPControlCar2. La carpeta en español contiene una copia de referencia .sb3 y una ruta Arduino separada.
- Se explicó la rutina de evasión a partir del proyecto de referencia y se distinguió el umbral nominal de 25 cm de la distancia física que se medirá.
- Se retiró la afirmación no sustentada de control IR integrado al programa final y se distinguieron los ejemplos IR separados del paquete.
- Se precisó la primera detención como variable de medición, sin mezclarla con un giro o una posición final. Se mantiene el registro de fallos y la evaluación de evasión sin contacto ni intervención manual.
- Se trasladó el detalle repetido de la incidencia al anexo A y se reformuló como práctica futura el registro sistemático de las clases, que no estaba confirmado como actividad ya realizada.
- Se recuperó la explicación válida del control PWM del servomotor y la aclaración de sus especificaciones que faltaban en el Word aportado.
- Se conservan el inventario completo, las ocho fotografías, las ocho tablas, las siete ecuaciones y los resultados experimentales pendientes. Se actualizan el índice y la exportación PDF.
- Se comprobó la nueva referencia de software de ACEBOTT: https://acebott.com/es/software/. No se modificó firmware ni se ejecutaron instaladores o programas del robot.
