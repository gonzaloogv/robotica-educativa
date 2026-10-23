# Handoff técnico para Codex — ACEBOTT QD001 / Proyecto IEN 2026

> **Actualización posterior, 23/10/2026:** leer primero [el estado de continuidad](docs/estado_sesion_2026-10-23.md). El usuario informó un firmware estable posterior al respaldo inicial, pospuso su comparación y pidió no modificar el robot. MicroPython no está instalado. Las secciones siguientes conservan el contexto inicial del 20/10; no deben confundirse con el estado técnico actualizado.

**Corte de información:** 20 de octubre de 2026. **Estado:** diagnóstico y diseño; NO se autorizó modificar el firmware.

## 1. Propósito y contexto

Proyecto grupal del espacio curricular **Probabilidad y Estadística**, Tecnicatura Superior en Desarrollo de Software, IEN UEGP N.º 167. La profesora pidió implementar **movimiento automático**. El trabajo escrito se entrega el **6/11/2026** y la defensa es el **13/11/2026**. El objetivo experimental elegido es **movimiento autónomo y detención ante obstáculos**, con captura de datos genuinos para análisis estadístico. No inventar resultados ni representar planes como pruebas realizadas.

### Hechos confirmados directamente por el grupo
- Kit: **ACEBOTT QD001**, vehículo de cuatro ruedas Mecanum.
- Armado iniciado el **16/10/2026** y completado el **20/10/2026**.
- El sensor ultrasónico está instalado.
- El robot **se desplazó correctamente** mediante la app oficial ACEBOTT conectada por **Wi-Fi** el 20/10/2026.
- **Todavía no se probó autonomía ni captura de mediciones**.
- Se desea programar **MicroPython en el ESP32**, sujeto a preservar/reproducir el comportamiento previo si es viable.

### Datos de hardware extraídos del borrador (verificar antes de usar)
- Placa indicada en el informe: **ESP32 Max V1.0** (ACEBOTT, QA007/QA008/QA009).
- Placa de expansión indicada: **ESP32 Car Shield V2.0**.
- Motores TT DC con reductora, 4 unidades; servo SG90, sensor ultrasónico; otros sensores y módulos listados en el kit.
- **NO está demostrado el número de GPIO, el chip driver, el modelo exacto del sensor ni los niveles de señal en esta unidad**. La página genérica QB042/QB093 muestra TRIG=16, ECHO=17 para una conexión ilustrativa; NO extrapolar al QD001 con Car Shield V2.0.
- La ficha genérica del fabricante para QB042/QB093 informa 3 a 500 cm, frecuencia 40 kHz, precisión declarada 0,1 cm, alimentación 3,3–5 V. NO asumir que el sensor instalado sea exactamente esa variante sin confirmar.
- Confirmar el modelo del chip y tamaño de flash mediante herramientas de solo lectura. La página de ESP32 Max V1.0 declara ESP-WROOM-32 y 4 MB flash; es información de catálogo, no diagnóstico del dispositivo conectado.

## 2. Documentación principal (abrir y comprobar antes de programar)

Fuentes oficiales consultadas y accesibles el 20/10/2026:
1. Kit ACEBOTT QD001: https://acebott.com/docs/qd001-smart-car-starter-kit-for-esp32/
2. Placa ESP32 Max V1.0: https://acebottteam.github.io/acebott-docs-master/board/ESP32/QA007%20ESP32%20Max%20V1.0%20Controller%20Board.html
3. Sensor QB042/QB093: https://acebott.com/docs/qb042-qb093-ultrasonic-sensor/
4. Tutoriales ACEBOTT, distinguir V1.0/V2.0: https://acebott.com/es/tutorial/
5. MicroPython ESP32: https://docs.micropython.org/en/latest/esp32/quickref.html
6. MicroPython `machine`: https://docs.micropython.org/en/latest/library/machine.html
7. Espressif `esptool`, lectura de flash: https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html

Proyecto de terceros de referencia (no asumir que funciona con nuestra unidad y no tratarlo como documentación oficial):
- https://github.com/pepeangell5/SMART-CAR-QD001
- https://github.com/Emmanuelprime/acebott-qd001-pro

Comprobar cuidadosamente versiones de hardware, asignaciones de pines y licencias antes de reutilizar código. El segundo proyecto está dirigido a variantes QD001 Pro / QD003; la compatibilidad con QD001 base no está establecida.

