"""
Clasificador de Latas (Negro vs Negro-Amarillo)
============================================
Responsable: [PERSONA 1 o 2 - Complementa detección]

DESCRIPCIÓN:
    Clasifica latas detectadas en:
    - Inorgánicas: Negro completo → Contenedor ROJO (5 pts)
    - Orgánicas: Negro + franja amarilla 25% inferior → Contenedor VERDE (15 pts)
    
    ⚠️ IMPORTANTE: Separar mal = -5 puntos

TAREAS:
    - Analizar región inferior (25%) de cada lata detectada
    - Buscar píxeles amarillos en esa región
    - Decidir tipo basándose en threshold
    - Asignar contenedor destino

ENTRADA:
    - Latas detectadas (de can_detector)
    - Frame HSV

SALIDA:
    - Latas clasificadas:
        * type: 'organic' o 'inorganic'
        * target_container: 'red' o 'green'
        * confidence: nivel de confianza 0-1
"""

import cv2
import numpy as np
from typing import Dict, List


class CanClassifier:
    """Clasificador de latas (orgánicas vs inorgánicas)"""
    
    def __init__(self, config: dict):
        """
        Inicializa el clasificador
        
        Args:
            config: Configuración con threshold de amarillo
        """
        # TODO: Cargar threshold de píxeles amarillos
        pass
    
    def classify(self, can: Dict, frame: np.ndarray, 
                 hsv_frame: np.ndarray) -> Dict:
        """
        Clasifica una lata en orgánica o inorgánica
        
        Args:
            can: Diccionario con info de lata (de can_detector)
            frame: Imagen BGR original
            hsv_frame: Imagen en HSV
            
        Returns:
            Lata clasificada (modifica can dict):
            {
                ...datos previos de can...,
                'type': 'organic' o 'inorganic',
                'target_container': 'green' o 'red',
                'yellow_ratio': porcentaje_de_amarillo,
                'confidence': nivel_de_confianza
            }
        """
        # TODO: Implementar clasificación
        # 1. Extraer ROI de la lata
        # 2. Tomar región inferior (25%)
        # 3. Contar píxeles amarillos
        # 4. Decidir tipo basándose en threshold
        pass
    
    def classify_batch(self, cans: List[Dict], frame: np.ndarray,
                       hsv_frame: np.ndarray) -> List[Dict]:
        """Clasifica múltiples latas"""
        # TODO: Aplicar classify() a cada lata
        pass
    
    def _extract_can_roi(self, can: Dict, frame: np.ndarray) -> np.ndarray:
        """Extrae región de interés de la lata"""
        # TODO: Usar bounding_box para extraer región
        pass
    
    def _get_bottom_region(self, roi: np.ndarray, percentage: float = 0.25) -> np.ndarray:
        """Obtiene el 25% inferior de la región"""
        # TODO: Calcular y extraer porción inferior
        pass
    
    def _count_yellow_pixels(self, region: np.ndarray, 
                            hsv_region: np.ndarray) -> float:
        """Cuenta ratio de píxeles amarillos en la región"""
        # TODO: Máscara amarilla + countNonZero
        pass
    
    def _decide_type(self, yellow_ratio: float) -> str:
        """Decide tipo basándose en cantidad de amarillo"""
        # TODO: Comparar con threshold (ej: >15% = orgánica)
        pass
