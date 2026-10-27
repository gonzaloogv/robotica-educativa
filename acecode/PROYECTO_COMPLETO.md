# QD001 V2.0: app por Wi-Fi y mando infrarrojo

**Esta guía describe la alternativa AP + IR.** Para la conexión solicitada a
una red existente usar [QD001_V2_STA_IR_Completo.sb3](versiones-ap-y-sta/QD001_V2_STA_IR_Completo.sb3)
y [la guía STA + IR](sta-ir/README.md). En esa variante no se crea `ESP32-CAR`.

Abrir **QD001_V2_AP_IR_Completo.sb3** en ACECode. Es un proyecto de bloques para
ESP32, en modo de carga y con generación Arduino. No usa MicroPython.
El archivo se preparó en la computadora y todavía no se instaló en el auto.

## Red del auto

El programa inicia el punto de acceso **ESP32-CAR**, con la clave pública del
ejemplo oficial **12345678**, e inicia el servidor para la app de ACEBOTT.
El celular se conecta a esa red; no hace falta configurar el Wi-Fi del instituto.
Que el celular indique que esa red no tiene Internet es compatible con este
uso local. La biblioteca del fabricante usa TCP 100 y un servidor HTTP.

La variante `QD001_V2_STA_Completo.sb3` es diferente: se conecta a un router y
no anuncia una red propia. Se conserva como alternativa separada, con sus
marcadores de credenciales y sus límites de compatibilidad con la app.

## Funciones incluidas

| Función | Preparación del programa |
| --- | --- |
| Movimiento manual | Avance, retroceso, desplazamientos laterales, giros, diagonales y parada. |
| Velocidad | Se conserva la lectura de velocidad enviada por la app. |
| Luces | Encendido y apagado de los dos LED del ejemplo. |
| Sonido | Se conservan las cuatro melodías del buzzer. |
| Evasión | Se conserva el algoritmo oficial con ultrasónico y barrido del servomotor. |
| Seguimiento de objeto | Se conserva el modo oficial con sensor ultrasónico. |
| Línea circular y en ocho | Se conservan los dos modos y la configuración de sensores oficial. |
| Mando infrarrojo | Se integra la lectura del receptor y el control manual, con parada por falta de renovación de la orden. |

Esta tabla describe instrucciones incluidas. El funcionamiento de cada modo,
la calibración de sensores, las velocidades, los recorridos y la conexión del
celular se comprobarán con el prototipo. No constituye un resultado experimental.

## Uso del mando

Al arrancar queda seleccionado el control de la app. Pulsar una tecla de
movimiento del mando selecciona el control IR. Mientras está seleccionado IR,
las órdenes de la app no se ejecutan.

| Tecla del mando | Acción programada |
| --- | --- |
| Flecha arriba / abajo | Avanzar / retroceder. |
| Flecha izquierda / derecha | Girar en sentido antihorario / horario. |
| 1 / 3 | Desplazarse hacia la izquierda / derecha. |
| 4 / 6 | Diagonal delantera izquierda / derecha. |
| 7 / 9 | Diagonal trasera izquierda / derecha. |
| OK | Detener y mantener seleccionado el mando. |
| # | Detener y devolver el control a la app. Luego pulsar STOP en la app. |

Se conserva la velocidad IR de 255 y el tiempo de 100 ms del ejemplo oficial
`4.2.1IRremoteCar.sb3`. Sin una nueva orden de movimiento durante ese tiempo se
ordena parar. Es un tiempo nominal de software, no una distancia ni un tiempo
de frenado medido. Las melodías y algunas maniobras originales tienen esperas;
la respuesta al cambio de control deberá comprobarse también durante esos modos.

Después de `#`, se espera la orden STOP de la app antes de aceptar otra orden.
Esto evita retomar una instrucción que hubiera quedado seleccionada antes de
usar el mando. En modo IR, usar OK para detener.

## Procedencia y cambios

La base es `4.4.2APPControlCar2(Final program).sb3`, extraído del instalador
ACECode 2.2.4 aportado por el grupo. Su SHA-256 coincide con la fuente registrada
en la rama `trabajo/acecode-sta`:
`54a97fa9bc9de649e9b9f14a2b68b889f1acee1ddcef781499f1e0642499d1b4`.

Se conservan copias sin modificar de los ejemplos de app e IR en `fuentes/`.
El programa ampliado conserva los 434 bloques oficiales, sus recursos y
parámetros. Agrega 107 bloques. Cinco bloques originales cambian únicamente
enlaces para insertar la ampliación. La configuración AP original se mantiene.
Los comentarios se conservan plegados para evitar un error de posicionamiento
que puede interrumpir la importación en ACECode 2.2.4.

