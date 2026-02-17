"""
Detector de Obstáculos (Maniquí, Silla, Sombrilla)
============================================
Responsable: [PERSONA 4]

DESCRIPCIÓN:
    Detecta obstáculos grandes en el escenario:
    - Maniquí (tamaño real) - NO TOCAR: -0.25 puntos
    - Silla de sol
    - Sombrilla de playa

TAREAS:
    - Detectar objetos grandes usando contornos
    - Diferenciar de latas (mucho más grandes)
    - Calcular zona de exclusión alrededor de obstáculos
    - Advertir cuando robot está muy cerca

ENTRADA:
    - Frame de cámara
    - Configuración de tamaños

SALIDA:
    - Lista de obstáculos con:
        * Posición (x, y)
        * Tamaño (ancho, alto)
        * Tipo estimado (mannequin/chair/umbrella)
        * Distancia
        * Zona de exclusión

PRIORIDAD: MEDIA ⭐⭐ (evitar penalizaciones)
"""

import cv2
import numpy as np
from typing import List, Dict


class ObstacleDetector:
    """Detector de obstáculos grandes"""
    
    def __init__(self, config: dict):
        """
        Inicializa el detector de obstáculos
        
        Args:
            config: Configuración de detección
        """
        # TODO: Cargar umbrales de tamaño
        pass
    
    def detect(self, frame: np.ndarray) -> List[Dict]:
        """
        Detecta obstáculos en la escena
        
        Args:
            frame: Imagen BGR
            
        Returns:
            Lista de obstáculos:
            [
                {
                    'type': 'mannequin' | 'chair' | 'umbrella' | 'unknown',
                    'bounding_box': (x, y, w, h),
                    'center': (x, y),
                    'area': área_en_píxeles,
                    'distance': distancia_estimada,
                    'exclusion_zone': (x, y, w, h)  # Zona a evitar
                },
                ...
            ]
        """
        # TODO: Implementar detección
        # 1. Convertir a escala de grises
        # 2. Detectar bordes
        # 3. Encontrar contornos grandes
        # 4. Filtrar por área mínima (mucho más grande que latas)
        # 5. Clasificar tipo de obstáculo (opcional)
        pass
    
    def _find_large_contours(self, frame: np.ndarray) -> List:
        """Encuentra contornos grandes que puedan ser obstáculos"""
        # TODO: Threshold + findContours + filtro por área
        pass
    
    def _classify_obstacle(self, contour: np.ndarray, 
                           bbox: Tuple[int, int, int, int]) -> str:
        """Intenta clasificar el tipo de obstáculo basándose en forma"""
        # TODO: Aspect ratio, forma, etc.
        # Vertical alto = maniquí
        # Horizontal = silla
        # Forma especial = sombrilla
        pass
    
    def _calculate_exclusion_zone(self, bbox: Tuple[int, int, int, int], 
                                  margin: int = 50) -> Tuple[int, int, int, int]:
        """Calcula zona de exclusión alrededor del obstáculo"""
        # TODO: Expandir bounding box con margen de seguridad
        pass
