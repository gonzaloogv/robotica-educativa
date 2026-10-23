# Información experimental pendiente

Esta lista reúne los datos que faltan para completar el informe y ejecutar el experimento. No impide utilizar la versión documental corregida. La programación y las intervenciones sobre el robot corresponden a una etapa separada, posterior al diagnóstico y respaldo.

## Identificación del montaje

- Fotografías legibles de la placa y el Shield, con modelo y revisión.
- Modelo exacto del sensor ultrasónico y ficha técnica correspondiente.
- Identificación de motores, driver o etapa de potencia y conexiones efectivamente utilizadas.
- Mapa de pines comprobado con fuente de la revisión correcta del equipo.
- Tipo, capacidad y tensión nominal de las celdas; esquema y condiciones de alimentación para los ensayos. Las fotos muestran un portabaterías para dos celdas cilíndricas.
- Identificación y función de los módulos adicionales visibles, y confirmación de cuáles se utilizarán en la tarea.

## Evidencia del armado y del control manual

- Ya incorporadas: ocho fotografías propias del armado y del robot ensamblado, numeradas en los anexos C y D.
- Fechas individuales de toma y autoría individual, solo si se desean consignar y el grupo dispone de esos datos. No se deducen de los nombres de archivo.
- Pasos realmente seguidos e incidentes o dificultades, únicamente si ocurrieron.
- Registro disponible de la prueba con la app oficial por Wi-Fi: acciones observadas y condiciones. El armado del 16/10 al 20/10/2026 y la respuesta manual ya están incorporados como hechos informados.

## Entorno y programa que se implementará después

- Resultado del diagnóstico de chip, memoria y firmware existente.
- Respaldo privado verificado y procedimiento de recuperación evaluado, antes de considerar un reemplazo.
- Decisión final sobre MicroPython y compatibilidad con el montaje.
- Versión del firmware, código ejecutado y versión del código.
- Pines verificados, PWM, intervalo de lectura, tiempo máximo de espera y regla para detectar una lectura expirada.
- Umbral de detención, respuesta a fallos y mecanismo de parada manual realmente probados.
- Evidencia de avance y detención autónoma. La prueba manual de la app no reemplaza esta comprobación.

## Protocolo previo a la toma de datos

| Dato por definir | Criterio para dejarlo registrado |
| --- | --- |
| Referencia de distancia | Instrumento, resolución, unidades y punto físico desde el cual se mide. |
| Repetibilidad | Tres distancias elegidas, cantidad fija de lecturas por distancia y separación temporal. La meta de 30 por distancia sigue como propuesta. |
| Calibración | Entre ocho y diez posiciones dentro del rango confirmado; repeticiones por posición y datos adicionales para comprobar cualquier corrección. |
| Frenado | Posición inicial, obstáculo, configuración de movimiento, umbral, banda aceptable de distancia final y número de corridas por condición. |
| Éxito o fracaso | Regla cerrada antes de medir; criterios para contacto, distancia fuera de banda, fallo de lectura y parada manual. |
| Condiciones | Superficie, orientación del sensor, objeto, temperatura ambiente y estado de alimentación. |
| Datos inválidos | Códigos y motivos; reglas previas de clasificación y análisis, conservando cada intento. |
| Modelos estadísticos | Justificación de independencia, estabilidad de condiciones y uso de t o binomial. Si no son adecuados, explicitar la limitación. |

## Mediciones y materiales que deberán incorporarse

- CSV originales con identificadores de ensayo y condición, tiempo, lecturas, validez y observaciones.
- Distancias de referencia y finales medidas externamente, con instrumento y método.
- Registro de cada corrida de frenado: resultado, contacto, causa de detención e intervención manual si la hubo.
- Recuento de intentos, lecturas válidas y fallos, sin exclusiones silenciosas ni reemplazo de ausencias por cero.
- Tablas de media, mediana, desvío, sesgo, MAE e intervalos cuando correspondan.
- Gráficos de repetibilidad, calibración y errores o residuos con unidades, número de observaciones y fuente.
- Archivos de cálculo o programas de análisis que permitan reproducir las tablas y gráficos.
- Fotografías del procedimiento y diagrama real de conexiones.
- Conclusión experimental ligada a cada objetivo, a los números obtenidos y a las limitaciones observadas.
- Libro o manual de Probabilidad y Estadística utilizado por la cátedra, si se lo citará.

El ensayo de velocidad según PWM es opcional. Si se realiza, requerirá un protocolo propio de recorrido, distancia, cronometraje, niveles de PWM y repeticiones; si no se realiza, no se informarán resultados sobre esa relación.