## 3. Restricciones obligatorias de seguridad y manejo de datos

**En la primera iteración: SOLO diagnosticar, documentar y planificar. NO borrar, flashear, escribir flash, restaurar binarios, cambiar particiones ni ejecutar motores sin permiso explícito del usuario.**

- No usar modos automáticos que acepten sin revisión operaciones destructivas sobre hardware.
- No asumir un puerto COM o `/dev/ttyUSB*`; detectar puerto local y solicitar confirmación.
- La lectura del flash puede reiniciar o detener temporalmente el firmware activo: avisar antes de conectar.
- Antes de cualquier reemplazo de firmware, realizar respaldo íntegro, guardar log de diagnóstico, tamaño del archivo, huella SHA-256 y segunda copia **fuera del repositorio Git**. Preparar `.gitignore` para binarios, credenciales, dumps y datos potencialmente sensibles.
- Examinar si existen Secure Boot / Flash Encryption / protecciones de lectura; una imagen leída **no garantiza por sí sola** restauración funcional. Tener un plan de restauración y fuente de firmware original antes de grabar.
- No publicar credenciales Wi-Fi, claves, direcciones MAC personales, binarios originales o volcados de memoria.
- No conectar una señal ECHO de 5 V directamente a una entrada ESP32 de 3,3 V sin comprobar protección / acondicionamiento ya existente en el Shield. **No modificar cableado por suposiciones.**
- Primera prueba de actuadores con el chasis elevado y ruedas libres; pruebas en piso a velocidad baja y zona despejada.
- Failsafe: ante dato ultrasónico inválido, lectura expirada, error o pérdida de referencia de proximidad, **detener el movimiento**. Incluir mecanismo claro de parada manual.
- Las métricas provienen de ensayos reales, con fecha, condición, versión del código y método de medición; no generar tablas simuladas que se confundan con resultados.

## 4. Prioridades y plan por etapas

### Etapa A — Diagnóstico no destructivo
1. Detectar sistema operativo (Windows / Linux), herramientas instaladas y puerto USB del dispositivo; no asumir el entorno.
2. Comprobar comunicación serial sin forzar reset innecesario. Identificar chip y capacidad de flash con `esptool`.
3. Localizar tutorial exacto de **Car Shield V2.0** y tabla de GPIO verificable, preferentemente en el paquete oficial de ACEBOTT.
4. Documentar la relación entre el firmware original y el control de la app Wi-Fi, sin copiar credenciales en el repositorio.
5. Entregar un informe `docs/diagnostico_hardware.md` con fuentes, observaciones, incógnitas y riesgos.

### Etapa B — Respaldo verificable (requiere confirmación del usuario antes de conectar y leer)
1. Preparar un directorio local privado fuera del repositorio.
2. Respetando la sintaxis de la versión instalada de `esptool`, ejecutar comandos de lectura; ejemplo (sustituir `<PUERTO>`):

   ```shell
   python -m pip install esptool
   python -m esptool --port <PUERTO> flash-id
   python -m esptool --port <PUERTO> read-flash 0 ALL qd001-original.bin
   ```

3. Registrar tamaño, SHA-256 y verificar lectura (por ejemplo, segunda lectura y comparación hash, cuando sea posible). No declarar «respaldo restaurable» sin pruebas/condiciones.
4. Preparar `docs/procedimiento_respaldo_y_restauracion.md` **sin ejecutar ninguna escritura**.

### Etapa C — Factibilidad sin reemplazar firmware
1. Investigar si la app original utiliza comandos Wi-Fi documentados y si el QD001 base responde a ellos. No asumir que el protocolo de otro modelo coincide.
2. Si hay un protocolo fiable, proponer un cliente Python para PC y pruebas pasivas primero. Pedir autorización antes de enviar órdenes de movimiento.
3. Documentar limitación: **Python en la PC no equivale a MicroPython ejecutándose en el ESP32**, y por sí solo no cumple autonomía sin computadora.
4. Verificar si el firmware original tiene ya un modo autónomo accesible por una función documentada.

