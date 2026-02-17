"""
Detector de Contenedores (Aros Rojo y Verde)
============================================
Responsable: [PERSONA 2]

DESCRIPCIÓN:
    Detecta los contenedores rojo (residuos generales) y verde (orgánicos).
    Son aros de 75cm de diámetro que deben ser visibles desde arriba.

TAREAS:
    - Detectar aro rojo usando máscara HSV (dos rangos por cruce de 0°)
    - Detectar aro verde usando máscara HSV
    - Usar detección de círculos de Hough
    - Calcular posición y orientación del robot respecto a contenedores

ENTRADA:
    - Frame de cámara
    - Configuración de colores

SALIDA:
    - Lista de contenedores detectados:
        * Color (red/green)
        * Posición (x, y)
        * Radio
        * Distancia y ángulo desde robot

PRIORIDAD: ALTA ⭐⭐⭐ (necesario para depositar residuos)
"""

import cv2
import numpy as np
from typing import List, Dict, Optional


class ContainerDetector:
    """Detector de contenedores (aros rojo y verde)"""
    
    def __init__(self, config: dict):
        """
        Inicializa el detector de contenedores
        
        Args:
            config: Configuración de detección
        """
        # TODO: Cargar parámetros
        pass
    
    def detect(self, frame: np.ndarray, hsv_frame: np.ndarray) -> List[Dict]:
        """
        Detecta contenedores rojo y verde
        
        Args:
            frame: Imagen BGR
            hsv_frame: Imagen HSV
            
        Returns:
            Lista de contenedores detectados:
            [
                {
                    'color': 'red' o 'green',
                    'center': (x, y),
                    'radius': radio_en_píxeles,
                    'distance': distancia_estimada,
                    'angle': ángulo_desde_robot
                },
                ...
            ]
        """
        # TODO: Implementar detección
        # 1. Detectar aro rojo
        # 2. Detectar aro verde
        # 3. Usar HoughCircles para encontrar círculos
        # 4. Filtrar por tamaño esperado
        pass
    
    def _detect_red_container(self, hsv_frame: np.ndarray) -> Optional[Dict]:
        """Detecta contenedor rojo (requiere dos rangos HSV)"""
        # TODO: Combinar dos masks para el rojo
        pass
    
    def _detect_green_container(self, hsv_frame: np.ndarray) -> Optional[Dict]:
        """Detecta contenedor verde"""
        # TODO: Crear mask verde y detectar círculo
        pass
    
    def _find_circles(self, mask: np.ndarray) -> List[Tuple[int, int, int]]:
        """Encuentra círculos en la máscara usando Hough"""
        # TODO: cv2.HoughCircles con parámetros apropiados
        pass
