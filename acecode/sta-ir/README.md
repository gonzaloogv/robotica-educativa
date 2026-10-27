# Proyecto completo con la conexión solicitada: STA + IR

Abrir **[QD001_V2_STA_IR_Completo.sb3](../versiones-ap-y-sta/QD001_V2_STA_IR_Completo.sb3)** en ACECode. Esta es la variante para
conectar el auto a una red Wi-Fi existente de 2,4 GHz. El programa no crea
`ESP32-CAR`: cierra AP, inicia STA, espera conexión y muestra la IP por serie
a 115200 baudios. Después inicia el servidor y los controles.

## Configurar antes de la carga

1. Usar Guardar como y nombrar la copia `QD001_V2_STA_IR.local.sb3`.
2. En el bloque de conexión, reemplazar `CONFIGURAR_WIFI_2_4_GHZ` y
   `CONFIGURAR_CLAVE_WIFI` por el nombre y la clave de la red elegida.
   La copia local queda excluida de Git. No publicar sus credenciales.
3. El celular y el robot deben tener acceso entre sí en esa red. Evitar
   aislamiento entre clientes y redes de invitados.

Con los marcadores sin completar, o si la conexión falla, el programa espera
antes de iniciar el servidor de la app. Durante esa espera ACECode genera
llamadas a `repeat()`, donde se procesa el mando IR; la espera no bloquea esa
lógica. No incluye un punto de acceso alternativo ni cambia a AP ante una
falla de conexión.

## Funciones conservadas

Se mantienen los siete modos de la app, el mando infrarrojo, las diagonales,
las luces, las cuatro melodías, el servomotor y los algoritmos de ultrasónico
y seguimiento de línea de la variante completa. Sus bloques funcionales
quedan idénticos. Solo se sustituye la preparación de red: 541 bloques de
partida y 549 en esta variante. Consultar [los controles y las pruebas físicas
pendientes](../PROYECTO_COMPLETO.md).

Mientras se usa IR, la app queda inhibida. OK detiene. `#` devuelve el control
a la app y exige STOP antes de aceptar otra orden.

## Límite que falta comprobar en la app

El servidor se conserva, pero la app ACEBOTT debe permitir conectarse a la IP
que obtiene el ESP32 en esta red. Esa posibilidad de la interfaz todavía no
se verificó. Si la app solo utiliza el destino fijo del modo AP, será necesario
resolver el acceso por IP antes de dar por validado el control desde el celular.
La compilación y las pruebas de archivos no prueban esa conexión.

## Procedencia

Se deriva de `QD001_V2_AP_IR_Completo.sb3` mediante el adaptador STA existente:

```text
node tools/preparar_sta.js acecode/QD001_V2_AP_IR_Completo.sb3 DESTINO_NUEVO/QD001_V2_STA_IR_Completo.sb3
```

El [manifiesto](../versiones-ap-y-sta/manifest-sta.json) registra las huellas y la conservación de todos los bloques
ajenos a la red. La variante AP + IR se conserva como alternativa separada.
El nuevo proyecto no se instaló ni se probó físicamente en el auto.

Verificación del 23/10/2026: 17 pruebas automatizadas aprobadas y compilación
Arduino de referencia correcta con ESP32 3.2.0 y las bibliotecas de ACECode
2.2.4. Programa: 988.826 bytes (75 %); variables globales: 52.184 bytes (15 %).
Se conservan [la fuente Arduino comprobada](codigo_generado/QD001CompletoSTA/QD001CompletoSTA.ino)
y [el registro de verificación](Verificacion_STA_IR.json).

Para la importación en ACECode 2.2.4 se conservan todos los comentarios plegados.
Esto evita el error de posicionamiento de comentarios que interrumpía la
construcción del espacio de bloques. Se mantienen los siete bloques de modo
originales del fabricante. La espera de conexión compara el estado Wi-Fi
documentado (`INFO`) con 1 mediante un operador booleano compatible con el editor.

Se abrió `QD001_V2_STA_IR_Completo.sb3` en ACECode y se revisó la generación
automática: módulos incluidos, rutina STA y final del programa (535 líneas).
La comprobación de compilación corresponde a la referencia generada mediante
el adaptador con los mismos generadores oficiales; no fue una carga desde la GUI.
