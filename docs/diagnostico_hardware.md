# Diagnóstico USB del ACEBOTT — 2026-10-23

Inspección de Windows mediante Get-PnpDevice, Get-PnpDeviceProperty y CIM. No se abrió ningún puerto serie ni se ejecutó esptool.

## Observado

- Dispositivo USB presente con descripción USB Serial.
- Hardware ID: USB\VID_1A86&PID_7523&REV_0264.
- Estado: Error. Código de problema: 28 / CM_PROB_FAILED_INSTALL.
- Sin controlador seleccionado: proveedor, versión, INF y servicio sin datos.
- Win32_SerialPort no devolvió puertos COM.

El identificador coincide con el puente USB-serie WCH CH340/CH341 en el catálogo de Microsoft. Es compatible con que sea la interfaz USB del ACEBOTT conectado, pero el identificador del puente no confirma el modelo de robot, chip ESP32 ni capacidad de flash.

El código 28 corresponde a controladores no instalados. El bloqueo actual está en el controlador USB de Windows; estos resultados no prueban un fallo del firmware del robot.

## Pendiente

Instalar el controlador oficial apropiado para WCH CH340/CH341 y comprobar que aparezca un puerto COM. No se instaló nada durante esta inspección. Después habrá que coordinar la identificación del chip y flash: abrir el puerto o usar esptool puede reiniciar la placa aunque no se escriba firmware.

No se comprobó el contenido o versión del firmware, tamaño de flash, estado de protecciones, pines del Shield ni funcionamiento de sensores o motores. No se modificó firmware, cableado ni se enviaron órdenes al robot.

## Fuentes

- https://learn.microsoft.com/en-us/windows-hardware/drivers/install/cm-prob-failed-install
- https://www.catalog.update.microsoft.com/ScopedViewInline.aspx?updateid=6faa33ef-5b78-469c-abac-10f990667c5f

## Actualización tras instalar el controlador — 2026-10-23

Windows ahora reconoce USB-SERIAL CH340 (COM6), clase Ports, estado OK. Controlador wch.cn, versión 4.0.2026.2, INF oem197.inf, firmado según Win32_PnPSignedDriver. El bloqueo por falta de controlador quedó resuelto en la consulta PnP. Win32_SerialPort no devolvió entradas; COM6 se obtuvo del nombre PnP del dispositivo presente.

La comprobación fue solamente mediante consultas a Windows. No se abrió COM6 ni se reinició intencionalmente la placa. Chip ESP32, flash y firmware siguen sin identificar mediante comunicación con el dispositivo.

## Identificación mediante esptool — 2026-10-23

Con autorización del usuario se ejecutó esptool 5.6.0 en COM6 a 115200 baudios, comando --no-stub flash-id. Resultado:

- Chip ESP32-D0WD-V3, revisión v3.1.
- Doble núcleo, 240 MHz, Wi-Fi y Bluetooth.
- Cristal: 40 MHz.
- Flash detectada: 4 MB; fabricante 0x68, dispositivo 0x4016.
- Tensión de flash indicada por strapping: 3,3 V (no es una medición del cableado del Shield).
- La herramienta efectuó reinicio por RTS al finalizar.

Registro: docs/identificacion_esp32.txt, con MAC omitida. No se cargó stub en RAM (--no-stub), no se borró ni escribió flash y no se enviaron órdenes de motores. El firmware original puede volver a ejecutar su comportamiento al reiniciar; no se verificó su funcionamiento desde la app.

El chip y tamaño detectados son coherentes con el candidato ESP32_GENERIC descargado. Esto no valida aún los GPIO, las bibliotecas del Shield ni la recuperación del firmware original. No se leyó un respaldo completo ni se verificaron Secure Boot o Flash Encryption. La versión y contenido del firmware instalado siguen pendientes.

Herramientas locales: entorno .venv, Python 3.10, esptool 5.6.0. Para resolver la cadena de certificados del pip inicial se actualizó pip a 26.2.2 mediante wheel de PyPI descargado con Windows y SHA-256 cotejado con sus metadatos; luego la instalación HTTPS de esptool funcionó sin desactivar la verificación.

## Respaldo final — 2026-10-23

Se completaron dos lecturas coincidentes de 4 MB a 115200 baudios mediante lector temporal en RAM. SHA-256: F8D6975734345B72EBD68E9CF845996CDCA328BA350991A6995C671CD9E99C15. verify-flash confirmó correspondencia de la imagen con la flash completa. Se conservan copias privadas en C: y D:, con manifiestos y verificación local. Procedimiento y límites: docs/procedimiento_respaldo_y_restauracion.md.

No se escribió ni borró flash ni se programaron eFuses. Al finalizar se reinició la placa para arrancar el firmware existente. No se comprobó todavía el funcionamiento desde la app. La restauración no fue ensayada y se mantiene la instrucción del usuario de probar primero el firmware actual. Se trabaja en trabajo/micropython-respaldo; origin/documentacion continúa sin cambios.

## Copia cifrada dentro del repositorio — 2026-10-23

El usuario pidió conservar también el firmware de respaldo en el repositorio. Se agregó backups/acebott-qd001/firmware-original.fernet y su manifiesto, con la clave privada fuera de Git en las carpetas de C: y D:. tools/extraer_respaldo.py permite verificar o extraer el original sin conectarse al dispositivo. El descifrado con ambas copias de la clave reproduce los 4.194.304 bytes y el SHA-256 original. Los binarios originales y claves permanecen excluidos de Git. No se accedió al robot para este trabajo.

En el volcado se encontró el literal ESP32-CAR (en mayúsculas) y una partición NVS con datos. Esto orienta la próxima prueba de Wi-Fi, pero no prueba que la red esté siendo emitida ni diagnostica su ausencia. El usuario indicó que el dispositivo está desconectado.
