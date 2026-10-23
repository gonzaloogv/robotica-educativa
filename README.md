# Robótica educativa

Proyecto académico de Probabilidad y Estadística de segundo año de la Tecnicatura Superior en Desarrollo de Software del Instituto Educativo Económico Nacional (IEN), UEGP N.° 167.

En este repositorio se realizará la programación en Python del robot ACEBOTT QD001, junto con las herramientas necesarias para registrar sus mediciones y analizar estadísticamente su desempeño. El código, los datos de los ensayos y el informe deberán describir el mismo funcionamiento del prototipo.

## Objetivo

Programar el robot para que se desplace de manera autónoma y se detenga ante un obstáculo detectado por su sensor ultrasónico. Se evaluarán la precisión de las mediciones y la confiabilidad del frenado con datos del grupo. El umbral de detención y los criterios de éxito deben definirse antes de los ensayos.

El trabajo integra:

- Lectura de sensores y control de los actuadores utilizados en la tarea.
- Explicación del algoritmo: lectura, decisión, actuación y registro de datos.
- Recolección de mediciones y resultados de cada ensayo.
- Análisis de repetibilidad, error de medición, calibración y frecuencia de éxito.
- Documentación del armado, las conexiones, los resultados y las conclusiones.

## Estado actual

El proyecto cuenta con un [borrador actualizado del informe en PDF](output/informe-borrador-corregido/Informe_Robotica_Educativa_borrador.pdf), su [fuente editable en Word](output/informe-borrador-corregido/Informe_Robotica_Educativa_borrador.docx), los dos documentos de referencia del instituto y la documentación técnica del robot.

Según el [contexto técnico aportado por el grupo](CONTEXTO_PARA_CODEX_ACEBOTT_QD001.md):

- El robot está armado y tiene instalado el sensor ultrasónico.
- Respondió correctamente a órdenes de movimiento desde la aplicación oficial ACEBOTT por Wi-Fi.
- Todavía no se probaron el movimiento autónomo ni la captura de mediciones.
- Se desea utilizar MicroPython en el ESP32, sujeto a comprobar el hardware y definir cómo conservar o recuperar el funcionamiento del firmware original.

Estos avances fueron informados por el grupo. Todavía no hay código propio del robot, scripts de captura o análisis, mediciones reales ni herramientas de ejecución configuradas en el repositorio. El borrador incorpora la experiencia de armado, las dificultades y su resolución, la prueba manual, el inventario del kit V2.0 y las ocho fotografías. Los resultados experimentales, las conclusiones finales y la presentación para la defensa siguen pendientes.

La [revisión inicial del informe](docs/revision-informe.md) conserva el diagnóstico de partida. Los [cambios aplicados](output/informe-borrador-corregido/Cambios_aplicados.md) y el [registro de verificación](output/informe-borrador-corregido/Verificacion_entrega.json) corresponden al borrador actualizado. Las carpetas restantes de `output/` conservan las versiones anteriores y sus fuentes.

## Documentos de trabajo

| Documento | Uso |
| --- | --- |
| [Pautas de organización](<ROBOTICA - PAUTAS DE ORGANIZACIÓN 2026.pdf>) | Requisitos del informe escrito, la presentación visual y la defensa oral. |
| [Rúbrica de evaluación](<Rúbrica Proyecto IEN 2026.pdf>) | Criterios y ponderaciones de la defensa del proyecto. |
| [Informe actualizado en PDF](output/informe-borrador-corregido/Informe_Robotica_Educativa_borrador.pdf) | Borrador vigente con documentación técnica, fotografías y metodología; resultados y conclusión experimental pendientes. |
| [Fuente editable del informe](output/informe-borrador-corregido/Informe_Robotica_Educativa_borrador.docx) | Word correspondiente al PDF actualizado. |
| [Informe inicial de Robótica Educativa](<Informe Robótica Educativa.pdf>) | Documento de partida, conservado para consulta. |
| [Contexto técnico del QD001](CONTEXTO_PARA_CODEX_ACEBOTT_QD001.md) | Avances informados por el grupo, preferencia por MicroPython, fuentes técnicas y condiciones para el diagnóstico y la programación. |
| [Plan de correcciones del informe](CAMBIOS_INFORME_ROBOTICA_2026.md) | Cambios propuestos por sección, textos de apoyo y auditoría de bibliografía aportada. También disponible en [PDF](PLAN_DE_CAMBIOS_INFORME_ROBOTICA.pdf). |

## Robot y entorno de programación

El informe identifica el kit ACEBOTT QD001 con estos componentes principales:

- Placa ESP32 Max V1.0 y placa de expansión ESP32 Car Shield V2.0.
- Cuatro motores de corriente continua con reductora y ruedas Mecanum.
- Sensor ultrasónico y servomotor SG90.
- Sensor de seguimiento de línea, receptor infrarrojo, módulos LED y buzzer.
- Portabaterías para celdas 18650.

