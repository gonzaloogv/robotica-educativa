# Auditoría bibliográfica del informe corregido

Consulta realizada el 20 de octubre de 2026. Se comprobaron individualmente los 15 destinos distintos de los hipervínculos del PDF original, incluidos los que aparecen dentro del texto, y las fuentes añadidas a la versión corregida. Los enlaces duplicados se agruparon por destino; las páginas indicadas corresponden al PDF original.

La comprobación incluyó abrir el recurso, identificar autoría y documento, leer los apartados pertinentes y contrastarlos con las afirmaciones del informe. Un código HTTP 200 acredita el acceso al recurso recuperado, pero no garantiza su exactitud científica ni su disponibilidad futura. Los errores de cuota del servicio de extracción se reintentaron y no se clasificaron como enlaces caídos.

## Resultado general

- De los 15 destinos originales, 13 permitieron acceder al contenido pertinente. Dos destinos de Hunter devolvieron bloqueos de acceso al editor.
- Se verificó el texto completo de Zapata en arXiv. Se conserva como preprint, sin presentarlo como un artículo con revisión por pares.
- Se verificó el texto completo de Hunter mediante una copia del PDF del mismo artículo alojada en ResearchGate. Coinciden autor, título, revista, año y DOI. El informe enlaza esa copia completa.
- La bibliografía corregida contiene 13 referencias con enlaces a contenido pertinente accesible en la comprobación. Las fuentes sobre RP2, Arduino UNO, L298 y control de servos no se utilizan para describir el montaje.
- El manual HC-SR04 se conserva únicamente para explicar un ejemplo general de tiempo de vuelo. No identifica el sensor del grupo ni permite atribuirle especificaciones.

## Todos los enlaces del PDF original

### O01 ACEBOTT QD001

