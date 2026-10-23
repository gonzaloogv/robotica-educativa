# Respaldos y recuperación del ACEBOTT QD001

## Dos estados diferentes

| Estado | Evidencia |
| --- | --- |
| Anterior, al comenzar la sesión | Respaldo completo capturado y verificado el 23/10/2026. |
| Estable posterior | Funcionamiento correcto informado por el usuario tras restaurar o cargar desde ACECode. Sin nuevo volcado o hash; comparación pospuesta. |

El respaldo anterior no acredita ser firmware de fábrica ni representa automáticamente el estado estable actual. Restaurarlo recuperaría su programa y configuración, incluidos los comportamientos de ese momento.

## Verificación del respaldo anterior

Dos lecturas independientes desde 0x00000000 hasta 0x003FFFFF inclusive produjeron 4.194.304 bytes por archivo. Coinciden en SHA-256:

`F8D6975734345B72EBD68E9CF845996CDCA328BA350991A6995C671CD9E99C15`

La comparación contra la flash confirmó coincidencia del digest. Se comprobaron también checksum y SHA-256 internos de la aplicación identificada. Las capturas válidas se hicieron a 115200 baudios con esptool 5.6.0 y un lector temporal en RAM, sin grabarlo en flash.

Una captura ROM se interrumpió por lentitud y otra a 460800 fue rechazada por datos corruptos. No cuentan como respaldos válidos. Los registros se conservaron en privado.

## Copias privadas

```text
C:/Users/Alumnos/AppData/Local/ACEBOTT-Backups/QD001-20261023-091536/
D:/ACEBOTT-Backups/Alumnos/QD001-20261023-091536/
```

Cada carpeta conserva las dos lecturas, manifiesto y registros. C: y D: corresponden a discos distintos según Windows, en la misma computadora. Se restringieron permisos al usuario y SYSTEM y se marcaron binarios como solo lectura. Los permisos NTFS no equivalen a cifrado ni impiden que un administrador tome posesión.

Las imágenes completas pueden contener configuración y credenciales. Los originales sin cifrar y las claves no se publican. La rama `trabajo/micropython-respaldo` contiene una copia cifrada Fernet y herramientas de verificación/extracción, que no se incluyen en esta rama documental. `clave-respaldo-repo.key` se conserva fuera de Git en las carpetas privadas y es necesaria para descifrar. Comprobar la disponibilidad de esa rama al clonar; no confundir la publicación de documentos con la entrega de una clave privada.

Para continuar en otra PC, guardar además una copia privada externa con su manifiesto y, si se transporta la imagen cifrada, su clave. Clonar esta documentación no transporta los respaldos ni permite restaurar por sí solo la placa.

## Respaldo del firmware estable: pendiente

El usuario solicitó compararlo y luego decidió hacerlo en otra ocasión, con el robot desconectado. No se ejecutó una nueva lectura. En la próxima sesión:

1. Registrar el proyecto o binario estable instalado y las funciones probadas.
2. Coordinar una lectura que puede reiniciar la placa, con COM libre y ruedas levantadas.
3. Guardar un NUEVO volcado completo en otra carpeta privada, sin sobrescribir los anteriores.
4. Verificar tamaño, repetir lectura cuando sea posible, cotejar hashes y comparar contra flash.
5. Guardar segunda copia privada en otro medio y registrar herramienta, fecha y procedencia.
6. Comparar por separado aplicación, particiones y configuración: un hash global distinto no determina dónde cambió el contenido.

## Límites y recuperación futura

La integridad de las imágenes anteriores está verificada; la restauración funcional NO fue ensayada. Un hash coincidente no prueba por sí solo el arranque y todas las funciones después de restaurar. El volcado externo tampoco respalda ni revierte eFuses.

Una recuperación futura requiere confirmar identidad del equipo, protecciones, alimentación, imagen y dirección de carga; obtener autorización explícita de escritura; grabar sin forzar protecciones; verificar contra flash y comprobar físicamente el arranque y las funciones esperadas. No se incluyen comandos de escritura ejecutables en esta etapa.

No se garantiza recuperación absoluta. Actualmente se conserva el firmware estable y rige la instrucción de no modificar el robot.

Fuente: [comandos oficiales de esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html).
