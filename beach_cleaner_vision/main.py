"""
Beach Cleaner Vision - Main Entry Point
TMR 2026 - Equipo de Visión Artificial

Punto de entrada del sistema de visión.
NOTA: Este módulo solo se encarga de DETECCIÓN y CLASIFICACIÓN visual.
      Otros equipos manejan movimiento y recolección.
"""

import cv2
import sys
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from utils.logger import get_logger
from utils.helpers import load_config
from core.vision_pipeline import VisionPipeline


def main():
    """Función principal"""
    
    # Inicializar logger
    logger = get_logger('main')
    logger.info("=== Beach Cleaner Vision System ===")
    logger.info("TMR 2026 - Categoría Robot Limpiador de Playa")
    
    # Cargar configuración
    try:
        camera_config = load_config('config/camera_config.yaml')
        detection_config = load_config('config/detection_config.yaml')
        vision_config = load_config('config/vision_config.yaml')
        
        logger.info("Configuración cargada correctamente")
        
    except Exception as e:
        logger.error(f"Error cargando configuración: {e}")
        return
    
    # TODO: Inicializar pipeline de visión
    # pipeline = VisionPipeline(camera_config, detection_config)
    
    # TODO: Ejecutar sistema
    # pipeline.run()
    
    logger.info("Sistema iniciado. Presiona 'q' para salir.")
    
    # Por ahora, solo un placeholder
    print("\n" + "="*50)
    print("SISTEMA DE VISIÓN ARTIFICIAL")
    print("Beach Cleaner Robot - TMR 2026")
    print("="*50)
    print("\nEstructura creada correctamente.")
    print("Listo para dividir trabajo entre el equipo.")
    print("\nVer: DIVISION_DE_TRABAJO.md para asignaciones")
    print("="*50)


if __name__ == '__main__':
    main()
