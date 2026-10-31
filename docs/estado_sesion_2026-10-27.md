# Contexto y continuidad del QD001 — 27/10/2026

**Cierre del 27/10 confirmado por el grupo el 30/10/2026:** el robot quedó funcionando y continuó en uso hasta que se agotaron las baterías. El estado intermedio de motores sin giro que se describe más abajo no representa el cierre de esa jornada. No se registraron duración de uso, tensión de las baterías ni resultados de ensayos estadísticos.

**Decisión académica vigente:** con autorización de la docente, el grupo utilizará el programa de fábrica de ACEBOTT y explicará su funcionamiento. No se utilizará Python ni MicroPython como implementación del trabajo. La versión exacta del programa de fábrica y la secuencia de recuperación posterior a las pruebas intermedias quedan por documentar; esta confirmación no permite atribuir el funcionamiento final a un archivo o firmware concreto.

Las notas de instalación, comandos y diagnóstico que siguen se conservan como antecedentes de las pruebas intermedias del 27/10. No son instrucciones de la implementación elegida para el informe.

## Estado intermedio registrado durante las pruebas

| Elemento | Situación comprobada o informada |
| --- | --- |
| Robot | ACEBOTT QD001, cuatro motores y ruedas Mecanum |
| Controlador identificado por USB | ESP32-D0WD-V3 rev. 3.1, cristal de 40 MHz, flash de 4 MB |
| Placa de motores | El usuario leyó V2.0 en la placa; falta contrastar el circuito y la interfaz física |
| USB en esta PC | CH340, COM6, 115200 baudios para MicroPython; el puerto puede cambiar |
| Firmware de la prueba intermedia | MicroPython 1.29.0, ESP32_GENERIC, instalado el 27/10 |
| Programa de la prueba intermedia | Versión `0.1.1-usb`: `main.py`, `qd001.py`, `safety.py` |
| Inicio | Detenido, desarmado, luces y buzzer apagados |
| Ultrasónico | Lecturas válidas con una superficie de referencia; sin ella hubo mediciones inválidas |
| Luces y música | El usuario confirmó encendido/apagado y reproducción de la melodía |
| Motores | Órdenes aceptadas por el programa y pulso de diagnóstico enviado, sin giro observado por el usuario |
| Autonomía, Wi-Fi, IR, servo y línea | No implementados en este programa Python |
| Datos estadísticos | No hay campaña experimental, calibración ni medición de frenado completadas |

El último acceso del diagnóstico intermedio terminó con órdenes de parada y reinicio del programa detenido. El usuario consultó si podía desconectar USB y se le indicó que sí, y que apagara el interruptor si iba a manipularlo. **No se verificó después si efectivamente quedó desconectado o apagado**: confirmar su estado físico antes de retomar hardware. Esta publicación de contexto no accede a COM6.

## Antecedentes de autorización e instalación durante las pruebas

La indicación inicial de conservar el firmware ACEBOTT fue reemplazada por el pedido explícito de instalar MicroPython. Antes de escribir se intentó obtener una copia actual, pero la lectura completa falló por comunicación USB. El usuario indicó después: «hacelo sin respaldar lo actual».

Tras reconectar USB, se borró la flash y se escribió MicroPython desde `0x1000` usando esptool 5.6.0 a 115200 baudios. La herramienta confirmó `Hash of data verified`. La comprobación por REPL devolvió versión 1.29.0, plataforma `esp32` e intérprete `micropython`. Inicialmente el sistema de archivos contenía `boot.py`.

El programa ACEBOTT quedó reemplazado. La aplicación del fabricante y la variante ACECode STA preparada antes no forman parte del programa MicroPython probado en esa etapa. No se debe prometer que la app o el control remoto funcionen con este programa.

El respaldo cifrado del 23/10 sigue conservado y no fue modificado. Es anterior a la restauración estable que hizo el usuario: **no hay imagen validada del estado estable inmediatamente anterior a instalar MicroPython**. No se ensayó una restauración en hardware. La autorización de omitir esa captura fue específica de esta instalación; no implica omitir respaldos futuros ni autoriza una restauración nueva.

