# Revisión del informe de Robótica Educativa

El borrador respeta la estructura general solicitada y desarrolla una relación clara entre robótica, programación y estadística. Todavía no constituye un informe final: faltan el programa autónomo, la documentación del montaje, las mediciones propias, los resultados y las conclusiones. El material complementario aportado informa que el robot ya está armado y que se comprobó su desplazamiento mediante la app oficial por Wi-Fi; esos avances deben incorporarse al informe.

Esta revisión compara el contenido disponible con las pautas y la rúbrica. Las fechas quedan fuera del análisis. La evaluación se limita a los documentos y archivos disponibles; no acredita funcionamiento del robot ni desempeño del grupo en una defensa oral.

## Documentos revisados

- [Pautas de organización](<../ROBOTICA - PAUTAS DE ORGANIZACIÓN 2026.pdf>): seis páginas con requisitos del informe, la presentación y la defensa.
- [Rúbrica de evaluación](<../Rúbrica Proyecto IEN 2026.pdf>): cuatro páginas con los criterios de la defensa y sus ponderaciones.
- [Informe de Robótica Educativa](<../Informe Robótica Educativa.pdf>): borrador de 17 páginas.
- [Contexto técnico del QD001](../CONTEXTO_PARA_CODEX_ACEBOTT_QD001.md): avances informados por el grupo, fuentes y condiciones para preservar el firmware y preparar la programación.
- [Plan de correcciones](../CAMBIOS_INFORME_ROBOTICA_2026.md), también disponible en [PDF](../PLAN_DE_CAMBIOS_INFORME_ROBOTICA.pdf): cambios por página, textos propuestos y auditoría de fuentes aportada. El PDF tiene siete páginas y reproduce el plan; no es una nueva versión del informe.

Las referencias de página que siguen corresponden al PDF del informe de 17 páginas. Los documentos originales se conservan sin modificaciones. Se mantiene la indicación de omitir las fechas de esta revisión, aunque los documentos complementarios incluyan propuestas sobre ellas.

## Información nueva aportada por el grupo

| Información | Consecuencia para el trabajo |
| --- | --- |
| Robot armado y sensor ultrasónico instalado | La sección de armado ya puede describir esa experiencia con los hechos aportados, las fotografías y las dificultades que el grupo confirme. |
| Desplazamiento correcto con la app oficial por Wi-Fi | Existe una prueba manual informada por el grupo. Debe documentarse con ese alcance; todavía no acredita autonomía, precisión del sensor ni frenado automático. |
| Objetivo de movimiento automático y detención ante obstáculos | Precisa la tarea del proyecto. El diseño inicial se centrará en avanzar y detenerse; girar o esquivar no integra ese mínimo. |
| Preferencia por MicroPython ejecutándose en el ESP32 | Resuelve la intención tecnológica. La factibilidad, el pinout y la conservación del firmware actual siguen por comprobar. |
| Autonomía y captura de mediciones todavía no probadas | Los resultados estadísticos y las conclusiones continúan pendientes de ensayos reales. |
| Plan de correcciones y auditoría de bibliografía disponibles | Aportan textos y referencias para editar el informe. La accesibilidad de todos los enlaces no se revalidó en esta actualización. |

Se trata de avances reportados en los documentos del grupo. Esta revisión no realizó pruebas sobre el dispositivo. El plan de diagnóstico, los scripts y la estructura de repositorio propuestos en el contexto quedan como referencia para trabajo posterior; esta actualización solo incorpora la información a la documentación existente.

## Comparación de los apartados obligatorios

