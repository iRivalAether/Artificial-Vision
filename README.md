# Beach Cleaner Vision System
Sistema de Visión Artificial - TMR 2026


##  Tareas de Visión

### Detecciones Requeridas:
1.  **Latas** (residuos) - Negro y Negro-Amarillo
2.  **Contenedores** - Rojo (general) y Verde (orgánicos)
3. **Límites** - Lona azul (mar) - **CRÍTICO**
4.  **Obstáculos** - Maniquí, silla, sombrilla

### Salidas del Sistema:
- Lista de objetos detectados con posiciones
- Clasificación de latas (orgánico/inorgánico)
- Alertas de límites y obstáculos
- Información para toma de decisiones

---

##  Arquitectura del Sistema de Visión

```
beach_cleaner_vision/
├──  config/              # Configuraciones YAML
├──  src/
│   ├──  core/            # Sistema principal (cámara, pipeline)
│   ├──  detection/       # Detectores (latas, contenedores, límites, obstáculos)
│   ├──  classification/  # Clasificación de residuos (orgánico/inorgánico)
│   ├──  processing/      # Procesamiento de imagen (HSV, filtros, bordes)
│   └──  utils/           # Utilidades (logging, helpers, visualización)
├──  tools/               # Herramientas de calibración HSV
├──  data/                # Imágenes de prueba y calibración
├──  tests/               # Pruebas unitarias
└── main.py                 # Punto de entrada
```

---

##  Instalación

### 1. Requisitos
- Python 3.8+
- Cámara (laptop o ESP32-CAM)

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar
Editar archivos en `config/` según tu setup.

---

##  Uso

### Ejecutar sistema completo:
```bash
python main.py
```

### Calibrar colores (antes de competencia):
```bash
python tools/calibrate_colors.py
```

### Test de rendimiento:
```bash
python tools/performance_test.py
```

---

##  División de Trabajo

Ver: **DIVISION_DE_TRABAJO.md**

---

##  Notas de Desarrollo

### Fase Actual: **DESARROLLO (Python en PC)**
- Plataforma: Laptop/PC
- Cámara: Webcam USB
- Framework: OpenCV completo
- Objetivo: Algoritmos validados

### Fase Futura: **PRODUCCIÓN (C++ en ESP32)**
- Plataforma: ESP32-CAM
- Resolución: 320x240 optimizada
- Migración: Código simplificado y optimizado
- Objetivo: Sistema embebido autónomo

---

## Hardware de Visión

- **Desarrollo:** Cámara Laptop (Python + OpenCV)
- **Producción:** ESP32-CAM + OV2640 (C++ optimizado)

---

##  Documentación Adicional

- `docs/TECHNICAL_SPEC.pdf` - Especificaciones técnicas
- `config/*.yaml` - Configuraciones comentadas
- Código fuente con docstrings detallados

--- Equipo de Visión

**4 Personas:**
- Persona 1: Detección de latas
- Persona 2: Detección de contenedores
- Persona 3: Detección de límites
- Persona 4: Detección de obstáculos
- Bryan: Integración del sistema

Ver: **[DIVISION_DE_TRABAJO.md](DIVISION_DE_TRABAJO.md)** para detalles completos.
