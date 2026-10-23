# Respaldo y recuperación del ACEBOTT QD001

## Estado y alcance

Respaldo capturado y verificado el 23/10/2026. Firmware actual conservado: no se borró ni escribió flash, no se programaron eFuses ni se enviaron órdenes de movimiento. El usuario quiere probar el firmware actual antes de cualquier reemplazo. La herramienta reinició la placa al terminar; el funcionamiento desde la app todavía debe comprobarse con el grupo.

Rama técnica: trabajo/micropython-respaldo, creada desde origin/develop y sin seguimiento de esa rama remota. origin/documentacion no fue modificada.

## Qué contiene

Dos lecturas completas de la flash externa, desde 0x000000 hasta 0x3FFFFF inclusive: 4.194.304 bytes por imagen. Incluyen bootloader, tabla de particiones, aplicaciones y datos persistentes presentes. No contienen el código fuente ni respaldan eFuses.

Chip: ESP32-D0WD-V3, revisión 3.1. Herramienta: esptool 5.6.0. Captura final: 115200 baudios con stub oficial temporal en RAM. No se grabó ese lector en flash. Durante las capturas la aplicación permaneció detenida en modo de descarga.

Archivos para recuperar: original-validado-1.bin y original-validado-2.bin (mismo contenido).
SHA-256 de ambos:

```text
F8D6975734345B72EBD68E9CF845996CDCA328BA350991A6995C671CD9E99C15
```

## Comprobaciones realizadas

- Ambas lecturas terminaron correctamente y midieron exactamente 4.194.304 bytes.
- Sus SHA-256 coinciden.
- verify-flash comparó toda la imagen contra la flash del ESP32: Verification successful (digest matched).
- La primera imagen tiene encabezado de bootloader ESP32 0xE9 en 0x1000, tabla de particiones AA50 en 0x8000 y encabezado de aplicación 0xE9 en 0x10000. Esto no equivale a probar cada función de la aplicación.
- Los dos binarios de cada ubicación se comprobaron otra vez con tools/Verificar-Respaldo.ps1 y están marcados como solo lectura.

## Ubicaciones privadas, fuera de Git

Principal: C:\Users\Alumnos\AppData\Local\ACEBOTT-Backups\QD001-20261023-091536
Segunda copia: D:\ACEBOTT-Backups\Alumnos\QD001-20261023-091536

Según Windows, C: corresponde al disco 1 y D: al disco 0. Son dos discos locales de la misma PC; no son una copia externa ni protección frente a pérdida de toda la computadora. Las carpetas tienen herencia de permisos desactivada y acceso concedido al usuario actual y SYSTEM. Los permisos NTFS no equivalen a cifrado y no impiden acceso de un administrador que tome posesión. Los binarios pueden contener credenciales Wi-Fi: no publicarlos.

Cada carpeta contiene manifest.json, las dos imágenes, logs y un verificador de integridad. Antes de modificar firmware conviene conservar además una copia privada en un medio externo y cotejar el SHA-256. Los binarios originales sin cifrar siguen fuera de Git. A pedido posterior del usuario se incorporó al repositorio una copia cifrada en backups/acebott-qd001, con la clave fuera de Git en las dos carpetas privadas. El .gitignore excluye binarios sin cifrar, claves y descargas.

Para revisar integridad sin abrir COM6 ni conectarse al robot:

```powershell
.\tools\Verificar-Respaldo.ps1 -Directorio 'C:\Users\Alumnos\AppData\Local\ACEBOTT-Backups\QD001-20261023-091536'
.\tools\Verificar-Respaldo.ps1 -Directorio 'D:\ACEBOTT-Backups\Alumnos\QD001-20261023-091536'
```

## Protecciones y límites

Lectura de eFuses: ABS_DONE_0 y ABS_DONE_1 = False (Secure Boot V1/V2 desactivados); FLASH_CRYPT_CNT = 0 (cifrado de flash desactivado); UART_DOWNLOAD_DIS = False. DISABLE_DL_ENCRYPT, DISABLE_DL_DECRYPT y DISABLE_DL_CACHE = False. No se modificaron esos valores. get-security-info no fue soportado en el modo ROM; se usó espefuse summary de solo lectura para estos campos.

Una lectura ROM inicial se interrumpió por lentitud y una captura a 460800 fue rechazada por datos corruptos. No se consideran respaldos válidos. La primera verificación que intentó reutilizar la conexión del stub se interrumpió por una advertencia de sincronización; con conexión limpia se completó correctamente a 115200, indicando cristal de 40 MHz. Los logs se conservan para trazabilidad.

Las coincidencias verificadas demuestran integridad y correspondencia con la flash en el momento del respaldo. La restauración funcional NO fue ensayada: hacerlo implicaría escribir el firmware, contra la indicación actual. No se garantiza seguridad absoluta. Tampoco se presupone que esta imagen sirva para otra placa, ni que puedan recuperarse futuras modificaciones de eFuses.

## Recuperación propuesta, no ejecutada

1. Confirmar que se trata de la misma placa, detectar el puerto y comprobar alimentación y protecciones sin modificar eFuses.
2. Ejecutar el verificador y cotejar el SHA-256 con este registro y una copia independiente. Usar original-validado-1.bin íntegro, no el firmware ESP32_GENERIC de MicroPython.
3. Obtener autorización explícita de escritura; preparar el robot con ruedas libres antes de reiniciar.
4. Restaurar la imagen completa original desde 0x0 con una versión compatible de esptool. Revisar los encabezados y los parámetros antes de ejecutar; conservar los parámetros de la imagen, sin opciones force ni cambios manuales de particionado, voltaje o eFuses. La operación de escritura sí es destructiva y NO se ejecutó en esta etapa.
5. Verificar la flash contra el archivo restaurado antes de arrancar. Después comprobar arranque, app Wi-Fi y comportamiento del robot con el grupo.

No se incluye un comando ejecutable de escritura en esta etapa para evitar activación accidental. La prueba del firmware actual es el próximo hito y todavía no se realizó.

Fuente técnica: https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html
