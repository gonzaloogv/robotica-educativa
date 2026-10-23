# Estado de continuidad — 23 de octubre de 2026

Este documento permite continuar desde otra computadora y separa lo comprobado de lo informado por el usuario.

## Estado al cerrar la sesión

- El usuario informó que el robot quedó funcionando correctamente con un firmware estable después de restaurar o cargar desde ACECode. No se identificó el archivo exacto instalado ni se registraron las pruebas de cada función.
- El robot quedó desconectado. Su nuevo respaldo y comparación se postergaron expresamente: «lo probamos después».
- Instrucción vigente: «sin modificaciones en el robot». Esta etapa comprende documentación y archivos, sin abrir COM6.
- El agente no ejecutó borrados ni escrituras de flash, no instaló MicroPython y no envió movimientos. La carga del ejemplo de app se detuvo antes de ejecutarse.
- El respaldo disponible corresponde al estado ANTERIOR a la restauración. No es una copia del firmware estable actual ni una imagen acreditada de fábrica.
- Los documentos se publican en `documentacion`. La preparación técnica y la imagen cifrada anterior están en la rama técnica local `trabajo/micropython-respaldo`; no se incluyen binarios ni claves en esta publicación documental.

## Comprobaciones anteriores a la restauración

| Elemento | Resultado |
| --- | --- |
| USB | Puente WCH CH340/CH341, VID 1A86 / PID 7523. |
| Controlador | Inicialmente faltante, error 28. Después: WCH 4.0.2026.2 firmado, estado OK. |
| Puerto de esta PC | COM6; no asumirlo en otra computadora. |
| Chip consultado | ESP32-D0WD-V3, revisión 3.1. |
| Flash | 4 MB; fabricante 0x68, dispositivo 0x4016. |
| Protecciones leídas | Secure Boot V1/V2 desactivados, FLASH_CRYPT_CNT = 0 y descarga UART habilitada. |
| Respaldo anterior | Dos lecturas de 4.194.304 bytes, SHA-256 idéntico y verificación contra flash satisfactoria. |
| Restauración física del respaldo | No ensayada. |

La identificación del chip no confirma todas las conexiones del Shield, el modelo del sensor ni sus niveles eléctricos.

## Wi-Fi y mando incluido

Antes de la restauración, el usuario informó avance continuo al encender y ausencia de la red. El análisis del respaldo era compatible con un programa sin inicialización de control Wi-Fi, pero no reconstruyó el proyecto original ni confirmó una causa única. Esos hallazgos no describen automáticamente el firmware estable posterior.

El mando fue descrito como pequeño, con números y flechas: es del tipo infrarrojo y no depende del Wi-Fi del celular. El programa de la placa debe atender sus órdenes.

Se localizaron estos ejemplos del QD001 V2 en ACECode 2.2.4:

| Archivo | Alcance revisado |
| --- | --- |
| `4.4.1APPControlCar1.sb3` | Control manual por app; configura ESP32-CAR y su servidor. |
| `4.4.2APPControlCar2(Final program).sb3` | Ejemplo ampliado con modos y sensores. |
| `4.2.1IRremoteCar.sb3` | Infrarrojo; incluye parada por falta de pulsaciones. |
| `4.1IRremoteTest.sb3` | Lectura de teclas para diagnóstico. |

Origen local: `C:/Program Files/ACECode/extraFiles/compile/sample-program/QD001~QD010(V2)/QD001/`. Se revisaron archivos y generadores sin ejecutar bloques ni subirlos al robot. El agente no completó una compilación o prueba física de esos ejemplos en esta sesión.

## MicroPython

Se descargó MicroPython 1.29.0 ESP32_GENERIC, publicación 2026-08-24. NO está instalado. Todavía no se implementó ni validó un programa MicroPython del proyecto.

La [guía para trabajar sin robot](continuidad_micropython_sin_robot.md) separa lógica en PC e integración física. Conectar el USB no instala MicroPython ni garantiza que el código funcione en el kit.

## Próximo encuentro

1. Registrar el proyecto o binario estable instalado y las funciones efectivamente probadas.
2. Coordinar una lectura que puede reiniciar la placa y obtener un respaldo NUEVO, separado del anterior.
3. Comparar aplicación, particiones y datos persistentes. Un hash global distinto puede deberse a configuración y no prueba por sí solo un cambio de código.
4. Conservar el firmware estable mientras se verifica recuperación y mapa de hardware.
5. Si luego se autoriza MicroPython, validar sensor y parada, después motores con ruedas libres y por último ensayos controlados.

Ver también [diagnóstico](diagnostico_hardware.md), [análisis histórico de Wi-Fi](diagnostico_arranque_wifi.md) y [respaldo y recuperación](procedimiento_respaldo_y_restauracion.md).
