# Registro de cambios del informe de Robótica Educativa

Se corrigió el contenido del PDF original y se reconstruyó una versión editable en Word. El original se conserva sin modificaciones. La nueva versión se entrega junto con su exportación PDF, auditoría bibliográfica y lista de información pendiente.

## Elementos conservados

- Estructura académica: portada, índice, introducción, problema y objetivos, marco teórico, desarrollo técnico, resultados, conclusión, bibliografía y anexos.
- Institución, carrera, asignatura, docente, curso y turno del documento original.
- Integrantes, con la misma escritura del original: Cardozo Agustin, Gomez Gonzalo, Medina Marcos, Monzon Esteban y Rojas Angel.
- Fecha de presentación existente: 30 de octubre de 2026.
- Tema de vinculación entre robótica y Probabilidad y Estadística, y estudios de Zapata y Hunter una vez comprobados.

## Correcciones de contenido efectuadas

| Apartado | Cambio realizado |
| --- | --- |
| Portada | Se reformuló el título como propuesta de programación y evaluación, para evitar afirmar que el robot ya fue programado en Python. Se conservaron integrantes y fecha. |
| Índice | Se reconstruyó con títulos, subtítulos, páginas y vínculos internos correspondientes al PDF corregido. |
| Introducción | Se distinguió el contexto educativo de los logros del grupo. Se incorporaron el armado y la prueba manual y se retiró la anticipación de resultados experimentales inexistentes. |
| Problema y objetivos | Se precisó la pregunta sobre error de medición y frecuencia de detención correcta. Los objetivos de programación y ensayos se presentan como metas pendientes. |
| Marco de programación | Se sustituyeron Pico/RP2 y la discusión de Arduino UNO por MicroPython para ESP32. Se explica ejecución en placa frente a Python en PC, sin afirmar instalación ni prueba. |
| Componentes | Se retiró la atribución de HC-SR04 y L298 al robot. Se distinguieron las denominaciones del borrador de la identificación física pendiente de la unidad. Se eliminó el inventario comercial como prueba del montaje. |
| Medición | Se mantuvo el factor 2 del tiempo de ida y vuelta y se aclararon unidades. Se definió error como lectura menos referencia; se reconoció la incertidumbre del instrumento de referencia. |
| Estadística | Se corrigieron las explicaciones sobre promedio, sesgo, incertidumbre Tipo A, independencia, intervalo t, cobertura y normalidad. Se aclaró que r alto no demuestra exactitud y que deben analizarse error y residuos. |
| Fórmulas | Se reconstruyeron como ecuaciones nativas editables de Word: distancia, error/sesgo/MAE, media y desvío muestral, binomial, intervalo t y regresión. La incertidumbre Tipo A del promedio también utiliza notación matemática editable. |
| Antecedentes | Se conservaron Zapata 2025 y Hunter 2023 con su método y valores verificados. Se identifican como estudios de otros montajes HC-SR04. No se copió una calibración ajena para usarla en el QD001. |
| Armado | Se incorporó inicio el 16/10/2026 y finalización el 20/10/2026. Se describió la respuesta manual mediante la app oficial por Wi-Fi, sin inventar incidentes o dificultades. |
| Programa previsto | Se describió el ciclo leer, validar, decidir, actuar y registrar. La detención ante obstáculos y lecturas inválidas es un requisito de diseño futuro. Se mantiene la programación como etapa separada. |
| Metodología | Se prepararon repetibilidad, calibración y frenado, unidades de observación, trazabilidad, referencia, repeticiones por condición y manejo de fallos. Los números propuestos se identifican como propuestas, sin simular ejecución. PWM queda opcional. |
| Resultados | Se informó únicamente el avance manual conocido. Se prepararon tablas vacías de repetibilidad y frenado y la estructura del análisis de calibración. Las celdas vacías no representan cero. |
| Conclusión | Se expresó el alcance actual y la imposibilidad de responder todavía la pregunta experimental. No se inventaron probabilidades, errores del sensor, aprendizajes individuales ni autonomía alcanzada. |
| Bibliografía | Se comprobaron los 15 destinos originales y las alternativas. Se retiraron fuentes ajenas al montaje, se añadieron secciones oficiales de estadística y se incorporaron enlaces completos de los antecedentes. La auditoría detalla cada resultado. |
| Anexos | Se prepararon cinco anexos para código real, registros, fotografías, documentación del montaje y análisis. Se añadió un esquema de campos que diferencia lecturas, referencias externas y observaciones manuales. |

## Formato aplicado

- A4 con márgenes de 2,5 cm.
- Arial de 12 puntos en cuerpo, bibliografía y tablas; títulos y subtítulos de 14 puntos en negrita.
- Interlineado 1,5 y párrafos del cuerpo justificados. Las ecuaciones y el índice utilizan un espaciado específico para conservar su legibilidad.
- Tablas numeradas con fuente y filas de encabezado repetibles; filas sin recorte de altura.
- Portada e índice sin número visible. Desarrollo numerado desde la página física 3.
- Índice enlazado y bibliografía con enlaces de texto legible.
- Archivo Word editable, con ecuaciones nativas, y PDF exportado a partir de esa misma versión.

La exportación final se verifica mediante renderizado de todas sus páginas. El registro técnico de comprobación se guarda en `Verificacion_entrega.json`.

## Límites de la corrección

No se cambió el firmware, no se abrió un puerto del robot y no se accionaron motores. Tampoco se incorporaron mediciones, fotografías, conexiones o configuraciones no disponibles. La versión está corregida en los aspectos documentales que permiten los hechos conocidos; los resultados y la conclusión experimental deben completarse después de los ensayos.

## Actualización de anexos con fotografías aportadas el 20/10/2026

- Nueva versión independiente en `output/informe-con-fotos`; se conservan la entrega corregida anterior y el PDF original.
- Anexo C: se reemplazó el marcador pendiente por seis fotografías de preparación, montaje y estado ensamblado, con números, títulos y procedencia.
- Anexo D: se incorporaron dos vistas de detalle y una tabla que separa observaciones visuales de identificaciones técnicas pendientes.
- Se documentó la presencia visible de cuatro motores con reductora, ruedas Mecanum, sensor frontal sobre servomotor, placas superpuestas y portabaterías para dos celdas cilíndricas. No se atribuyen especificaciones eléctricas o modelos ilegibles.
- Se aclaró que V2.0 en el embalaje no identifica la revisión del Shield.
- Se actualizó el párrafo del apartado 6.2 que anunciaba fotografías futuras para remitir a los anexos ya incorporados.
- Se conservaron los ocho archivos de imagen sin modificar sus bytes y se registraron sus huellas SHA-256 y nombres originales.
- Se ordenaron las fotos por estado visible del armado; no se dedujeron fechas de toma de los nombres de WhatsApp.
- Se mantienen integrantes, fecha de presentación, fechas de armado y carácter propuesto de MicroPython y de la funcionalidad autónoma.
- El anexo E conserva su contenido y comienza en una página propia.
- Se actualizó la lista de información pendiente. No se agregaron mediciones, incidentes, resultados experimentales ni conclusiones nuevas.
- La bibliografía y su auditoría no cambian: esta actualización aporta evidencia fotográfica, sin nuevas fuentes técnicas externas.