La lista debe contrastarse con el kit recibido. El modelo exacto del sensor ultrasónico, la etapa de potencia, los pines y la alimentación siguen pendientes de confirmación.

El fabricante [declara compatibilidad con Python](https://acebott.com/es/stem-kits/explorer-series/acebott-omni-wheel-car-robot-starter-kit-collection/), y su [documentación del QD001](https://acebott.com/docs/qd001-smart-car-starter-kit-for-esp32/) describe el kit y sus funciones. La opción prevista por el grupo es MicroPython ejecutándose en el ESP32. Falta validar la variante de placa, el firmware compatible y las bibliotecas necesarias; la [documentación oficial para ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html) deberá corresponder a la versión que se instale.

Las instrucciones de instalación, carga y ejecución se incorporarán cuando el entorno esté definido y comprobado con el robot.

## Conservación del firmware y control del equipo

El firmware actual permite el control con la app oficial. Conservar o recuperar esa capacidad es un criterio de la elección técnica. El contexto del grupo pide investigar primero la viabilidad y preservar el firmware antes de cualquier reemplazo; la preferencia por MicroPython todavía está sujeta a esa evaluación.

La etapa actual comprende revisión documental y preparación del diagnóstico. La conexión al dispositivo y las lecturas de diagnóstico o respaldo se coordinarán con el usuario, ya que pueden reiniciar el equipo. El cambio de firmware y las pruebas de movimiento requieren autorización explícita.

El respaldo deberá guardarse fuera del repositorio, con tamaño y huella SHA-256 registrados y una segunda copia privada. También se deberá documentar cómo se recuperaría el funcionamiento original: disponer de un volcado no demuestra por sí solo que pueda restaurarse. Los binarios y las credenciales Wi-Fi se mantendrán fuera de Git.

## Programación prevista

El desarrollo comprenderá el control del robot y el tratamiento de los datos del experimento:

1. Leer el sensor y reconocer mediciones inválidas o ausentes.
2. Controlar el avance y ordenar la detención ante un obstáculo próximo o una lectura inválida o expirada, con un mecanismo de parada manual.
3. Registrar las lecturas, las decisiones y los resultados necesarios para cada ensayo.
4. Guardar los datos en la computadora; el borrador propone una salida por USB y archivos CSV.
5. Calcular los indicadores estadísticos y generar las tablas y los gráficos del informe.

Los pines, las unidades, los umbrales y los parámetros de movimiento se documentarán según el montaje y las pruebas realizadas. Los pines o las especificaciones de módulos genéricos no se atribuirán al robot sin comprobar su correspondencia con la unidad y el Shield. Las dependencias se elegirán cuando exista una necesidad concreta.

## Ensayos propuestos en el informe

| Ensayo | Datos a obtener | Análisis previsto |
| --- | --- | --- |
| Repetibilidad del sensor | Lecturas repetidas a distancias de referencia fijas. | Media, mediana, desvío estándar, histograma e intervalo de confianza. |
| Calibración del sensor | Distancia de referencia y distancia medida en distintos puntos. | Regresión lineal, correlación, sesgo y error absoluto medio. |
| Frenado ante un obstáculo | Resultado de cada corrida y distancia final al obstáculo. | Frecuencia de éxito y aplicación justificada de la distribución binomial. |
| Velocidad según PWM | Tiempo de recorrido para distintos ciclos de trabajo. | Dispersión entre corridas y evaluación de la relación entre PWM y velocidad. |

Son ensayos previstos. Antes de medir se deben fijar las condiciones, las repeticiones por condición, las unidades y los criterios de éxito o fracaso. El plan de correcciones aportado prioriza repetibilidad, calibración y frenado; el ensayo de velocidad según PWM queda como opcional.

Los datos crudos se conservarán. Las lecturas descartadas deberán quedar identificadas con su motivo. Si se utilizan datos simulados para verificar cálculos o programas, se identificarán como simulados y se mantendrán separados de las mediciones del robot.

## Verificación y entrega académica

La programación deberá comprobarse tanto mediante verificaciones del software como con ensayos del prototipo. Las pruebas de cálculos o archivos CSV no demuestran por sí solas el funcionamiento físico del robot.

El informe deberá incluir el código explicado, las conexiones reales, el procedimiento realizado, los datos, su análisis y conclusiones que respondan a los objetivos. La defensa requiere una presentación de apoyo y una demostración del prototipo, con participación de todos los integrantes.

Todavía no hay comandos de typecheck, lint, tests o build configurados. Cuando se incorpore código se documentarán las verificaciones que correspondan al entorno elegido y las comprobaciones que requieran el equipo físico.
