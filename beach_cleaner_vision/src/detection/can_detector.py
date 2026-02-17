"""
Detector de Latas (Residuos)
============================================
Responsable: [PERSONA 1]

DESCRIPCIÓN:
    Detecta latas negras y latas con franja amarilla en la imagen.
    Usa segmentación de color HSV y análisis de contornos.

TAREAS:
    - Detectar latas negras usando máscara HSV
    - Filtrar por forma circular/rectangular
    - Estimar posición y distancia
    - Marcar latas ya detectadas para no repetir

ENTRADA:
    - Frame de cámara (BGR)
    - Configuración de detección

SALIDA:
    - Lista de latas detectadas con:
        * Posición (x, y)
        * Radio/tamaño
        * Tipo (marcador para clasificación posterior)
        * Distancia estimada

PRIORIDAD: ALTA ⭐⭐⭐ (15-20 puntos dependen de esto)
"""

import cv2
import numpy as np
from typing import List, Dict, Tuple


class CanDetector:
    """Detector de latas en la escena"""
    
    def __init__(self, config: dict):
        """
        Inicializa el detector de latas
        
        Args:
            config: Configuración de detección (detection_config.yaml)
        """
        # TODO: Cargar parámetros de configuración
        pass
    
    def detect(self, frame: np.ndarray, hsv_frame: np.ndarray) -> List[Dict]:
        """
        Detecta todas las latas en el frame
        
        Args:
            frame: Imagen BGR original
            hsv_frame: Imagen convertida a HSV
            
        Returns:
            Lista de diccionarios con información de cada lata:
            [
                {
                    'center': (x, y),
                    'radius': radio,
                    'area': área_en_píxeles,
                    'bounding_box': (x, y, w, h),
                    'type': 'unknown',  # Se clasificará después
                    'distance': distancia_estimada
                },
                ...
            ]
        """
        # TODO: Implementar detección
        # 1. Crear máscara de color negro
        # 2. Aplicar operaciones morfológicas
        # 3. Encontrar contornos
        # 4. Filtrar por área y forma
        # 5. Extraer características de cada lata
        pass
    
    def _create_black_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        """Crea máscara de objetos negros"""
        # TODO: Usar cv2.inRange con rangos HSV del negro
        pass
    
    def _filter_by_shape(self, contours: List) -> List:
        """Filtra contornos que parezcan latas (circulares o rectangulares)"""
        # TODO: Verificar circularidad y aspect ratio
        pass
    
    def _estimate_distance(self, radius: int) -> float:
        """Estima distancia a la lata basándose en su tamaño en imagen"""
        # TODO: Usar tamaño conocido de lata (6.6cm) para calcular distancia
        pass
