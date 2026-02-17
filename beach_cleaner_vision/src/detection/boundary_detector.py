"""
Detector de Límites (Borde Arena/Mar)
============================================
Responsable: [PERSONA 3]

DESCRIPCIÓN:
    Detecta el límite entre la arena y la lona azul (mar).
    CRÍTICO: Robot pierde puntos si sale >5 segundos de la arena.

TAREAS:
    - Detectar lona azul en los bordes del frame
    - Crear zona de advertencia antes del límite
    - Alertar cuando robot se acerca al mar
    - Sugerir dirección segura para no salir

ENTRADA:
    - Frame de cámara
    - Configuración de color azul

SALIDA:
    - Estado del límite:
        * safe: Lejos del límite
        * warning: Cerca del límite (zona de advertencia)
        * danger: Muy cerca o sobre el límite
    - Dirección sugerida para alejarse
    - Máscara del área azul

PRIORIDAD: CRÍTICA ⚠️⚠️⚠️ (puede descalificar al robot)
"""

import cv2
import numpy as np
from typing import Dict, Tuple, List


class BoundaryDetector:
    """Detector de límites (arena vs mar)"""
    
    def __init__(self, config: dict):
        """
        Inicializa el detector de límites
        
        Args:
            config: Configuración de detección
        """
        # TODO: Cargar umbrales y zonas de advertencia
        pass
    
    def detect(self, frame: np.ndarray, hsv_frame: np.ndarray) -> Dict:
        """
        Detecta límites y determina si hay peligro
        
        Args:
            frame: Imagen BGR
            hsv_frame: Imagen HSV
            
        Returns:
            Diccionario con información del límite:
            {
                'status': 'safe' | 'warning' | 'danger',
                'blue_ratio': porcentaje_de_azul_en_frame,
                'boundary_regions': lista_de_regiones_azules,
                'safe_direction': ángulo_para_alejarse (si hay peligro),
                'distance_to_boundary': distancia_estimada_en_píxeles
            }
        """
        # TODO: Implementar detección
        # 1. Crear máscara de color azul
        # 2. Analizar posición del azul en el frame
        # 3. Determinar nivel de peligro
        # 4. Calcular dirección segura
        pass
    
    def _create_blue_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        """Crea máscara del color azul (mar)"""
        # TODO: cv2.inRange con rango de azul
        pass
    
    def _analyze_boundary_position(self, mask: np.ndarray) -> str:
        """Analiza dónde está el azul y determina peligro"""
        # TODO: Dividir frame en regiones, ver dónde hay más azul
        # Abajo = OK, arriba/lados = DANGER
        pass
    
    def _calculate_safe_direction(self, blue_regions: List) -> float:
        """Calcula ángulo hacia donde debe moverse para alejarse del mar"""
        # TODO: Vector opuesto a la concentración de azul
        pass
