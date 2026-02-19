# DIVISIÓN DE TRABAJO - EQUIPO DE VISIÓN ARTIFICIAL

---

##  Petter: DETECCIÓN DE LATAS
**Responsabilidad:** Detectar latas en la escena

### Archivos asignados:
- `src/detection/can_detector.py`
- `src/classification/can_classifier.py` (colaboración con Persona 2)

### Tareas específicas:
1.  Implementar detección de objetos negros por color HSV
2.  Filtrar contornos por forma (circular/rectangular)
3.  Calcular posición (x, y) y tamaño de cada lata
4.  Estimar distancia basándose en tamaño conocido (lata = 6.6cm diámetro)
5.  Clasificar latas: negro vs negro-amarillo
   - Analizar 25% inferior de la lata
   - Contar píxeles amarillos
   - Decidir: orgánica (15 pts) o inorgánica (5 pts)

### Entregables:
- Función `detect()` que retorna lista de latas detectadas
- Función `classify()` que determina tipo de lata
- Pruebas con imágenes de ejemplo

---

## PERSONA 2: DETECCIÓN DE CONTENEDORES
**Responsabilidad:** Detectar aros rojo y verde

### Archivos asignados:
- `src/detection/container_detector.py`
- Apoyo en `src/classification/can_classifier.py`

### Tareas específicas:
1. Detección de aro ROJO
   - Implementar dos rangos HSV (el rojo cruza 0°)
   - Combinar ambas máscaras
2. Detección de aro VERDE
   - Un solo rango HSV
3. Usar detección de círculos (HoughCircles)
4. Filtrar por tamaño esperado (~75cm = X píxeles según distancia)
5. Calcular posición y ángulo relativo al robot

### Entregables:
- Función `detect()` que encuentra ambos contenedores
- Información de posición y distancia
- Visualización de contenedores detectados

### Sugerencias:
- El rojo es complicado en HSV, prueba bien los dos rangos
- HoughCircles tiene muchos parámetros, experimenta

---

## # Archivos asignados:
- `src/detection/boundary_detector.py`

### Tareas específicas:
1.  Detección de color AZUL (lona del mar)
2.  Analizar posición del azul en el frame:
   - Abajo del frame = OK (lejos)
   - Arriba/lados = PELIGRO (cerca)
3.  Implementar sistema de alertas:
   - **SAFE:** Sin azul visible o muy lejos
   - **WARNING:** Azul visible en zona de advertencia
   - **DANGER:** Mucho azul, muy cerca del borde
4.  Calcular dirección segura para alejarse
5.  Contar tiempo fuera de la arena (para evitar >5s)

### Entregables:
- Función `detect()` con estado de límite
- Sistema de alertas funcionando
- Sugerencia de dirección segura

### Sugerencias:
- Esto es LO MÁS IMPORTANTE - prioriza robustez sobre velocidad
- Prueba con diferentes ángulos de cámara


---

## # Archivos asignados:
- `src/detection/obstacle_detector.py`

### Tareas específicas:
1.  Detección de objetos GRANDES (mucho más que latas)
2.  Usar detección de bordes + contornos
3.  Filtrar por área mínima (5000+ píxeles)
4.  Calcular bounding box de cada obstáculo
5.  Crear zona de exclusión (margen de seguridad)
6.  (Opcional) Clasificar tipo de obstáculo por forma:
   - Vertical alto = maniquí
   - Horizontal = silla
   - Forma característica = sombrilla

### Entregables:
- Función `detect()` que encuentra obstáculos
- Zonas de exclusión calculadas
- Advertencias de proximidad


### Sugerencias:
- Diferencia clave: TAMAÑO (obstáculos >> latas)
- No necesitas ser perfecto en clasificar qué es qué
- Lo importante es NO CHOCAR (especialmente con maniquí = -0.25 pts)
- Margen de seguridad generoso

---

---

##  (Bryan): INTEGRACIÓN

### Tareas específicas:
1.  Implementar gestión de cámara (laptop/ESP32)
2.  Crear pipeline que integre todos los detectores
3.  Establecer orden de ejecución (prioridades)
4.  Optimizar rendimiento (FPS, latencia)
5.  Crear herramienta de calibración
6.  Coordinar pruebas del equipo
7.  Resolver conflictos de integración

### Entregables:
- Sistema completo funcionando
- Documentación técnica
- Herramientas de calibración
- Reporte de rendimiento

---

## CRONOGRAMA SUGERIDO

### Semana 1: Desarrollo Individual
- Cada persona trabaja en su módulo
- Pruebas con imágenes estáticas
- Reunión diaria de 15 min (stand-up)

### Semana 2: Integración Inicial
- Líder integra módulos
- Pruebas con video en tiempo real
- Ajustes de parámetros

### Semana 3: Pruebas en Escenario Real
- Llevar laptop a la playa de prueba
- Calibrar colores HSV en condiciones reales
- Ajustar umbrales

### Semana 4: Optimización
- Mejorar FPS y precisión
- Documentar configuración final
- Preparar backup plans

### Semana 5: Preparación para Competencia
- Práctica con escenario completo
- Calibración rápida (90 segundos)
- Plan de contingencia

---

## HERRAMIENTAS DE COLABORACIÓN

### Control de Versiones (RECOMENDADO):
```bash
git init
git add .
git commit -m "Estructura inicial"
```

### Comunicación:
- Documentar decisiones importantes

### Pruebas:
- Cada persona crea su carpeta en `data/test_images/`
- Compartir casos de prueba complicados
- Reportar bugs en grupo

---

## DEFINICIÓN DE "TERMINADO"

Un módulo está completo cuando:
1.  Código implementado y comentado
2.  Probado con al menos 5 casos diferentes
3.  Funciona en tiempo real (>10 FPS)
4.  Documentado (docstrings)
5.  Integrado en el pipeline principal
6.  Revisado por al menos 1 compañero

---



### Avances (1 hora):
- Demo de avances
- Integración de módulos
- Planificación siguiente semanal
