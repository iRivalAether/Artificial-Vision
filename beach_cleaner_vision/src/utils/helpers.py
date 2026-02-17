"""
Funciones auxiliares y helpers generales
"""

import cv2
import numpy as np
import yaml
from pathlib import Path
from typing import Tuple, List, Dict, Any


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Carga archivo de configuración YAML
    
    Args:
        config_path: Ruta al archivo YAML
        
    Returns:
        Diccionario con configuración
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_config(config: Dict[str, Any], config_path: str):
    """
    Guarda configuración a archivo YAML
    
    Args:
        config: Diccionario con configuración
        config_path: Ruta donde guardar
    """
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Calcula distancia euclidiana entre dos puntos
    
    Args:
        point1: (x1, y1)
        point2: (x2, y2)
        
    Returns:
        Distancia en píxeles
    """
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def calculate_angle(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Calcula ángulo entre dos puntos
    
    Args:
        point1: Punto origen (x1, y1)
        point2: Punto destino (x2, y2)
        
    Returns:
        Ángulo en grados (-180 a 180)
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return np.degrees(np.arctan2(dy, dx))


def get_contour_center(contour: np.ndarray) -> Tuple[int, int]:
    """
    Calcula el centro de un contorno
    
    Args:
        contour: Contorno de OpenCV
        
    Returns:
        (cx, cy) centro del contorno
    """
    M = cv2.moments(contour)
    if M['m00'] == 0:
        return (0, 0)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return (cx, cy)


def calculate_circularity(contour: np.ndarray) -> float:
    """
    Calcula qué tan circular es un contorno
    
    Args:
        contour: Contorno de OpenCV
        
    Returns:
        Valor entre 0 y 1 (1 = círculo perfecto)
    """
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    
    if perimeter == 0:
        return 0
    
    circularity = 4 * np.pi * area / (perimeter ** 2)
    return min(circularity, 1.0)


def get_bounding_box(contour: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Obtiene el bounding box de un contorno
    
    Args:
        contour: Contorno de OpenCV
        
    Returns:
        (x, y, w, h) del rectángulo delimitador
    """
    return cv2.boundingRect(contour)


def calculate_aspect_ratio(contour: np.ndarray) -> float:
    """
    Calcula la relación de aspecto de un contorno
    
    Args:
        contour: Contorno de OpenCV
        
    Returns:
        Aspect ratio (height/width)
    """
    x, y, w, h = cv2.boundingRect(contour)
    if w == 0:
        return 0
    return h / w


def resize_with_aspect_ratio(image: np.ndarray, width: int = None, 
                              height: int = None) -> np.ndarray:
    """
    Redimensiona imagen manteniendo aspect ratio
    
    Args:
        image: Imagen a redimensionar
        width: Ancho deseado (opcional)
        height: Alto deseado (opcional)
        
    Returns:
        Imagen redimensionada
    """
    h, w = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        ratio = height / h
        new_width = int(w * ratio)
        return cv2.resize(image, (new_width, height))
    
    ratio = width / w
    new_height = int(h * ratio)
    return cv2.resize(image, (width, new_height))


def create_directory(path: str):
    """
    Crea directorio si no existe
    
    Args:
        path: Ruta del directorio
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def is_point_in_region(point: Tuple[int, int], 
                        region: Tuple[int, int, int, int]) -> bool:
    """
    Verifica si un punto está dentro de una región
    
    Args:
        point: (x, y)
        region: (x, y, width, height)
        
    Returns:
        True si está dentro, False si no
    """
    x, y = point
    rx, ry, rw, rh = region
    return rx <= x <= rx + rw and ry <= y <= ry + rh


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Limita un valor entre un mínimo y máximo
    
    Args:
        value: Valor a limitar
        min_value: Valor mínimo
        max_value: Valor máximo
        
    Returns:
        Valor limitado
    """
    return max(min_value, min(value, max_value))


def draw_text_with_background(image: np.ndarray, text: str, position: Tuple[int, int],
                               font_scale: float = 0.6, thickness: int = 2,
                               text_color: Tuple[int, int, int] = (255, 255, 255),
                               bg_color: Tuple[int, int, int] = (0, 0, 0),
                               padding: int = 5):
    """
    Dibuja texto con fondo sobre una imagen
    
    Args:
        image: Imagen donde dibujar
        text: Texto a dibujar
        position: (x, y) posición del texto
        font_scale: Tamaño de la fuente
        thickness: Grosor del texto
        text_color: Color del texto (B, G, R)
        bg_color: Color del fondo (B, G, R)
        padding: Padding alrededor del texto
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
    
    x, y = position
    cv2.rectangle(image, 
                  (x - padding, y - text_height - padding),
                  (x + text_width + padding, y + baseline + padding),
                  bg_color, -1)
    
    cv2.putText(image, text, (x, y), font, font_scale, text_color, thickness)