Enlace: [página comercial oficial del QD001](https://acebott.com/es/stem-kits/explorer-series/acebott-omni-wheel-car-robot-starter-kit-collection/). Aparece en las páginas 5, 9 y 16.

Resultado: HTTP 200. Se leyeron la descripción, las funciones y la tabla de plataforma y lenguajes. Declara ESP32, ruedas Mecanum, seguimiento de línea, detección de obstáculos y distintas formas de control.

Decisión: sustituir como referencia principal por la documentación oficial del QD001, ver A07. Las capacidades del producto se distinguen de lo efectivamente implementado por el grupo. Esta página no verifica el pinout ni el driver de la unidad recibida.

### O02 Zapata 2025

Enlace: [ficha académica arXiv 2506.06314](https://arxiv.org/abs/2506.06314). Aparece en las páginas 8, 12 y 16.

Resultado: HTTP 200. Se verificaron Allan Zapata, título, año, identificador, resumen y vínculo al PDF. El texto completo se verificó también, ver A04.

Decisión: conservar. La ficha no se utilizó como sustituto de la lectura del trabajo completo. El informe corregido enlaza el PDF de arXiv.

### O03 Resolución CFE 343/18 y NAP

Enlace: [documento oficial alojado por Educ.ar](https://backend.educ.ar/refactor_resource/get-attachment/162). Aparece en las páginas 3, 5 y 15.

Resultado: HTTP 200, contenido del documento completo. Se leyeron la resolución, en particular el artículo 1 que aprueba los NAP, y los pasajes relativos a programación, robótica y aprendizaje.

Decisión: conservar para el contexto educativo argentino. Se formula que la resolución aprobó los NAP; no se usa como prueba de los resultados del robot.

### O04 MicroPython y módulo machine

Enlace: [machine y funciones de acceso al hardware](https://docs.micropython.org/en/latest/library/machine.html). Aparece en las páginas 5 y 15.

Resultado: HTTP 200. Se revisaron las clases del módulo y la función time_pulse_us: mide duración en microsegundos y puede devolver valores negativos cuando agota la espera.

Decisión: conservar para explicar el programa previsto. Se aclara que la documentación corresponde a latest y que la versión elegida deberá verificarse. No se afirma que se haya instalado o ejecutado.

### O05 Referencia MicroPython RP2

Enlace: [Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html). Aparece en las páginas 5 y 15.

Resultado: HTTP 200. El propio encabezado identifica Raspberry Pi RP2 y Pico.

Decisión: retirar de la bibliografía final y reemplazar por A06, específico de ESP32. El acceso correcto al enlace no resuelve su falta de correspondencia con la plataforma propuesta.

### O06 DOI de Albarello y Hafner Táboas

Enlace: [DOI 10.26439/contratexto2019.n032.4607](https://doi.org/10.26439/contratexto2019.n032.4607). Aparece en la página 15.

Resultado: HTTP 200 con redirección a la ficha editorial de Contratexto. Se comprobaron autores, título, volumen 32, páginas 71-93, fecha y resumen. Se leyó el texto completo desde Redalyc, ver O14.

Decisión: conservar el estudio y su DOI como identificador. La bibliografía enlaza la copia completa en Redalyc. En esta comprobación el DOI funcionó; no se conserva como vigente el error informado en el diagnóstico anterior.

### O07 DOI de Hunter

Enlace: [DOI 10.62962/001c.87939](https://doi.org/10.62962/001c.87939). Aparece en la página 16.

Resultado: redirección al editor con HTTP 403. No se pudo leer el contenido por esa ruta. El error de acceso no demuestra que el artículo sea inexistente.

Decisión: conservar el DOI como identificador y reemplazar el vínculo de consulta por el PDF íntegro verificado en ResearchGate, ver A17. No se declara que el DOI haya permitido acceder al texto.

### O08 Ficha abreviada de Hunter

Enlace: [ficha de la revista con identificador 87939](https://ewuurj.scholasticahq.com/article/87939). Aparece en la página 8.

Resultado: primer intento con error de túnel del servicio de extracción; repetición con HTTP 403. No se verificó el texto desde esa página.

Decisión: reemplazar la ruta de consulta por A17. El artículo se conserva porque pudo cotejarse su texto completo y su identidad por la alternativa.

### O09 Foro Arduino UNO y Python

Enlace: [Python based curriculum for Arduino Uno](https://forum.arduino.cc/t/python-based-curriculum-for-arduino-uno/993550). Aparece en las páginas 5 y 15.

Resultado: HTTP 200. Se leyó la discusión sobre ejecución de Python desde computadora y el uso de Arduino UNO. Es un intercambio de foro, no documentación de ESP32 o del QD001.

Decisión: retirar del marco y de la bibliografía del informe corregido. La explicación se centra en la tecnología prevista para el equipo del grupo.

### O10 Manual HC-SR04

Enlace original: [manual alojado en la Universidad de York](https://www-users.cs.york.ac.uk/~mjf/roach/Datasheets/HCSR04_Manual.pdf). Aparece en las páginas 6 y 16.

Resultado: HTTP 200 con redirección al [destino actual del manual](https://www-users.york.ac.uk/~mjf5/roach/Datasheets/HCSR04_Manual.pdf). Se leyeron funcionamiento, fórmula, especificaciones y notas. El documento describe tiempo de ida y vuelta y divide por dos. Incluye copyright de AccuDIY de 2011 y cifras de catálogo del HC-SR04.

Decisión: usar el destino redirigido y conservar la fuente solo como ejemplo general del principio de medida. Se retiran del montaje las cifras de 2-400 cm, 0,3 cm, 5 V y 15 grados, porque el sensor instalado no está identificado. La autoría se registra como aparece en el documento; York es el alojamiento de la copia.

### O11 Guía GUM en BIPM

Enlace: [DOI institucional de JCGM 100:2008](https://www.bipm.org/doi/10.59161/JCGM100-2008E). Aparece en las páginas 6 y 15.

Resultado: HTTP 200 con redirección dentro de BIPM. La ficha identifica la guía y enlaza el texto completo. Se revisaron el PDF y los apartados 3.2 y 4.2, ver A08 y A13.

Decisión: conservar la guía, enlazando el PDF completo. Se distingue error de incertidumbre y se aclara que promediar no elimina el sesgo. La reducción de la incertidumbre del promedio exige condiciones apropiadas, incluidas observaciones independientes.

### O12 Control de servomotores

Enlace: [Servomotor Control with MicroPython and PWM](https://www.luisllamas.es/en/micropython-servomotors-pwm/). Aparece en las páginas 6 y 16.

Resultado: HTTP 200. Se leyeron los apartados sobre pulsos, servos analógicos, PWM y conexión. El artículo utiliza ejemplos SG90 y otros modelos.

Decisión: retirar de la bibliografía final. El papel de un servo específico no está confirmado para la tarea del grupo y la fuente no identifica el montaje. No se mantiene el bloqueo 403 del diagnóstico anterior: en esta consulta abrió.

### O13 Caracterización de mediciones NIST

Enlace: [ficha de Croarkin sobre el capítulo 2](https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-2-measurement-process). Aparece en las páginas 6 y 15.

Resultado: HTTP 200. Se comprobó C. Croarkin, publicación de 2003 y resumen relativo a repetibilidad, reproducibilidad, estabilidad, calibración e incertidumbre.

Decisión: conservar como fuente consultada de contexto. Es una ficha, no el capítulo completo. Las fórmulas y condiciones concretas del informe se respaldan con la GUM y las secciones de contenido completo de NIST añadidas; no se afirma haber leído todo el capítulo a partir de esta ficha.

### O14 Texto completo de Albarello y Hafner Táboas

Enlace: [PDF completo en Redalyc](https://www.redalyc.org/journal/5706/570661491004/570661491004.pdf). Aparece como hipervínculo dentro del marco teórico original.

Resultado: HTTP 200. Se leyeron la introducción, los apartados sobre el uso educativo de programación y robótica y la discusión. Coinciden título, autores, DOI y paginación editorial.

Decisión: conservar como enlace de lectura completa. Respalda el contexto de políticas educativas y la distinción entre contenidos propios y herramientas para otros aprendizajes. No se usa para acreditar mejoras de rendimiento del grupo.

### O15 L298 de STMicroelectronics

Enlace: [ficha oficial L298](https://www.st.com/en/motor-drivers/l298.html). Aparece en las páginas 6 y 16.

Resultado: HTTP 200. Se comprobaron la descripción como puente completo doble y los límites de catálogo de 46 V y 4 A totales.

Decisión: retirar del informe y de la bibliografía final, ya que no está identificado como el driver del robot. Una ficha válida de otro componente no permite atribuirle características al montaje.

## Fuentes alternativas y complementarias comprobadas

| ID | Recurso | Acceso y lectura | Uso |
| --- | --- | --- | --- |
| A02 | [Variante singular motor-driver/l298](https://www.st.com/en/motor-driver/l298.html) | HTTP 404. Variante exploratoria errónea; no es el destino del hipervínculo original. | Descartada. La ruta plural correcta figura en O15. |
| A03 | [Ficha editorial de Albarello](https://revistas.ulima.edu.pe/index.php/contratexto/article/view/4607) | HTTP 200. Metadatos, resumen, DOI y enlaces a formatos completos. | Contraste bibliográfico con O14. |
| A04 | [PDF completo de Zapata](https://arxiv.org/pdf/2506.06314) | HTTP 200. Se abrió el PDF de seis páginas y se leyeron procedimiento, calibración, resultados y limitaciones. | Fuente conservada. |
| A05 | [Ficha extensa de Hunter en la revista](https://ewuurj.scholasticahq.com/article/87939-analysis-of-the-measurement-error-from-a-low-cost-ultrasonic-sensor) | HTTP 403. No permitió lectura directa. | Reemplazada por A17. |
| A06 | [MicroPython para ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html) | HTTP 200. Puerto ESP32, GPIO, PWM y advertencia sobre la rama latest. | Reemplaza RP2. No se trasladan pines de ejemplo al robot. |
| A07 | [Documentación oficial QD001](https://acebott.com/docs/qd001-smart-car-starter-kit-for-esp32/) | HTTP 200. Descripción del producto, ESP32, Mecanum y modos anunciados. | Referencia general del kit, sin certificar hardware o funciones de la unidad. |
| A08 | [GUM completa en BIPM](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf) | HTTP 200. Apartados 3.2, 3.3 y 4.2.1-4.2.7. | Error, incertidumbre, promedio y correlación temporal. |
| A09 | [NIST Confidence Limits for the Mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) | HTTP 200. Definición, fórmula con t y explicación de cobertura. | Intervalo de la media y su interpretación. |
| A10 | [NIST Binomial Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm) | HTTP 200. Función de probabilidad, dos resultados y p fija. | Modelo binomial y estimación de p. |
| A11 | [NIST Linear Least Squares Regression](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm) | HTTP 200. Modelo, criterio de mínimos cuadrados y limitaciones. | Regresión, residuos y cautela frente a extrapolación y atípicos. |
| A12 | [PDF de Hunter en el editor](https://ewuurj.scholasticahq.com/article/87939-analysis-of-the-measurement-error-from-a-low-cost-ultrasonic-sensor.pdf) | El buscador permitió leer una copia indexada; accesos directos y repetidos devolvieron 403. Disponibilidad inconsistente. | No se adopta como único acceso al texto. |
| A13 | [GUM con identificador persistente del archivo](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf/cb0ef43f-baa5-11cf-3f85-4dcd86f77bd6) | HTTP 200. Mismo documento y apartados que A08. | Alternativa oficial de la guía. |
| A14 | [Visor PDF editorial de Albarello](https://revistas.ulima.edu.pe/index.php/contratexto/article/view/4607/4582) | HTTP 200. Contenedor editorial con acceso al PDF; la lectura completa se hizo mediante O14. | Ruta alternativa de consulta, no prueba independiente de contenido íntegro. |
| A15 | [NIST Control del proceso de medición](https://www.itl.nist.gov/div898/handbook/mpc/section2/mpc21.htm) | HTTP 200. Sesgo, variabilidad y supuestos de control. | Complementaria; no incorporada como referencia separada. |
| A16 | [Copia académica de Hunter en ResearchGate](https://www.researchgate.net/publication/383448334_Analysis_of_the_Measurement_Error_From_a_Low-Cost_Ultrasonic_Sensor) | HTTP 200. Autor, DOI, título, texto y vínculo al PDF. Parte de la extracción HTML presenta caracteres de fuente alterados. | La lectura decisiva se hizo desde el PDF A17, con extracción legible. No se atribuye la carga al autor. |
| A17 | [PDF completo de Hunter en ResearchGate](https://www.researchgate.net/publication/383448334_Analysis_of_the_Measurement_Error_From_a_Low-Cost_Ultrasonic_Sensor/fulltext/66cde986bd201736675be557/Analysis-of-the-Measurement-Error-From-a-Low-Cost-Ultrasonic-Sensor.pdf) | HTTP 200 por el servicio de extracción. Método, tablas y conclusión legibles; metadatos coincidentes con la revista. Una descarga directa desde esta computadora recibió 403. | Enlace completo conservado, con esta limitación de acceso registrada. |

Los ID corresponden a los registros de recuperación y por eso no forman una secuencia sin saltos. Un recurso abierto mediante el servicio de extracción puede imponer restricciones a otros clientes. No se garantiza que todos los navegadores o redes obtengan el mismo resultado.

## Contraste de los dos antecedentes

### Zapata

Se verificaron 33 pares de calibración en la tabla 1, r = 0,9985 y MAE de 0,40 cm en la comprobación posterior, sección 3.2, página 3. También se leyeron las limitaciones ambientales y de detección. Se conserva una síntesis del procedimiento y de los resultados reportados; no se copian los datos ni se presentan como propios.

La fórmula introductoria del trabajo no explicita el factor de ida y vuelta y aparecen valores distintos del término independiente entre una ecuación y el código mostrado. Por ese motivo, el informe del grupo no reproduce esa ecuación de calibración ni sus coeficientes. El principio físico se explica con el manual y el ajuste propio deberá estimarse con datos del grupo. El antecedente no se trata como validación universal del sensor.

### Hunter

Se verificaron 30 registros y el promedio de 16 lecturas por registro en el método. La nota de la tabla de error absoluto informa 4,96583 mm, redondeado a 4,97 mm en el informe corregido. Se leyeron también los análisis de incertidumbre, las pruebas estadísticas y la conclusión sobre las limitaciones de referencia, alineación, tamaño muestral y uso de un solo sensor.

El estudio utiliza la convención referencia menos lectura para el error con signo; el informe corregido define lectura menos referencia y la mantiene de manera coherente. El MAE no depende de ese cambio de signo. No se reproducen las interpretaciones generales del artículo como garantías del equipo del grupo.

## Correspondencia entre fuentes y afirmaciones del informe corregido

| Apartado | Afirmación o contenido | Respaldo leído |
| --- | --- | --- |
| 3 y 5.1 | Aprobación de los NAP y contexto educativo | O03 y O14. |
| 5.2 | MicroPython para ESP32 y acceso a hardware | A06 y O04. |
| 5.3 | Tiempo de ida y vuelta, distancia y factor 2 | O10, únicamente como principio y ejemplo general. |
| 5.4 y 5.5 | Error, incertidumbre Tipo A y promedio | A08, apartados 3.2 y 4.2. |
| 5.6 | Fórmula e interpretación del intervalo | A09 y A08. |
| 5.6 | Distribución binomial | A10; independencia y condiciones comparables explicitadas en la metodología. |
| 5.7 | Regresión y limitaciones | A11; cálculo e interpretación no se trasladan de otra unidad. |
| 5.8 | Antecedentes | A04 y A17. |
| 6.1 | Identificación general del producto | A07. |
| 3, 6.1, 6.3 y 7 | Armado y prueba manual por Wi-Fi | Hechos informados por el grupo en los documentos aportados; no proceden del catálogo ni de pruebas ejecutadas por Codex. |

## Contenido que no pudo acreditarse

- Acceso directo sin bloqueos al editor de Hunter mediante O07, O08 y A05. El PDF editorial A12 tuvo disponibilidad inconsistente. El texto sí se verificó mediante A17.
- Identidad exacta del sensor instalado, driver de motores, revisión de placa y Shield, GPIO y alimentación de la unidad. Ninguna fuente genérica se usa para dar estos datos por confirmados.
- Instalación de MicroPython, autonomía, frenado automático y mediciones propias. Permanecen como trabajo previsto.
- Libro o manual que utiliza la cátedra. No se inventó una referencia; se incluye en la lista de información pendiente.

El archivo `Evidencia_enlaces.json` conserva destinos, códigos de respuesta, redirecciones, identificadores de recuperación y huellas de las extracciones. Las extracciones completas y los archivos de trabajo se usaron para la comprobación, pero no se adjuntan como reproducciones de obras ajenas.

## Actualización del Anexo D y recuperación del inventario

Esta sección actualiza las decisiones de alcance de la auditoría anterior. Los ejemplos generales válidos de HC-SR04, L298, RP2/Pico y Python en PC se conservan en D.6; no se consideran componentes físicamente confirmados. Las referencias previas a su retiro describen la versión anterior, no la entrega actual.

Se recuperaron las 34 entradas y cantidades de la Tabla 4 original y se cotejaron una por una con la Product List del Smart Car Manual V2, página PDF 4 (numerada 3). No se encontraron diferencias de cantidad ni de identidad de componente. El cotejo individual consta en Cotejo_inventario.md y Cotejo_inventario.json.

### Fuentes técnicas leídas en esta actualización

| Fuente | Acceso | Contenido pertinente y límite de aplicación |
| --- | --- | --- |
| [D_qd001](https://acebott.com/docs/qd001-smart-car-starter-kit-for-esp32/) | HTTP 200; contenido leído | Presentación oficial del kit y sus capacidades de catálogo; no acredita funciones implementadas por el grupo. |
| [D_tutorials](https://acebott.com/tutorial/) | HTTP 200; contenido leído | Distingue paquetes con Car Shield V1.0 y V2.0; establece la procedencia oficial de las carpetas de descarga. |
| [D_manual-v2-folder](https://www.dropbox.com/scl/fo/nuvcm7jz61pyvkf2e6wqn/AL1zIzwhCVJPD_86wI9yRsY?rlkey=2sw5femcol2t2od43sqxhxaf9&st=oopqhoof&dl=0) | HTTP 200; contenido leído | Carpeta publicada por ACEBOTT Resources. Se consultó English.zip y se extrajo el manual de montaje de 24 páginas. Product List en página PDF 4; baterías aparte en página 2; seguridad en página 3. |
| [D_manual-v1-folder](https://www.dropbox.com/scl/fo/892ydm4qyqw7e10oup40h/AHYlVVPFq4_BCH0yVdJyfzI?rlkey=ez14m5d6335al7pwzup7kit3q&st=kpmvmfwc&dl=0) | HTTP 200; contenido leído | Carpeta identificada como QD001 V1.5, ofrecida por el portal para Shield V1.0. Se consultaron montaje y biblioteca Python servo.py; no se ejecutó ni instaló código. |
| [D_controller](https://acebott.com/docs/qa007-qa008-qa009-esp32-max-v1-0-controller-board/) | HTTP 200; contenido leído | Ficha QA007/QA008/QA009: ESP-WROOM-32, 240 MHz, SRAM 520 KB, flash 4 MB, conectividad y entrada de placa. No se traslada esa entrada a GPIO. |
| [D_shield](https://acebott.com/docs/qa052-esp32-car-shield-v1-0/) | HTTP 200; contenido leído | Wiki titulada V1.0. No sustituye la identificación de V2.0 ni demuestra la revisión de la placa del grupo. |
| [D_shield-shop-v2](https://shop.acebott.com/products/acebott-qa052-esp32-car-shield-v1-0) | HTTP 200; contenido leído | Tienda oficial titulada Car Shield V2.0, aunque su URL conserva v1-0. Lista de interfaces, dimensiones y máximos publicados; no define corriente continua por motor. |
| [D_ultrasonic](https://acebottteam.github.io/acebott-docs-master/tutorials/Sensor/QB042%20Ultrasonic%20Sensor.html) | HTTP 200; contenido leído | Ficha QB042/QB093: 3,3-5 V, 3-500 cm, zona ciega menor de 3 cm y 40 kHz. Detection accuracy 0,1 cm es cifra de catálogo; no constituye incertidumbre medida. La lista del kit no identifica ese código QB. |
| [D_servo](https://acebott.com/docs/qb054-servo-sg90-9g-module-180-degree/) | HTTP 200; contenido leído | Ficha QB054: 3,3-5 V, PWM y recorrido nominal 180 grados. La unidad KG/cm del par es ambigua; se registra y no se adopta como dato de diseño. |
| [D_trace](https://acebottteam.github.io/acebott-docs-master/tutorials/Sensor/QB060%20Trace%20Sensor.html) | HTTP 200; contenido leído | Ficha QB060/QB080: tres canales infrarrojos, salida analógica, alimentación y dimensiones. Los pines de su ejemplo UNO no son el mapa verificado del robot. |
| [D_led](https://acebottteam.github.io/acebott-docs-master/tutorials/Module/QB007%20LED%20Module.html) | HTTP 200; contenido leído | Ficha QB007/QB081: LED azul, 3,3-5 V, control digital o PWM. Pendiente confirmar código y prueba individual de las piezas. |
| [D_buzzer](https://acebottteam.github.io/acebott-docs-master/tutorials/Module/QB010%20P-Buzzer%20Module.html) | HTTP 200; contenido leído | Ficha QB010/QB077: zumbador pasivo y excitación periódica. La etiqueta Output signal de la tabla es imprecisa frente a la descripción de excitación; no se convierte en resultado experimental. |
| [D_ir](https://acebottteam.github.io/acebott-docs-master/tutorials/Module/QB001%2BQB053%20Infrared%20Remote%20Control%20Module.html) | HTTP 200; contenido leído | Ficha de receptor y mando: 38 kHz, señal digital, alimentación, ángulo y alcance declarados. No acredita prueba del mando del grupo. |
| [D_l298](https://www.st.com/resource/en/datasheet/l298.pdf) | HTTP 200; contenido leído | PDF primario completo de STMicroelectronics. Permite conservar el ejemplo general de doble puente H, hasta 46 V y 4 A totales bajo condiciones de ficha. No identifica el driver del Shield. |
| [D_rp2](https://docs.micropython.org/en/latest/rp2/quickref.html) | HTTP 200; contenido leído | Documentación oficial de MicroPython: duty_u16 de 0 a 65535 en RP2. Se conserva como ejemplo de otra plataforma; no se asignan pines RP2 al ESP32. |
| [D_pyfirmata](https://github.com/tino/pyFirmata) | HTTP 200; contenido leído | Documentación del propio proyecto para Python en PC mediante Firmata. Modalidad conceptual, sin adopción ni instalación en este trabajo. |
| [D_upgrades](https://acebott.com/stem-blogs/qd001-smart-car-starter-kit-v2-0-upgrades/) | HTTP 200; contenido leído | Artículo oficial de diferencias V1/V2; confirma la coexistencia de variantes y cambios documentales. No se usa para afirmar la revisión ni funciones de la unidad del grupo. |

### Accesos y datos que no se presentan como verificados

- La lista de piezas de la web se ofrece como imagen. El acceso de la herramienta web a esa imagen no permitió consultarla con fiabilidad y el navegador local estaba deshabilitado. La verificación completa se realizó con la Product List del manual oficial V2, no con OCR supuesto de esa imagen.
- Las consultas iniciales por CLI tuvieron problemas de argumentos y una tanda fue limitada temporalmente por frecuencia. Se corrigió la invocación y se recuperaron las fuentes con HTTP 200; esos intentos no se cuentan como lecturas.
- No se verificaron físicamente la serigrafía, el chip de potencia, las conexiones, la capacidad/protección de las celdas ni las especificaciones individuales de los motores TT. Se conserva lo declarado en el inventario y se separa esa falta de identificación física.
- La ficha QA052 V1.0 y la ficha comercial V2.0 no se intercambian silenciosamente.
- La nueva fuente del L298 es el PDF oficial, que reemplaza las rutas HTML inaccesibles o ambiguas del borrador.
- Los enlaces de la bibliografía general conservan la comprobación documentada de la corrección anterior. Esta actualización agrega fuentes técnicas y verifica su incorporación en el Word y el PDF.

Las extracciones, sus huellas y la procedencia del manual se registran en Evidencia_fuentes_tecnicas.json.