| Apartado | Estado | Evidencia y trabajo pendiente |
| --- | --- | --- |
| 1. Portada | Presente | Página 1. Incluye institución, carrera, asignatura, título, integrantes, docente, curso y turno. |
| 2. Índice | Presente | Página 2. Los apartados y las páginas coinciden con el borrador. Deberá actualizarse al incorporar el material faltante. |
| 3. Introducción | Desarrollada | Página 3. Presenta el tema, su importancia, la elección y el contenido previsto. La referencia a datos obtenidos deberá corresponder con los resultados que finalmente se incorporen. |
| 4. Problema y objetivos | Desarrollados | Página 4. Incluye pregunta, objetivo general y cinco objetivos específicos. Debe precisarse el foco en movimiento autónomo y detención, y traducir precisión y confiabilidad a variables y criterios medibles. |
| 5. Marco teórico | Parcial | Páginas 5 a 8. Incluye robótica, Python, sensores, medición, estadística, probabilidad, regresión y antecedentes. El contexto complementario propone MicroPython en ESP32; falta adaptar la explicación y confirmar los componentes utilizados. |
| 6. Desarrollo técnico | Parcial | Páginas 9 a 12. Identifica el QD001 y propone ensayos. El contexto complementario ya aporta el armado finalizado y una prueba manual por Wi-Fi; falta integrarlos al informe con fotos. Siguen pendientes conexiones confirmadas, programa autónomo y procedimiento experimental ejecutado. Las figuras son espacios reservados. |
| 7. Resultados y análisis | Pendiente | Página 13. Hay tablas vacías y preguntas orientadoras. Faltan mediciones, cálculos, gráficos e interpretación vinculada con los objetivos. |
| 8. Conclusión | Pendiente | Página 14. Contiene instrucciones para redactarla. Debe responder la pregunta de investigación con los resultados y explicar los aprendizajes y las limitaciones del trabajo. |
| 9. Bibliografía | Parcial | Páginas 15 y 16. Hay fuentes y enlaces. El plan complementario aporta una auditoría y referencias más específicas. Falta incorporarlas según su pertinencia, completar la referencia de la cátedra y cerrar las verificaciones pendientes. |
| 10. Anexos | Parcial | Página 17. Están enumerados los anexos y aparece el inventario del kit. Faltan el código, los datos crudos, las fotografías, las fichas técnicas y los cálculos anunciados. El inventario no reemplaza las fichas técnicas. |

## Requisitos formales

| Requisito del instituto | Comprobación en el borrador |
| --- | --- |
| A4 y márgenes de 2,5 cm | Las páginas miden aproximadamente 595 × 842 puntos. Los bordes del texto principal se ubican a unos 70,86 puntos de los laterales, equivalentes a 2,5 cm. El contenido principal revisado respeta el área prevista. |
| Arial o Times New Roman, cuerpo 12 | El texto general utiliza Arial de 12 puntos. Hay excepciones en código, fórmulas, leyendas y tablas; las tablas del desarrollo usan aproximadamente 11 puntos y el inventario del anexo, 10. Conviene confirmar si se admiten estas excepciones o unificar el tamaño. |
| Títulos de 14 puntos en negrita | Los títulos principales utilizan aproximadamente 14 puntos en negrita. Los subtítulos usan 12 puntos en negrita. Para una aplicación estricta de la pauta, revisar el tamaño de los subtítulos. |
| Interlineado 1,5 y texto justificado | Los párrafos generales revisados presentan separación de líneas de 18 puntos para cuerpo 12 y alineación justificada. Las tablas tienen espaciado propio. |
| Desarrollo numerado | Las páginas del desarrollo muestran numeración. |
| Entre 8 y 15 páginas de desarrollo | Hay 14 páginas desde la introducción hasta el final de la bibliografía, o 12 sin bibliografía. Ambos recuentos entran en el rango, excluyendo portada, índice y anexos. Debe comprobarse nuevamente al completar el contenido. |
| Recursos visuales con título, número y fuente | Las figuras previstas y las tablas tienen identificadores y fuentes. Faltan las fotografías, el diagrama y los gráficos reales. |
| Redacción formal y documento completo | La base tiene una redacción adecuada. Permanecen marcadores de completar, tablas vacías y textos que instruyen al grupo sobre qué escribir. Deben reemplazarse al finalizar el trabajo. |
| Entrega digital e impresa | Existe un PDF digital. La preparación de la copia impresa no puede verificarse con los archivos disponibles. |

La comprobación de formato combina extracción de fuentes y posiciones con inspección visual de páginas representativas. No reemplaza la revisión de la versión final después de incorporar código, gráficos y fotografías.

## Ajustes técnicos y estadísticos recomendados

### Confirmar el montaje y la modalidad de Python

