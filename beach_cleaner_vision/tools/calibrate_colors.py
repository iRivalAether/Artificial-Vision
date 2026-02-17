"""
Sistema de Calibración de Colores HSV
============================================
Responsable: [TODOS - Trabajo en equipo]

DESCRIPCIÓN:
    Herramienta interactiva para calibrar rangos HSV.
    Se usa en el escenario real antes de cada ronda (90 segundos disponibles).

USO:
    python tools/calibrate_colors.py
    
    - Captura frames de la cámara
    - Muestra sliders para ajustar rangos HSV
    - Permite guardar configuración calibrada
"""

import cv2
import numpy as np


def calibrate_color(camera_id: int = 0):
    """
    Abre interfaz de calibración de colores
    
    Args:
        camera_id: ID de la cámara a usar
    """
    # TODO: Crear ventana con trackbars
    # TODO: Capturar video
    # TODO: Mostrar máscara en tiempo real
    # TODO: Guardar valores cuando se presione 's'
    pass


if __name__ == '__main__':
    calibrate_color()
