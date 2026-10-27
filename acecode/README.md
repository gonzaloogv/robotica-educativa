# QD001 V2 completo en modo STA

Esta guía corresponde a la variante STA anterior, que se conserva sin cambios.
Para STA con mando infrarrojo y todos los bloques de la ampliación, usar
[QD001_V2_STA_IR_Completo.sb3](versiones-ap-y-sta/QD001_V2_STA_IR_Completo.sb3) y
[su guía de configuración](sta-ir/README.md).
Para usar la red propia `ESP32-CAR` y el mando infrarrojo, abrir el
[proyecto AP + IR y su guía](PROYECTO_COMPLETO.md).

Abrir `QD001_V2_STA_Completo.sb3` con ACECode. Se adaptó el ejemplo instalado con ACECode 2.2.4: `4.4.2APPControlCar2(Final program).sb3`.

## Configuración

1. Antes de ingresar credenciales, usar Guardar como y nombrar la copia `QD001_V2_STA.local.sb3` (excluida de Git).
2. En el bloque Conectar Wi-Fi, reemplazar `CONFIGURAR_WIFI_2_4_GHZ` y `CONFIGURAR_CLAVE_WIFI` por los datos de la red local de 2,4 GHz. No enviar la clave por chat ni publicarla.
3. Mantener el celular en una red con acceso al robot; evitar redes de invitados o aislamiento entre clientes.
4. Para una futura prueba autorizada, abrir el monitor serie a 115200: después de conectar se imprime la IP obtenida por DHCP. En STA no aparece una red propia ESP32-CAR.

Este proyecto cierra AP, conecta como estación y espera la conexión antes de iniciar el servidor y las funciones originales. Con credenciales incorrectas queda esperando; no se debe interpretar como una conexión exitosa.

## Funciones preservadas

Se conservaron los bloques funcionales del fabricante: movimiento manual, evasión con ultrasónico, seguimiento de objeto, seguimiento de línea en sus dos modos, luces, buzzer/música y uso del servomotor del ejemplo. No se añadieron funciones de cámara, GPS o accesorios que no estuvieran implementadas en este proyecto.

El programa completo de app no incorpora el lector del pequeño mando infrarrojo. Ese mando requiere el ejemplo IR o una integración adicional; no se afirma que esta variante lo habilite.

## Acceso desde el celular

La biblioteca inicia servidor de app en TCP 100 y servidor HTTP. Para usar la app nativa en STA, su pantalla de Smart Car debe permitir indicar la nueva IP. Esa compatibilidad de interfaz no fue comprobada: si solo acepta el destino AP predeterminado, cambiar únicamente el ESP32 a STA no basta para conectar esa app. No se promete descubrimiento automático ni todas las opciones en la interfaz web.

## Verificación y límites

`manifest-sta.json` registra hashes, 434 bloques originales y 441 en la variante. Se comprobaron ZIP/CRC, conservación de recursos y que los bloques ajenos al encadenamiento de red no cambiaron. Se conservan GPIO y lógica originales, sin atribuirles una nueva verificación física.

No se compiló ni cargó este proyecto en el robot, no se verificó su funcionamiento físico y no se cambió el firmware estable. Antes de instalarlo: respaldar el estado estable actual, confirmar versión del Shield y realizar la prueba con ruedas libres. MicroPython no interviene en esta variante; es ACECode/Arduino.

## Reproducir la adaptación

Con Node.js, sin abrir ningún puerto:

```text
node tools/preparar_sta.js ORIGINAL.sb3 acecode/QD001_V2_STA_Completo.sb3
```

El destino debe ser nuevo. El generador usa marcadores fijos, sin credenciales reales, y conserva los recursos del archivo original.
