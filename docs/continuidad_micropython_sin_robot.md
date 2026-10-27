# Continuar MicroPython desde casa, sin el robot

> **Estado posterior, 27/10/2026:** MicroPython y el programa USB ya estan instalados por pedido del usuario; luces, musica y ultrasonico respondieron, pero no hubo giro visible de motores. Leer primero [el contexto vigente](estado_sesion_2026-10-27.md). Esta guia conserva el contexto de la etapa anterior.

## Alcance

Se puede desarrollar la lógica de decisión, los formatos de datos y el análisis en Python de PC. Eso no demuestra que funcionen el sensor, la dirección de los motores o el frenado del robot.

El usuario informó un firmware estable y pidió conservar el equipo sin modificaciones. MicroPython está solamente descargado; todavía no hay un programa MicroPython del robot terminado o validado.

## Separar lógica y hardware

| Capa | Trabajo sin robot | Comprobación física pendiente |
| --- | --- | --- |
| Controlador | Estados de espera, avance y parada; reglas ante obstáculos y errores. | Respuesta real y tiempo de frenado. |
| Sensor | Lecturas simuladas, timeout y datos inválidos o vencidos. | Modelo, conexiones, niveles de señal y calibración. |
| Motores | Interfaz de órdenes y sustituto que registre llamadas. | Protocolo del Shield, direcciones, velocidad útil y parada efectiva. |
| Registro | CSV con unidades, ensayo, eventos y observaciones. | Captura real por USB y tiempos del dispositivo. |
| Estadística | Cálculos con datos de prueba identificados como simulados. | Mediciones genuinas del grupo. |

La lógica debe importarse en PC sin depender de `machine` ni activar hardware. La adaptación MicroPython queda en módulos separados. El estado inicial debe ser detenido y requerir habilitación explícita antes de ordenar movimiento.

Una estructura propuesta, todavía no implementada, es:

```text
firmware_micropython/
  main.py             # inicio detenido y coordinación
  controller.py       # lógica pura comprobable en PC
  config.py           # parámetros explícitos, sin GPIO inventados
  sensors.py          # adaptación al sensor real
  motors.py           # adaptación al Shield real
  safety.py           # parada y condiciones de ejecución
pc/
  capture_serial.py   # captura futura de mediciones reales
analysis/
  analyze_trials.py
tests/
  test_controller.py
```

## Pruebas útiles en PC

- No emitir avance al iniciar ni antes de habilitar el ensayo.
- Detener ante un obstáculo dentro del umbral definido para ese ensayo.
- Detener ante lectura ausente, inválida, expirada, timeout o excepción.
- Priorizar la parada manual y exigir rearme cuando corresponda.
- Comprobar unidades, orden de eventos y conservación de lecturas descartadas con su motivo.
- Identificar los datos simulados; no presentarlos como resultados experimentales.

Los umbrales, intervalos y límites de movimiento se deben validar. Un test con sustitutos no demuestra seguridad física.

## Particularidad del Shield V2

La biblioteca Arduino `ACB_CAR_ARM` revisada en ACECode inicializa V2 mediante serie por software, RX=16, TX=17 y 9600 baudios, y envía velocidad cero a los cuatro motores al iniciar. Esto describe la fuente instalada: NO verifica eléctricamente esta unidad.

No trasladar al V2 un ejemplo genérico de GPIO/PWM del Shield V1. Antes de escribir el adaptador MicroPython hay que confirmar versión física, protocolo y conexiones. También siguen pendientes el modelo exacto del ultrasónico y el acondicionamiento de ECHO.

## Repositorio y entorno

Consultar la rama `documentacion` y desarrollar código en una rama técnica separada, siguiendo el uso de `develop`. Crear un entorno Python de PC para probar la lógica. Un paquete de PC llamado micropython no instala el firmware de la placa.

Esta guía no incluye código del robot o tests ya configurados. Deberán crearse en la rama de programación. No guardar credenciales o volcados privados en commits. Las copias privadas de la sesión siguen en su computadora de origen; clonar esta rama no las transporta.

## Antes de reconectar y ejecutar

Primero hay que obtener un respaldo del firmware ESTABLE actual: su lectura y comparación se postergaron. Confirmar recuperación, chip/flash y conexiones; después decidir la instalación de MicroPython con autorización explícita. Validar sensor y parada, luego motores con ruedas libres y finalmente ensayos controlados.

**Conectar el robot después de desarrollar desde casa no garantiza que funcione:** la instalación e integración con hardware siguen pendientes.

Fuentes: [MicroPython ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html), [ESP32_GENERIC](https://micropython.org/download/ESP32_GENERIC/) y [tutoriales ACEBOTT](https://acebott.com/tutorial/).
