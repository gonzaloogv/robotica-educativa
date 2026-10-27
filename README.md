# Robótica educativa — preparación técnica y respaldo

Estado vigente: [contexto completo del 27/10/2026](docs/estado_sesion_2026-10-27.md). MicroPython y el programa USB están cargados; luces, música y ultrasónico respondieron. Los motores no giraron visiblemente y siguen en diagnóstico.

Esta rama conserva el respaldo cifrado del estado inicial de la sesión del 23/10/2026 y las herramientas locales para comprobarlo o extraerlo. No es una copia acreditada del firmware de fábrica ni del estado estable que el usuario informó después de restaurar desde ACECode.

Consultar [las instrucciones del respaldo](backups/acebott-qd001/README.md). La clave queda fuera de Git, en las copias privadas de C: y D:. Clonar esta rama no alcanza para descifrar sin esa clave. Los binarios originales sin cifrar no se publican.

El 27/10/2026 se instaló MicroPython 1.29.0 en el ESP32 por pedido del usuario, reemplazando el programa ACEBOTT. La escritura se verificó y el intérprete respondió por USB en COM6 a 115200 baudios. El usuario indicó omitir el respaldo del estado actual; el respaldo cifrado anterior sigue conservado. Consultar el [registro de instalación](docs/instalacion_micropython_2026-10-27.md).

Luego se cargó el [programa Python USB para QD001](firmware_micropython/README.md): arranque detenido, sensor ultrasónico, luces, música y órdenes manuales con movimiento limitado por tiempo. Se comprobó la carga, el arranque detenido y la lectura del sensor; no se probaron desplazamientos físicos.

Estado actualizado y guía para continuar desde casa: rama [documentacion](https://github.com/gonzaloogv/robotica-educativa/tree/documentacion). La versión completa de ACECode preparada para STA está separada en [trabajo/acecode-sta](https://github.com/gonzaloogv/robotica-educativa/tree/trabajo/acecode-sta).