La integración usa los bloques V2, sus menús y las bibliotecas de ACECode 2.2.4.
No traslada el control de motores V1 a la Shield V2. La biblioteca V2 utiliza
comunicación serie por RX16/TX17 a 9600 baudios. Los pines de los sensores se
mantienen como en los ejemplos: IR4, servo25, ultrasónico13/14,
línea39/36/35, LED2/12 y buzzer33. Su correspondencia con el cableado del auto
debe comprobarse antes de la prueba física.

Las cuatro diagonales se agregaron al modo manual porque la biblioteca y los
menús V2 las reconocen, pero el ejemplo final no contenía sus casos. La biblioteca
asigna las órdenes 74, 71, 72 y 73 a esas direcciones, respectivamente.

Para reproducir el archivo en un destino nuevo:

```text
python tools/preparar_completo.py acecode/fuentes/QD001_V2_APP_Oficial.sb3 DESTINO.sb3
```

El generador conserva los recursos y produce un manifiesto con huellas y cambios.
No abre puertos, no carga firmware y no ejecuta motores.

## Estado de verificación

Las pruebas automatizadas comprueban la red AP, los modos, la integridad de
referencias, la conservación del contenido oficial y la selección entre app e IR.
La simulación de selección registra órdenes en memoria; no simula la física ni
demuestra la recepción real del mando. El registro de entrega distingue estas
comprobaciones de la compilación y de los ensayos físicos.

Se generó una referencia Arduino con los generadores de ACECode 2.2.4 mediante
un adaptador sin interfaz y se compiló con las bibliotecas y el entorno ESP32
3.2.0 del mismo instalador, para `esp32:esp32:esp32`. La compilación terminó
con código 0: 987.854 bytes de programa (75 %) y 52.184 bytes de variables
globales (15 %). Además, la variante STA + IR se abrió en ACECode 2.2.4 y se
comprobó visualmente su generación completa, con los módulos de IR, Wi-Fi,
línea, servo, ultrasónico, LED y buzzer.
Se conservan [el código compilado como fuente](codigo_generado/QD001Completo/QD001Completo.ino)
y [el registro de verificación](Verificacion_proyecto_completo.json).
El editable principal sigue siendo el `.sb3`; no se entrega un binario para
cargar automáticamente.

| Prueba pendiente en el auto | Comprobación concreta |
| --- | --- |
| Red y app | Aparece `ESP32-CAR`; conecta el celular y acepta STOP antes de mover. |
| Motores y ruedas | Sentido de cada motor, traslaciones, giros, diagonales y parada, primero con ruedas libres. |
| Mando | Correspondencia de teclas, recepción, parada al soltar y retorno a la app mediante `#` y STOP. |
| Sensores y servo | Cableado real, orientación del servo y lecturas a distancias conocidas. |
| Línea | Lecturas de los tres sensores y ajuste de umbral a la superficie de prueba. |
| Modos y sonido | Selección y salida de cada modo; respuesta a parada y cambio de control durante maniobras y melodías. |

Los valores 2000/4000 del seguimiento de línea, las velocidades y los tiempos
se conservan del fabricante como parámetros iniciales; no son calibraciones
ni mediciones del grupo. Para los ensayos de estadística se registrarán datos
reales en una etapa posterior.

Antes de cargar: identificar y respaldar el firmware estable actual, comprobar
placa y conexiones y preparar una prueba con las ruedas libres. El respaldo
de la otra rama corresponde al estado anterior a la recuperación informada;
no debe confundirse con una imagen de fábrica o del estado estable actual.

## Aclaración sobre el incidente de Wi-Fi

El grupo informó conexión desde el celular el 20/10 y, en una sesión posterior,
ausencia de la red y un proyecto vacío en ACECode. No se recuerda el orden
de los eventos ni el mensaje del intento de carga desde la computadora del
instituto. Por eso no se atribuye una causa al incidente. Un proyecto vacío
en el editor no permite determinar qué programa estaba almacenado en el ESP32.

El fabricante distingue el modo de ejecución en línea del modo de carga:
tras una carga exitosa, el programa puede funcionar sin la computadora. Abrir
un proyecto y cargarlo en la placa son pasos distintos. En esta entrega solo
se preparan y verifican archivos.

Fuentes del fabricante consultadas:

- [Uso de ACECode y modos de ejecución](https://acebott.com/docs/getting-started-with-acecode/).
- [Distribución oficial de ACECode](https://acebott.com/software/).
- [Tutoriales oficiales del kit](https://acebott.com/tutorial/).
