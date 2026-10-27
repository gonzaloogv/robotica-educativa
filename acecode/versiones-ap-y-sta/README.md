# QD001 V2.0: versiones AP + IR y STA + IR

Entrega local del 24/10/2026. Abrir uno de los dos proyectos en ACECode 2.2.4,
con placa ESP32, modo de carga y generación Arduino. Cada archivo es un
proyecto editable `.sb3`; el firmware se obtiene al compilarlo para la placa.

| Proyecto | Red utilizada | Acción desde el celular |
| --- | --- | --- |
| [QD001_V2_AP_IR_Completo.sb3](QD001_V2_AP_IR_Completo.sb3) | Crea `ESP32-CAR`, con la clave pública del ejemplo `12345678`. | Conectarse a esa red y usar la aplicación ACEBOTT. |
| [QD001_V2_STA_IR_Completo.sb3](QD001_V2_STA_IR_Completo.sb3) | Conecta a una red Wi-Fi existente de 2,4 GHz. | Conectar el celular a la misma red y comprobar el acceso de la app a la IP del robot. |

Se carga una versión a la vez. Para pasar de STA a AP hay que cargar el otro
proyecto; no se agregó un cambio automático entre ambos modos de conexión.

## Configuración STA

Guardar una copia llamada `QD001_V2_STA_IR.local.sb3`. En el bloque de conexión,
reemplazar `CONFIGURAR_WIFI_2_4_GHZ` por el nombre exacto de la red y
`CONFIGURAR_CLAVE_WIFI` por su contraseña. Las copias `*.local.sb3` están
excluidas de Git. El archivo entregado contiene solamente marcadores.

El programa muestra la IP obtenida en el monitor serie a 115200 baudios y
espera conexión antes de iniciar el servidor de la app. Mientras espera, la
lógica del mando IR se sigue procesando. Falta comprobar que la aplicación
ACEBOTT admita la IP obtenida en STA.

## Funciones y mando

Ambas versiones conservan los siete modos del ejemplo V2: movimiento manual,
luces, melodías, seguimiento de objeto, evasión y dos modos de seguimiento de
línea. Incluyen la integración del mando IR y las cuatro diagonales de la app.
Los parámetros de sensores y velocidades son valores iniciales del ejemplo;
la calibración real está pendiente.

| Tecla IR | Acción programada |
| --- | --- |
| Flechas arriba / abajo | Avanzar / retroceder. |
| Flechas izquierda / derecha | Girar en sentido antihorario / horario. |
| 1 / 3 | Desplazamiento lateral izquierdo / derecho. |
| 4 / 6 | Diagonal delantera izquierda / derecha. |
| 7 / 9 | Diagonal trasera izquierda / derecha. |
| OK | Detener y mantener seleccionado IR. |
| # | Detener y volver al control de la app; después pulsar STOP en la app. |

El mando tiene prioridad mientras está seleccionado. El programa ordena parar
tras 100 ms sin una nueva orden de movimiento IR. Las esperas de algunas
maniobras y melodías pueden demorar la atención a nuevas órdenes. No hay un
mecanismo de propietario exclusivo para un celular.

## Verificación y primera prueba física

[Verificacion_AP_STA.json](Verificacion_AP_STA.json) registra las comprobaciones
de esta entrega, las huellas de los dos archivos y su correspondencia con las
versiones cuya compilación de referencia se registró el 23/10/2026. La entrega
se regeneró con los mismos generadores, sin cambiar las bibliotecas ni los
parámetros funcionales.

Los dos archivos son versiones candidatas para pruebas: todavía no se cargaron
ni se comprobaron en el robot. Antes de cargar una, identificar y respaldar el
firmware estable actual. La primera prueba debe hacerse con las ruedas libres,
comprobando arranque, movimientos y parada antes de ensayar los modos.

La revisión posterior identificó [mejoras pendientes](Mejoras_pendientes.md)
que afectan a ambas variantes. No están implementadas en los archivos publicados.

Las instrucciones detalladas se conservan en la [guía AP + IR](../PROYECTO_COMPLETO.md)
y la [guía STA + IR](../sta-ir/README.md).
