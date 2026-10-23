# Diagnóstico de arranque y ausencia de Wi-Fi — 2026-10-23

## Situación informada por el usuario

El robot avanza hacia adelante sin detenerse al encender y no aparece la red ESP32 en el teléfono. El usuario atribuye el avance a un programa o configuración cargado desde el software ACEBOTT y confirmó que conserva el proyecto. El movimiento no fue reproducido por el agente ni se enviaron órdenes a los motores.

## Comprobación de conexión

Con el robot informado como apagado, Windows reconoce USB-SERIAL CH340 (COM6). Se abrió COM6 a 115200 durante 12 segundos, únicamente para recibir datos, con DTR y RTS desactivados y sin enviar bytes. No se recibieron mensajes. Esto no prueba que la aplicación esté detenida ni permite diagnosticar su ejecución. El registro queda fuera de Git, en la carpeta privada de respaldo. No se forzó un reinicio durante esta captura.

## Análisis local del respaldo

- Tabla de particiones: nvs en 0x9000, otadata en 0xE000, app0 en 0x10000, app1 en 0x150000, spiffs en 0x290000 y coredump en 0x3F0000.
- app0 contiene una imagen ESP32 con cinco segmentos, 368.548 bytes de datos de segmento y fin de segmentos en 0x69FE4. Se comprobaron su checksum y SHA-256 internos: correctos.
- Los metadatos identifican componentes Arduino/ESP-IDF v4.4.5. La fecha de compilación de la biblioteca no establece cuándo se cargó el programa ni identifica su proyecto fuente.
- En los segmentos válidos no se encontraron los textos WiFi, softAP, softap, lwip, tcpip, esp_wifi, ESP32-CAR ni ESP32-Car. Hay una aparición de wifi en minúsculas. Esta inspección de cadenas no equivale a reconstruir el flujo de ejecución.
- El texto ESP32-CAR aparece en la partición de configuración NVS, no como literal en los segmentos de la aplicación. Parte de los textos de red detectados al revisar el rango completo de flash están fuera de la imagen válida y pueden ser restos de programas anteriores.
- La configuración NVS conserva ap.hidden = 0, ap.chan = 5 y ap.max.conn = 4. Son valores guardados, no prueba de que el radio esté iniciado ahora. No se muestran claves ni contenidos privados.
- La partición SPIFFS está completamente en 0xFF en el respaldo.

## Hipótesis y alcance

Los hallazgos son compatibles con un programa de movimiento cargado que no inicia un punto de acceso Wi-Fi. La causa exacta del avance y la ausencia de red sigue pendiente de revisar el proyecto .sb3 o .ino conservado por el grupo. No se atribuye el comportamiento a un modo persistido concreto ni a una avería del sensor sin evidencia adicional.

El respaldo conserva el estado que tenía la unidad al comenzar esta sesión. No acredita que sea firmware de fábrica. Restaurarlo recuperaría ese estado, incluido el comportamiento del programa respaldado; no es una corrección del avance automático.

ACECode para Windows puede servir para abrir el proyecto y revisar sus bloques. Subir un proyecto sí sustituye el programa de la placa. Se mantiene la instrucción de no borrar ni reemplazar firmware. El análisis inicial del .sb3 se puede hacer como archivo, sin instalar ACECode, ejecutar bloques ni acceder al robot.

## Próximo paso

Obtener la ubicación o el archivo del proyecto que el usuario conserva y revisar eventos de inicio, bucles de avance, orden de parada, inicialización Wi-Fi y relación con el control por app. Mantener apagada la alimentación de motores para el diagnóstico y ruedas libres en cualquier prueba posterior.

Fuentes oficiales:
- https://acebott.com/docs/getting-started-with-acecode/
- https://acebott.com/software/
- https://acebott.com/tutorial/
