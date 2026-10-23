# Variante STA del programa completo ACECode

Preparada en la rama [trabajo/acecode-sta](https://github.com/gonzaloogv/robotica-educativa/tree/trabajo/acecode-sta), separada de esta documentación y sin instalarla en el robot.

El archivo `acecode/QD001_V2_STA_Completo.sb3` deriva del ejemplo `4.4.2APPControlCar2(Final program).sb3` del QD001 V2 incluido en ACECode 2.2.4. Conserva los bloques de movimiento, evasión ultrasónica, seguimiento, dos modos de línea, luces, buzzer/música y servomotor. El cambio se limita al inicio de red: cierra AP, conecta como estación, espera conexión y muestra la IP por serie a 115200.

Incluye marcadores de red y clave, no credenciales reales. Antes de completarlos, guardar una copia `*.local.sb3` excluida de Git. Usar Wi-Fi de 2,4 GHz y una red que permita comunicación entre celular y robot. En STA no se crea una red propia ESP32-CAR.

La app nativa debe permitir configurar la IP local del robot para poder usarla en STA; esa función de la interfaz no se comprobó. La biblioteca conserva sus servidores, pero no se promete detección automática, compatibilidad de todas las pantallas o funciones de accesorios no implementados.

El proyecto completo de app no incluye el lector del mando pequeño infrarrojo. Mantener las funciones del ejemplo no equivale a agregar automáticamente IR o accesorios adicionales.

Se verificaron el archivo ZIP, CRC, recursos y conservación de bloques ajenos a la red. La variante tiene 441 bloques frente a 434 del original. No se compiló ni probó en hardware y no modifica el firmware estable hasta que alguien decida cargarla explícitamente. MicroPython no interviene en esta variante.

La comparación y respaldo del firmware estable siguen pendientes, tal como se acordó con el robot desconectado.
