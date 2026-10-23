# Análisis histórico del respaldo anterior: arranque y Wi-Fi

**No describe el firmware estable actual.** Después de esta revisión, el usuario informó una restauración desde ACECode y funcionamiento correcto. El respaldo y comparación de ese nuevo estado se postergaron. Véase [el estado vigente](estado_sesion_2026-10-23.md).

## Situación anterior informada

El robot avanzaba al encender y el usuario no encontraba su red Wi-Fi. El movimiento no fue reproducido por el agente ni se enviaron órdenes a los motores. El usuario conserva el proyecto original en otra computadora; no estuvo disponible para examinar sus bloques.

Con el robot informado como apagado, se abrió COM6 a 115200 durante 12 segundos solo para recibir, con DTR y RTS desactivados y sin enviar bytes. No llegaron mensajes. Eso no demuestra que la aplicación estuviera detenida ni explica su comportamiento. No se forzó un reinicio en esa captura.

## Imagen anterior examinada

- Particiones: nvs en 0x9000, otadata en 0xE000, app0 en 0x10000, app1 en 0x150000, spiffs en 0x290000 y coredump en 0x3F0000.
- app0 contiene una imagen ESP32 de cinco segmentos, 368.548 bytes de datos y fin de segmentos en 0x69FE4. Sus checksum y SHA-256 internos resultaron correctos.
- Los metadatos incluyen Arduino/ESP-IDF v4.4.5. La fecha de compilación de una biblioteca no determina cuándo se instaló el programa ni identifica su fuente.
- En los segmentos válidos no se encontraron los textos WiFi, softAP, softap, lwip, tcpip, esp_wifi, ESP32-CAR o ESP32-Car. Hay una aparición de wifi en minúsculas. Examinar cadenas no reconstruye el flujo de ejecución.
- ESP32-CAR aparece guardado en NVS, no como literal en los segmentos de la aplicación. Parte de los textos de red hallados al revisar toda la flash están fuera de la imagen válida y pueden ser restos de programas anteriores.
- La configuración NVS conserva ap.hidden = 0, ap.chan = 5 y ap.max.conn = 4. Son valores guardados, no prueba de que el radio estuviera encendido.
- SPIFFS está completamente en 0xFF en esa imagen. No se publicaron claves o contenidos privados.

## Interpretación y límites

Los indicios son compatibles con un programa de movimiento que no inicia un punto de acceso. No se confirmó una causa única, un modo persistido de avance o una avería del sensor. El respaldo conserva el estado inicial de esta sesión y no acredita ser firmware de fábrica.

Posteriormente se revisaron los ejemplos QD001 V2 instalados con ACECode 2.2.4. El de app configura ESP32-CAR y su servidor; el de mando pequeño recibe infrarrojo y no depende del Wi-Fi. Conectar COM6 o cerrar el programa de PC no restaura automáticamente el software anterior de la placa. El agente no cargó esos ejemplos.

## Continuación

El usuario informó un firmware estable posterior y decidió probar su comparación en otra ocasión. Cuando corresponda, identificar su proyecto, obtener un respaldo separado y comparar aplicación y configuración sin sobrescribir el respaldo histórico. Por ahora no conectar al puerto ni modificar el robot para completar documentos.

Fuentes oficiales: [ACECode](https://acebott.com/docs/getting-started-with-acecode/), [software](https://acebott.com/software/) y [tutoriales](https://acebott.com/tutorial/).
