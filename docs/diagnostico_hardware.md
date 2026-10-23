# Diagnóstico de hardware — 23/10/2026

Estado vigente: [resumen de continuidad](estado_sesion_2026-10-23.md). Las lecturas técnicas se hicieron ANTES de la restauración posterior informada por el usuario; no se volvieron a consultar las protecciones o el firmware estable actual.

## USB y herramientas

Windows detectó inicialmente USB Serial, VID 1A86/PID 7523, con error 28 por falta de controlador. Después de instalar el controlador WCH CH340/CH341 apareció USB-SERIAL CH340 (COM6), estado OK. Windows informó wch.cn 4.0.2026.2 firmado. COM6 corresponde a esta PC, no necesariamente a otra.

Se usó Python 3.10 con esptool 5.6.0 para identificar y respaldar la unidad. También se comprobaron ACECode 2.2.4, Arduino CLI y paquete ESP32 3.2.0. El esptool incluido en ACECode informó 4.5.1: se consultó su ayuda sin hacer una nueva captura o grabación con él.

## Identificación consultada

| Campo | Resultado |
| --- | --- |
| Chip | ESP32-D0WD-V3, revisión 3.1. |
| Funciones informadas | Wi-Fi, Bluetooth, doble núcleo y 240 MHz. |
| Cristal | 40 MHz. |
| Flash | 4 MB; fabricante 0x68, dispositivo 0x4016. |
| Strapping de tensión de flash | 3,3 V según esptool; no mide el cableado del Shield. |

No se publican direcciones MAC. Esto no confirma los pines o niveles eléctricos de cada módulo.

## Protecciones leídas

`get-security-info` no fue soportado en el modo ROM usado. Se consultaron indicadores con `espefuse summary`, sin programarlos:

- ABS_DONE_0 y ABS_DONE_1 = False: Secure Boot V1/V2 desactivados.
- FLASH_CRYPT_CNT = 0: cifrado de flash desactivado.
- UART_DOWNLOAD_DIS = False: descarga UART habilitada.
- DISABLE_DL_ENCRYPT, DISABLE_DL_DECRYPT y DISABLE_DL_CACHE = False.

Son observaciones anteriores a la restauración, no una certificación del estado posterior. No se modificaron eFuses.

## Respaldo anterior

Dos lecturas completas de 4.194.304 bytes coincidieron en SHA-256:

`F8D6975734345B72EBD68E9CF845996CDCA328BA350991A6995C671CD9E99C15`

La verificación contra flash fue satisfactoria. Se guardaron copias privadas en dos discos locales, con permisos restringidos y binarios de solo lectura. La restauración funcional no se ensayó. Véase [respaldo y recuperación](procedimiento_respaldo_y_restauracion.md).

## Estado estable posterior y límites

El usuario informó una restauración en ACECode, desaparición del avance espontáneo y luego funcionamiento correcto de un firmware estable. No se confirmó el proyecto o binario exacto. Su nueva lectura y comparación se postergaron con el robot desconectado. El hash anterior no describe automáticamente ese firmware.

El agente no borró ni escribió flash ni envió movimientos. Las lecturas anteriores incluyeron un lector temporal en RAM y reinicios. La publicación documental no abre COM6.

Quedan pendientes modelo del ultrasónico, niveles de señal, GPIO reales, versión física y protocolo del Shield, parada efectiva, respaldo del estado estable y recuperación probada. La fuente de una biblioteca no sustituye esas comprobaciones.

Fuentes: [error 28 de Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/cm-prob-failed-install), [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html) y [ACEBOTT](https://acebott.com/tutorial/).
