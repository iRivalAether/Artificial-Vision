"""
Sistema de logging para Beach Cleaner Vision
"""

import logging
import os
from datetime import datetime
from pathlib import Path


class Logger:
    """Clase para gestionar logging del sistema"""
    
    def __init__(self, name='beach_cleaner', log_dir='logs', level=logging.INFO):
        """
        Inicializa el logger
        
        Args:
            name: Nombre del logger
            log_dir: Directorio para guardar logs
            level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Evitar duplicar handlers
        if self.logger.handlers:
            return
            
        # Crear directorio de logs si no existe
        log_path = Path(log_dir)
        log_path.mkdir(parents=True, exist_ok=True)
        
        # Formato de log
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Handler para archivo
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_handler = logging.FileHandler(
            log_path / f'{name}_{timestamp}.log',
            encoding='utf-8'
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def debug(self, message):
        """Log mensaje de debug"""
        self.logger.debug(message)
    
    def info(self, message):
        """Log mensaje informativo"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log advertencia"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log crítico"""
        self.logger.critical(message)


def get_logger(name='beach_cleaner', log_dir='logs', level=logging.INFO):
    """
    Función helper para obtener un logger
    
    Args:
        name: Nombre del logger
        log_dir: Directorio para logs
        level: Nivel de logging
        
    Returns:
        Instancia de Logger
    """
    return Logger(name, log_dir, level)
