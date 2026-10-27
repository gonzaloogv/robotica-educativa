# Robótica educativa

> **Continuidad al 27/10/2026:** MicroPython 1.29.0 y el programa USB `0.1.1-usb` están instalados por pedido del usuario. Luces, melodía y ultrasónico respondieron; los motores no giraron de forma visible y siguen en diagnóstico. Se omitió el respaldo del firmware estable inmediatamente anterior por indicación explícita del usuario; la imagen cifrada anterior sigue conservada. Leer primero [el contexto completo y los próximos pasos](docs/estado_sesion_2026-10-27.md).

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

## Informe y contexto de partida

El proyecto cuenta con un [borrador actualizado del informe en PDF](output/informe-borrador-corregido/Informe_Robotica_Educativa_borrador.pdf), su [fuente editable en Word](output/informe-borrador-corregido/Informe_Robotica_Educativa_borrador.docx), los dos documentos de referencia del instituto y la documentación técnica del robot.

Según el [contexto técnico aportado por el grupo](CONTEXTO_PARA_CODEX_ACEBOTT_QD001.md):

- El robot está armado y tiene instalado el sensor ultrasónico.
- Respondió a órdenes de movimiento desde la aplicación ACEBOTT antes de reemplazar el firmware; ese resultado no acredita movimiento con el programa Python actual.
- Todavía no se probaron el movimiento autónomo ni la captura de mediciones.
- MicroPython está instalado; se cargó un programa USB con arranque detenido y comandos manuales. La adaptación de motores todavía no funciona físicamente.

El contexto del grupo se complementó con la instalación y pruebas del 27/10. Ahora hay código propio en la [rama técnica](https://github.com/gonzaloogv/robotica-educativa/tree/trabajo/micropython-respaldo), una consola USB y catorce pruebas locales. Se obtuvieron lecturas reales del ultrasónico, sin calibración contra patrón ni campaña experimental. No hay autonomía, captura CSV o análisis estadístico completados. El borrador incorpora armado, dificultades y resolución, prueba manual previa, inventario V2.0 y ocho fotografías; todavía debe actualizarse con este nuevo estado. Los resultados experimentales, conclusiones finales y presentación para la defensa siguen pendientes.

La [revisión inicial del informe](docs/revision-informe.md) conserva el diagnóstico de partida. Los [cambios aplicados](output/informe-borrador-corregido/Cambios_aplicados.md) y el [registro de verificación](output/informe-borrador-corregido/Verificacion_entrega.json) corresponden al borrador actualizado. Las carpetas restantes de `output/` conservan las versiones anteriores y sus fuentes.

## Documentos de trabajo

| Documento | Uso |
| --- | --- |
| [Contexto completo del 27/10/2026](docs/estado_sesion_2026-10-27.md) | Estado vigente, instalación, comandos Python, resultados reales y diagnóstico pendiente de motores. |
| [Instalación de MicroPython](docs/instalacion_micropython_2026-10-27.md) | Escritura verificada, firmware usado y alcance del respaldo anterior. |
| [Estado de continuidad del 23/10/2026](docs/estado_sesion_2026-10-23.md) | Comprobaciones, firmware estable informado y comparación pendiente. |
| [MicroPython sin robot](docs/continuidad_micropython_sin_robot.md) | Lógica y pruebas en PC; integración física pendiente. |
| [Variante completa ACECode en STA](docs/acecode_sta.md) | Proyecto de red local preparado en una rama separada, sin instalarlo en el robot. |
| [Preparación de MicroPython](PREPARACION_MICROPYTHON.md) | Descarga realizada, integridad local y límites. |
| [Diagnóstico de hardware](docs/diagnostico_hardware.md) | Chip, flash, controlador USB y alcance de las lecturas. |
| [Respaldo y recuperación](docs/procedimiento_respaldo_y_restauracion.md) | Diferencia entre imagen anterior y estado estable; verificación y límites. |
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

El usuario confirmó la serigrafía V2.0 del Shield. El mapa del programa se obtuvo de ACECode; ultrasónico, luces y buzzer respondieron. Siguen pendientes el modelo exacto del sensor, los niveles eléctricos y la verificación del circuito, alimentación y recepción de órdenes de motores.

El fabricante [declara compatibilidad con Python](https://acebott.com/es/stem-kits/explorer-series/acebott-omni-wheel-car-robot-starter-kit-collection/), y su [documentación del QD001](https://acebott.com/docs/qd001-smart-car-starter-kit-for-esp32/) describe el kit y sus funciones. Se identificaron ESP32-D0WD-V3 revisión 3.1 y 4 MB de flash. MicroPython ESP32_GENERIC 1.29.0 está instalado y se verificó su intérprete por USB. La referencia usada es la [documentación de ESP32 para 1.29](https://docs.micropython.org/en/v1.29.0/esp32/quickref.html). La aceptación de órdenes por software no demuestra giro de las ruedas.

Las instrucciones de consola, carga y pruebas están en el [contexto vigente](docs/estado_sesion_2026-10-27.md) y en la guía del programa de la rama técnica.

## Conservación del firmware y control del equipo

El grupo informó una prueba previa con la app y, al finalizar la sesión del 23/10, funcionamiento correcto con un firmware estable después de una restauración. El 27/10 el usuario autorizó reemplazarlo por MicroPython y pidió omitir el respaldo del estado actual después de un intento de lectura fallido. El programa ACEBOTT quedó reemplazado; la aplicación del fabricante y el proyecto STA anterior no forman parte del Python activo.

La etapa actual es diagnóstico de motores con programa Python cargado. Las pruebas realizadas terminaron detenidas y se indicó al usuario que podía desconectar y apagar el equipo. El estado físico después de esa indicación no se verificó. Confirmar conexión, alimentación y ruedas levantadas antes de nuevas pruebas; esta publicación no accede al robot.

El respaldo ANTERIOR tiene dos lecturas completas de 4 MB con SHA-256 idéntico y verificación contra flash correcta. Se conserva en privado, con copias en dos discos locales. No acredita ser imagen de fábrica ni una copia del firmware estable posterior. No hay respaldo validado del estado inmediatamente anterior a instalar MicroPython y la restauración funcional no se ensayó. Ver [procedimiento y límites](docs/procedimiento_respaldo_y_restauracion.md) y [registro de instalación](docs/instalacion_micropython_2026-10-27.md). Esta publicación documental no contiene volcados, claves ni credenciales.

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

La rama técnica incluye catorce pruebas locales ejecutables con `python -m unittest discover -s tests -v`. Se verificaron también archivos y arranque en el ESP32. Esas comprobaciones no acreditan movimiento físico; los motores siguen pendientes. Los comandos y evidencias están documentados en el contexto vigente.