Las páginas 5 y 6 mezclan referencias a ESP32, Raspberry Pi Pico, Arduino UNO, HC-SR04 y L298. Algunas son ejemplos generales y otras todavía no están confirmadas para el prototipo. Debe quedar explícito cuáles corresponden al robot utilizado.

La [página del QD001 de ACEBOTT](https://acebott.com/es/stem-kits/explorer-series/acebott-omni-wheel-car-robot-starter-kit-collection/) declara ESP32, ruedas Mecanum y compatibilidad con Python. Esa información no confirma por sí sola el modelo del sensor, el driver, el pinout ni el firmware de la unidad recibida.

Antes de escribir el control del hardware hay que identificar esos elementos y la alimentación. Si se utiliza MicroPython, la explicación y los ejemplos deberán corresponder al ESP32 y a la versión instalada; existe una [referencia oficial específica para ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html). La referencia RP2 puede conservarse como comparación, pero no reemplaza la documentación del equipo elegido.

El contexto complementario identifica QB042/QB093 como una posible referencia de sensor y advierte que su modelo y su conexión genérica no están confirmados para esta unidad. No corresponde sustituir las especificaciones del informe ni adoptar un mapa de GPIO hasta comprobar esa correspondencia.

La prueba con la app también establece un funcionamiento previo que interesa conservar. Antes de reemplazar el firmware se deberá definir una estrategia de respaldo y recuperación, y evaluar si existe una alternativa documentada compatible con el objetivo. La elección final de tecnología continúa pendiente de esa comprobación.

### Definir qué significa que la tarea se cumplió

El informe original propone evasión de obstáculos y un ensayo de frenado sin precisar su relación. El contexto nuevo fija como tarea el desplazamiento autónomo y la detención ante obstáculos. Esa definición debe trasladarse a introducción, objetivos y desarrollo técnico; la maniobra de esquive queda fuera del mínimo descrito.

Para cada corrida se necesita una regla previa de éxito o fracaso: posición inicial, movimiento solicitado, obstáculo, distancia mínima aceptada y condición de finalización. Los valores se establecerán según el montaje y las pruebas; no se pueden deducir de las plantillas actuales.

El contexto nuevo establece detener el movimiento ante lecturas inválidas, expiradas o ausentes y disponer de una parada manual. El procedimiento debe explicar cómo se implementa y registra esa respuesta. Así, la explicación del algoritmo y el recuento de resultados tendrán el mismo criterio.

### Precisar las repeticiones y el registro

La página 11 propone al menos 30 repeticiones por ensayo, pero no aclara si corresponden al total o a cada condición. Hay que indicar las repeticiones por distancia, punto de calibración o configuración de movimiento.

Cada conjunto de datos debe identificar ensayo, condición, unidades y resultados. El protocolo deberá indicar cómo se mantiene o registra el estado de la batería y qué se hace con lecturas ausentes, valores atípicos y corridas interrumpidas. Los datos originales se conservan y cualquier exclusión se justifica.

La cantidad de repeticiones es una propuesta del borrador y debe acordarse para el experimento. Las consignas del instituto no fijan 30 como requisito obligatorio.

### Separar correlación y exactitud

La pregunta de la página 13 sobre si el error cambia con la distancia o el ángulo no se resuelve únicamente con la pendiente de la recta y el coeficiente de correlación.

Un ejemplo matemático es una lectura que siempre duplica la distancia real: tiene correlación perfecta y, aun así, presenta error sistemático. Para evaluar la calibración conviene analizar también la diferencia entre valor medido y valor de referencia, el sesgo, el error absoluto medio y los residuos del ajuste. Si se quiere estudiar el ángulo, debe registrarse y variarse expresamente en el ensayo.

### Precisar las condiciones de los modelos estadísticos

Promediar lecturas puede reducir la variabilidad del promedio bajo las condiciones adecuadas; no elimina automáticamente la dispersión de cada lectura ni corrige un sesgo. Conviene ajustar la explicación de la página 6 en ese sentido.

Para la binomial, justificar por qué las corridas pueden tratarse como ensayos independientes y con probabilidad de éxito aproximadamente constante. Si cambian la distancia, la velocidad o el obstáculo, corresponde identificar y analizar esas condiciones. La frecuencia observada estima la probabilidad de éxito; no la convierte en un valor conocido sin incertidumbre.

Los intervalos de confianza también deben acompañarse de sus supuestos y del tamaño de muestra. Un histograma orienta el análisis, pero no demuestra por sí solo que los datos sigan una distribución normal.

### Mantener un alcance experimental manejable

Repetibilidad, calibración y frenado se relacionan directamente con el sensor y la tarea de detención. El plan complementario coincide en priorizar esos tres y deja el ensayo de velocidad según PWM como opcional.

El PDF original todavía enumera los cuatro ensayos y permanece sin modificaciones. La regresión deberá utilizarse cuando la relación observada y el propósito del análisis la justifiquen.

## Presentación y defensa oral

Las pautas piden una presentación de apoyo de entre 8 y 12 diapositivas, una exposición orientativa de 15 a 20 minutos y una demostración del prototipo de 10 minutos. Todos los integrantes deben participar y conocer el contenido completo. No hay una presentación entre los archivos disponibles.

La rúbrica permite identificar qué evidencias conviene preparar; no corresponde asignar una nota anticipada al grupo.

| Criterio | Peso | Evidencia pendiente o a preparar |
| --- | --- | --- |
| Dominio del tema | 20 puntos | Explicar las decisiones técnicas y responder preguntas con fundamentos. El PDF no acredita por sí solo ese dominio. |
| Aplicación de Probabilidad y Estadística | 20 puntos | Aplicar los conceptos a datos propios, justificar los modelos e interpretar sus límites. La teoría está presente; la aplicación está pendiente. |
| Relación entre Programación y Robótica | 15 puntos | Mostrar el algoritmo y relacionar lecturas, decisiones, actuadores y datos. Falta código y demostración. |
| Calidad de la presentación oral | 15 puntos | Ensayar claridad, vocabulario, contacto visual y administración del tiempo. No verificable con los archivos actuales. |
| Material de apoyo | 10 puntos | Elaborar diapositivas legibles con fotografías, diagramas y resultados. Pendiente. |
| Trabajo en equipo | 10 puntos | Preparar una participación equilibrada y conocimiento compartido. La portada enumera integrantes, pero no acredita la participación. |
| Presentación personal y actitud profesional | 10 puntos | Se evalúa durante la defensa y no puede inferirse del informe. |

La programación del repositorio aportará evidencia especialmente a la relación entre programación y robótica y a la aplicación de estadística, pero la defensa también evalúa la comprensión y la comunicación del trabajo.

## Prioridades para completar el trabajo

1. Confirmar componentes y conexiones con el kit disponible; evaluar MicroPython y la conservación del firmware que permite el control manual.
2. Definir la tarea, las condiciones experimentales y los criterios de éxito.
3. Una vez definido el entorno y autorizado el trabajo sobre el equipo, programar el avance, la detención y el registro de datos en este repositorio, documentando su funcionamiento.
4. Ejecutar los ensayos elegidos y conservar sus datos y registros.
5. Completar resultados, gráficos, conclusiones y anexos a partir de esa evidencia.
6. Ajustar formato, índice y bibliografía; preparar y ensayar la presentación.

## Alcance de la verificación

La revisión inicial abarcó los tres PDF originales y el contenido inicial del repositorio. Se comprobaron los apartados, la extensión, las fuentes tipográficas, posiciones de texto y páginas renderizadas. Se contrastó la descripción general del QD001 con ACEBOTT y se consultó la documentación de MicroPython para ESP32. La actualización incorpora los dos documentos Markdown nuevos y el PDF del plan de correcciones, cuya primera página también se inspeccionó visualmente. Se volvió a consultar la documentación oficial del QD001 indicada en el contexto.

La bibliografía completa, los resultados de los antecedentes, el hardware recibido y el funcionamiento físico no se validaron en esta revisión. La prueba manual se conoce por la documentación del grupo; no se ejecutó desde este repositorio. No hay mediciones ni código propio con los que comprobar la autonomía todavía. Los resultados y las conclusiones deberán provenir de los ensayos del grupo.