### Etapa D — Decisión de arquitectura (no implementar hasta revisar con usuario)
Comparar:
- **Opción 1, prioritaria si es viable:** reutilizar el firmware original para autonomía incorporada y telemetría desde PC, sin modificar la flash.
- **Opción 2:** instalar MicroPython nativo para autonomía real y captura por USB; la app original normalmente dejará de funcionar mientras esté reemplazado el firmware.
- **Opción 3:** construir firmware integrado que mantenga app Wi-Fi y nuevo modo autónomo. Puede requerir Arduino/C++ y trabajo adicional.
- **Opción 4, NO prioritaria:** multiboot con múltiples imágenes en flash. No significa ejecución simultánea y requiere personalizar arranque y particiones.

Recomendar con criterios: tiempo disponible, reversibilidad, riesgo eléctrico, compatibilidad de hardware, autonomía, facilidad para registrar datos y utilidad para la defensa académica.

### Etapa E — Programación autónoma y validación (con autorización explícita)
- Primero lectura de sensor con timeout y validación de rango.
- Luego control de motores mediante los pines confirmados y abstracción en módulos; no inventar mapas de GPIO.
- Lógica mínima: detenerse cuando haya obstáculo dentro de distancia de seguridad establecida experimentalmente; avanzar cuando esté libre; opcionalmente retroceder/girar después de validarlo.
- Configuración de umbral, velocidad PWM, intervalo de lectura y máximos de movimiento; inicialmente conservadores, calibrar con pruebas controladas.
- Captura de eventos CSV: tiempo relativo/marca, `trial_id`, distancia medida, distancia de referencia, PWM, orden, tipo de evento, éxito/fracaso, observaciones, y método de obtención de dato. **No crear columnas con mediciones ficticias**.
- Reproducibilidad: código versionado, manifest del montaje, protocolo de pruebas y tests de algoritmo con mocks (sin activar GPIO).

### Etapa F — Estadística e informe
- Repetibilidad: al menos 3 distancias fijas, varias lecturas por distancia; definir n antes del ensayo.
- Calibración: 8–10 puntos de distancia real, regresión medida vs real, MAE y residuos; explicar que correlación alta NO implica bajo error.
- Frenado: registrar cada intento y criterio de éxito predeterminado, frecuencia de éxito e interpretación binomial **si se justifican independencia y condiciones comparables**.
- PWM opcional: tiempo para distancia fija bajo varios niveles PWM, solo si hay tiempo/condiciones seguras.
- Calcular media, mediana, desviación estándar muestral, IC de la media según supuestos apropiados; tablas y gráficos con fuente, n, unidades y procedimiento.
- Colocar datos crudos y scripts reproducibles en anexos; los resultados se escriben después de ejecutar ensayos.

## 5. Arquitectura de repositorio recomendada (NO requiere acceso a hardware para crearla)

```text
qd001-robotica/
  README.md
  docs/
    diagnostico_hardware.md
    fuentes_tecnicas.md
    protocolo_experimental.md
    procedimiento_respaldo_y_restauracion.md
    bitacora_armado_y_pruebas.md
    mapa_pines_verificado.md
  firmware_micropython/     # desarrollar después de validar pinout
    boot.py
    main.py
    config.py
    sensors.py
    motors.py
    controller.py
    safety.py
  pc/
    capture_serial.py
  analysis/
    analyze_trials.py
    requirements.txt
  tests/
    test_controller.py
    test_measurements.py
  data/
    .gitkeep             # nunca subir archivos con secretos
  .gitignore
```

## 6. Criterios de aceptación por hito

- A: identificación de chip, flash, Shield y pines con fuente reproducible, y lista explícita de incógnitas.
- B: archivo binario original privado, tamaño correcto, SHA-256, comprobación documental de lectura y procedimiento de restauración propuesto.
- C: evidencia reproducible de compatibilidad o incompatibilidad del protocolo; no afirmar que funciona por similitud entre modelos.
- D: decisión de tecnología justificada y aprobada por el usuario.
- E: el robot se mueve autónomamente de manera segura y genera registros observables, solo tras permisos y pruebas graduales.
- F: conjunto de ensayos reales con CSV, gráficos, cálculos y limitaciones; nunca datos inventados.

## 7. Encargo inmediato a Codex

**En esta primera respuesta**: examinar estas fuentes; diseñar la estructura del repo; preparar los scripts de detección/lectura (sin ejecutarlos sobre el dispositivo hasta confirmación); explicar opciones de conservación del firmware; devolver preguntas mínimas bloqueantes y un plan de pruebas. **No borrar, flashear, escribir flash ni mover motores.**
