# Firmware original del ACEBOTT QD001

Esta carpeta conserva una copia cifrada completa del respaldo obtenido el 23/10/2026. Corresponde al ESP32-D0WD-V3 revisión 3.1 de este proyecto, no a un firmware genérico descargado ni al código fuente del fabricante.

- firmware-original.fernet: imagen completa cifrada, versionada en Git.
- manifest.json: tamaño, SHA-256 de la imagen original y del archivo cifrado, y verificaciones de captura.
- La clave clave-respaldo-repo.key está fuera de Git, en las carpetas privadas indicadas abajo. Nunca copiarla al repositorio.

La imagen original mide 4.194.304 bytes y su SHA-256 es:

```text
F8D6975734345B72EBD68E9CF845996CDCA328BA350991A6995C671CD9E99C15
```

Se conserva el volcado íntegro, incluida la configuración persistente de la placa. El cifrado permite versionarlo sin publicar ese contenido. Se utiliza Fernet de cryptography, con autenticación de integridad. Véase https://cryptography.io/en/latest/fernet/ . El archivo cifrado no se puede grabar directamente en el ESP32: primero debe recuperarse y verificarse el .bin original.

## Clave privada y copias originales

La misma clave se conserva en:

```text
C:\Users\Alumnos\AppData\Local\ACEBOTT-Backups\QD001-20261023-091536\clave-respaldo-repo.key
D:\ACEBOTT-Backups\Alumnos\QD001-20261023-091536\clave-respaldo-repo.key
```

Ambas carpetas mantienen también las dos lecturas originales sin cifrar. Están fuera del repositorio, con permisos restringidos. Un clon de Git por sí solo no permite descifrar el archivo: hace falta la clave, o una de las copias originales. Conservar también una copia privada externa de la clave y del respaldo cubre la pérdida de toda la PC; no hay garantía absoluta de recuperación.

## Comprobar sin extraer ni conectarse al robot

Desde la raíz del proyecto, con el entorno .venv ya preparado:

```powershell
.\.venv\Scripts\python.exe tools/extraer_respaldo.py --clave 'C:\Users\Alumnos\AppData\Local\ACEBOTT-Backups\QD001-20261023-091536\clave-respaldo-repo.key' --verificar
```

La herramienta comprueba tamaño y SHA-256 del archivo cifrado, autenticidad al descifrar y tamaño y SHA-256 de la imagen original. Todo se realiza en memoria y no se abre ningún puerto serie.

Si hay que preparar las herramientas en otra PC, crear un entorno con Python 3.10 e instalar requirements-tools.txt. Las claves y los originales se transfieren por un medio privado, fuera de Git.

## Extraer un archivo nuevo, sin flashear

Elegir una carpeta privada existente y un nombre de salida que todavía no exista:

```powershell
.\.venv\Scripts\python.exe tools/extraer_respaldo.py --clave 'C:\Users\Alumnos\AppData\Local\ACEBOTT-Backups\QD001-20261023-091536\clave-respaldo-repo.key' --salida 'C:\Users\Alumnos\AppData\Local\ACEBOTT-Backups\QD001-20261023-091536\qd001-para-recuperar.bin'
```

No sobrescribe archivos existentes. Extraer no instala ni escribe nada en el robot. La recuperación funcional en hardware NO se ensayó: el usuario pidió conservar y probar primero el firmware actual. El procedimiento de recuperación propuesto está en ../../docs/procedimiento_respaldo_y_restauracion.md.

## Aclaración sobre el estado respaldado

Esta imagen conserva el programa y la configuración que tenía el robot al iniciar la sesión de trabajo. No acredita que sea el firmware de fábrica. El usuario informó que al encender avanza sin detenerse y no muestra Wi-Fi. Restaurar esta copia recuperaría ese estado; no corrige por sí solo ese comportamiento. La investigación está en docs/diagnostico_arranque_wifi.md y queda pendiente revisar el proyecto fuente conservado por el grupo.
