# Mejoras pendientes de las variantes AP + IR y STA + IR

Registro para la publicación del 27/10/2026, basado en la revisión de código
realizada el 24/10/2026. Esta publicación conserva las versiones candidatas
preparadas; las mejoras siguientes todavía no se implementaron.

| Punto revisado | Comportamiento identificado | Trabajo pendiente |
| --- | --- | --- |
| Pérdida de conexión | Al terminar la conexión TCP, `Carloop()` cierra el cliente y asigna `val = 3`; ese tramo no envía una orden explícita de detener los motores. | Implementar y probar parada ante desconexión o falta de órdenes, y definir cómo volver a habilitar el movimiento. |
| Prioridad de STOP | Cuando IR está seleccionado, el controlador retorna antes de procesar la orden STOP de la app. OK detiene por IR. | Definir una parada común y comprobar su atención con cualquier control seleccionado. |
| Maniobras y melodías | Hay esperas bloqueantes en las maniobras y en la biblioteca del buzzer. | Reorganizar los tiempos para atender órdenes durante su ejecución y medir la respuesta. |
| Lecturas del ultrasónico | El seguimiento trata una lectura de cero como distancia menor a 15 cm y ordena retroceder. No distingue explícitamente una lectura inválida. | Validar mediciones y tiempos de espera antes de ordenar movimiento. |
| Velocidad de prueba | El control IR utiliza 255 y una espera nominal de 100 ms sin nueva orden. | Definir una velocidad inicial limitada y calibrar velocidad y respuesta en el robot. |
| Varios celulares | No hay un mecanismo de propietario exclusivo para todos los canales de control. | Definir quién controla y cómo se cede el control antes de implementar una interfaz propia. |

La revisión se refiere al código generado y a las bibliotecas examinadas de
ACECode 2.2.4. No determina cómo respondió físicamente esta unidad.

Las 17 pruebas actuales comprueban integridad, conservación de bloques y lógica
de selección de órdenes. No cubren los escenarios completos anteriores ni
demuestran parada física, calibración o compatibilidad de la app en STA.

Los valores de sensores, velocidades y tiempos proceden del ejemplo y deberán
contrastarse con ensayos reales. La interfaz propia y el simulador siguen como
propuestas. No se incorporan resultados experimentales al informe mediante
esta publicación y no se modifica el firmware instalado en el robot.