Detalles de instalación y huella del firmware: [registro de instalación](instalacion_micropython_2026-10-27.md). Conservación y límites de la imagen anterior: [procedimiento de respaldo](procedimiento_respaldo_y_restauracion.md).

## Archivos y ramas

La rama `documentacion` conserva las guías y el contexto. El programa y las herramientas están en [trabajo/micropython-respaldo](https://github.com/gonzaloogv/robotica-educativa/tree/trabajo/micropython-respaldo):

| Archivo de la rama técnica | Función |
| --- | --- |
| `firmware_micropython/main.py` | Bucle de comandos USB y coordinación del robot |
| `firmware_micropython/qd001.py` | Adaptador de motores UART, ultrasónico, luces y buzzer |
| `firmware_micropython/safety.py` | Habilitación, validación de mediciones y límite de movimiento |
| `firmware_micropython/README.md` | Uso, conexiones, verificaciones y limitaciones |
| `pc/control_qd001.py` | Consola interactiva por USB desde la computadora |
| `tools/cargar_programa_qd001.py` | Carga de archivos, compilación en el ESP32 y comparación SHA-256 |
| `tests/test_qd001_safety.py` | Pruebas locales de interbloqueos y tramas, sin hardware |

La variante completa de ACECode en STA permanece en [trabajo/acecode-sta](https://github.com/gonzaloogv/robotica-educativa/tree/trabajo/acecode-sta). Se preparó antes del reemplazo y no se cargó en esta sesión. Estos proyectos se conservan como antecedentes y no sustituyen la decisión de utilizar y explicar el programa de fábrica.

Los scripts de un solo uso, logs y archivos de diagnóstico quedan en `downloads/`, excluido de Git. Los volcados privados, claves, credenciales y binarios sin cifrar no se incorporan a esta publicación.

## Uso del programa Python de la prueba intermedia

Desde la raíz de la rama técnica, con el USB conectado y ACECode y otros monitores serie cerrados:

```powershell
.\.venv\Scripts\python.exe .\pc\control_qd001.py --port COM6
```

En una computadora nueva primero se debe crear su entorno e instalar `pyserial`. El entorno `.venv` de esta PC no se publica. El programa del ESP32 ya queda guardado; abrir la consola no requiere reinstalar MicroPython ni volver a cargar archivos.

Si el usuario abrió directamente el `python.exe` del entorno y ve `>>>`, puede iniciar el cliente así, ajustando la ruta en otra PC:

```python
import sys, runpy
sys.argv = ["control_qd001.py", "--port", "COM6"]
runpy.run_path(r"C:\Users\Alumnos\Documents\robotica-educativa\pc\control_qd001.py", run_name="__main__")
```

Cuando aparece `QD001>`, las órdenes se escriben sin comillas:

| Orden | Comportamiento |
| --- | --- |
| `estado` / `distancia` | Distancia, validez, armado, movimiento y motivo de bloqueo |
| `luces on` / `luces off` | Cambia las luces y desarma motores |
| `musica` | Desarma motores y reproduce cuatro notas |
| `armar` | Habilita órdenes por 15 s si hay una lectura reciente y mayor a 25 cm; no mueve por sí solo |
| `adelante`, `atras`, `izquierda`, `derecha`, `girar_izquierda`, `girar_derecha` | Ordena un pulso de movimiento si está armado y el sensor sigue válido |
| `parar` | Ordena detener y desarma |
| `salir` | El cliente ordena parar y libera el puerto USB |

Cada movimiento tiene un límite nominal de 250 ms y velocidad de entrada fija 80/255. Al terminar el pulso se ordena parar y se desarma; para otro pulso hay que volver a escribir `armar`. Las luces y la música también desarman. Una respuesta `movimiento=adelante` acredita aceptación de la orden, **no giro de ruedas ni desplazamiento**.

La parada depende del software y la transmisión; no hay tiempo de frenado físico calibrado ni watchdog independiente del Shield confirmado. Se requiere sensor válido para todas las direcciones, incluido retroceso. No se considera libre el espacio por falta de eco.

## Ultrasónico: diagnóstico de `null`

Al cargar la primera versión se registraron tres lecturas de 40,1 cm. Después el usuario informó `distancia=null`. La versión 0.1.0 usaba un mensaje que mezclaba sensor inválido y obstáculo cercano; se corrigió en la 0.1.1.

En la revisión directa, veinte mediciones terminaron con `time_pulse_us=-1`: ECHO estaba bajo antes del disparo y alto al vencer 25 ms. Es un timeout de la duración del pulso; no una distancia corta confirmada. Con la superficie plana que colocó el usuario a aproximadamente 40–60 cm, doce lecturas dieron entre 52,0 y 52,1 cm. Se probó un límite de 25 ms y otro de 45 ms durante el diagnóstico; el límite normal del programa se mantuvo en 25 ms.

Tras cargar 0.1.1 se obtuvieron 51,2 cm y lectura válida. `armar` devolvió `armado=true`, `estado` indicó `moviendo=false`, y `parar` dejó ambos estados en falso. Estos valores son lecturas reales del sensor, **no una calibración**: no se registró una distancia patrón medida con instrumento.

La versión 0.1.1 distingue medición ausente, vencida, fuera de rango, obstáculo medido, motores desarmados y fin del pulso. La falta de distancia válida conserva el bloqueo. Una superficie a unos 50 cm sirve como referencia para la prueba de banco con ruedas levantadas.

## Motores: diagnóstico intermedio y confirmación posterior

El usuario ejecutó `armar` y `adelante`. La respuesta fue velocidad 80, duración 250 ms y después `parada_automatica`, motivo `Pulso terminado; volver a armar para otro movimiento`. El usuario indicó que las ruedas no giraron. Esto descarta que ese mensaje particular corresponda a un bloqueo ultrasónico, pero no demuestra recepción por la etapa de motores.

Se confirmó con el usuario batería conectada y preparación para una prueba breve con las ruedas levantadas y consola cerrada. Se envió un único pulso al motor 1, velocidad de entrada 150, límite nominal de 250 ms y comprobación ultrasónica activa. La distancia inicial fue 51,9 cm. El tiempo hasta completar la orden de parada fue 272 ms, incluyendo el bucle y la transmisión. El usuario tampoco observó giro. Esta prueba puntual **no se agregó al arranque ni cambió la velocidad normal 80**.

La batería conectada no acredita tensión o capacidad de corriente bajo carga. No se midieron alimentación del Shield, tensión en motores, continuidad o señales físicas. Durante ese diagnóstico no se identificó una causa definitiva. El grupo confirmó después el funcionamiento del robot hasta agotar las baterías; no quedó documentada la causa del síntoma intermedio ni la secuencia que permitió recuperar el funcionamiento.

El adaptador que se probó reproduce la biblioteca oficial local `ACB_CAR_ARM.cpp`, funciones `Vehicle_init_V2` y `motorControl`, y su selección se contrastó con el generador `carMotorV2` de ACECode:

- UART2 de MicroPython, TX GPIO17 y RX GPIO16, 9600 baudios, 8N1.
- Trama de cinco bytes: `[motor, sentido, potencia, 13, 10]`.
- Motores 3 y 4 con inversión de sentido respecto de 1 y 2.
- Potencia no nula: mapeo entero de entrada 0–255 a 40–100; cero enviado como cero.

El resto del mapa usado es TRIG GPIO13, ECHO GPIO14, luces GPIO2/12 y buzzer GPIO33. Luces, buzzer y ultrasónico respondieron; eso **no valida** el camino de control de motores. No hubo confirmación de recepción del Shield ni se probaron mapas alternativos de GPIO. No atribuir aún el fallo a potencia baja, protocolo o avería.

## Verificaciones y evidencia local

Las catorce pruebas locales aprobaron estado inicial, bloqueo por lecturas inválidas o viejas, obstáculo, vencimiento del pulso, rearme, rollover del reloj, dirección y escala de las tramas y mensajes diferenciados. No sustituyen ensayos físicos.

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Los tres archivos del ESP32 se compilaron en la placa y se cotejaron por SHA-256. Huellas de la versión 0.1.1 cargada:

| Archivo | SHA-256 |
| --- | --- |
| `qd001.py` | `9559b5a261f406a699be2732175f9319cef6f87f89cf4e6057b9995723af96ab` |
| `safety.py` | `f20e56cd9a5b490485c2c19d2d23f87c093100a32203f69d312bdbcd187d936c` |
| `main.py` | `e25d4f8d1da0c99d8c14d30001677394bbba89f5fce59f987f801df285815547` |

Registros locales, excluidos de Git: `downloads/instalacion-micropython-20261027.json`, `downloads/programa-qd001-20261027.json`, `downloads/diagnostico-ultrasonico-20261027.json`, `downloads/diagnostico-ultrasonico-con-objeto-20261027.json`, `downloads/verificacion-armado-sin-movimiento-20261027.json` y `downloads/prueba-motor1-20261027.json`. Sus observaciones relevantes están resumidas aquí para que la continuidad no dependa de esos archivos locales.

## Continuidad con el programa de fábrica

1. Identificar el archivo, fuente y versión del programa de fábrica que se utilizará y preparar su explicación para el informe.
2. Confirmar el estado de carga de las baterías y el funcionamiento del robot antes de iniciar nuevas pruebas.
3. Documentar por separado cada función efectivamente comprobada, sin extender la confirmación general de funcionamiento a todos los modos automáticos.
4. Ejecutar los ensayos de repetibilidad, calibración y frenado con un protocolo definido y datos propios. El funcionamiento hasta agotar las baterías es una observación cualitativa, no una medición de autonomía ni una calibración.

## Recomendaciones del diagnóstico intermedio conservadas como antecedente

1. Confirmar estado físico, batería e interruptor, liberar el puerto y mantener las ruedas levantadas antes de retomar pruebas.
2. Contrastar la placa V2.0 real con documentación o esquema exactos y revisar alimentación efectiva de los motores. No probar pines alternativos por semejanza con otro kit.
3. Comprobar la señal de control y recepción del Shield; si hace falta cambiar el adaptador, justificarlo con esa evidencia.
4. Probar un motor a la vez con pulso acotado y parada, y después verificar sentidos de los cuatro. No aumentar duración o potencia indefinidamente sin diagnóstico.
5. Solo después validar desplazamiento y parada en piso; luego desarrollar autonomía, registro CSV y ensayos estadísticos con datos genuinos.
6. Mantener desarrollo en rama técnica y documentación en `documentacion`. No publicar datos privados ni volver a usar el respaldo anterior como si fuese la imagen del estado estable posterior.

## Fuentes

- [QD001 oficial](https://acebott.com/docs/qd001-smart-car-starter-kit-for-esp32/) y [tutoriales ACEBOTT con variantes V1/V2](https://acebott.com/tutorial/).
- Paquete oficial local de ACECode: `extraFiles/compile/sketch/ACB_CAR_ARM/ACB_CAR_ARM.cpp` y ejemplo `QD001~QD010(V2)/QD001/4.4.2APPControlCar2(Final program).sb3`. El generador Arduino selecciona `Car_init(2)` para `carMotorV2`.
- [MicroPython 1.29 ESP32](https://docs.micropython.org/en/v1.29.0/esp32/quickref.html), [UART](https://docs.micropython.org/en/v1.29.0/library/machine.UART.html) y [time_pulse_us](https://docs.micropython.org/en/v1.29.0/library/machine.html#machine.time_pulse_us).
