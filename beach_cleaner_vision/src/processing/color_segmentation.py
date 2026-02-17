"""
Segmentación de imagen por color usando HSV
"""

import cv2
import numpy as np
from typing import Tuple, List, Dict


class ColorSegmentation:
    """Clase para segmentar imagen por colores"""
    
    def __init__(self, color_config: dict):
        """
        Inicializa el segmentador
        
        Args:
            color_config: Diccionario con rangos de colores HSV
        """
        self.color_config = color_config
        self.masks = {}
    
    def segment_by_color(self, hsv_image: np.ndarray, 
                         color_name: str) -> np.ndarray:
        """
        Segmenta imagen por un color específico
        
        Args:
            hsv_image: Imagen en espacio HSV
            color_name: Nombre del color ('black', 'yellow', 'red', etc.)
            
        Returns:
            Máscara binaria del color
        """
        if color_name not in self.color_config:
            raise ValueError(f"Color '{color_name}' no encontrado en configuración")
        
        color_info = self.color_config[color_name]
        
        # El rojo necesita dos rangos
        if color_name == 'red':
            lower1 = np.array(color_info['lower1'])
            upper1 = np.array(color_info['upper1'])
            lower2 = np.array(color_info['lower2'])
            upper2 = np.array(color_info['upper2'])
            
            mask1 = cv2.inRange(hsv_image, lower1, upper1)
            mask2 = cv2.inRange(hsv_image, lower2, upper2)
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            lower = np.array(color_info['lower'])
            upper = np.array(color_info['upper'])
            mask = cv2.inRange(hsv_image, lower, upper)
        
        return mask
    
    def segment_all_colors(self, hsv_image: np.ndarray) -> Dict[str, np.ndarray]:
        """
        Segmenta todos los colores configurados
        
        Args:
            hsv_image: Imagen en espacio HSV
            
        Returns:
            Diccionario con máscaras por cada color
        """
        self.masks = {}
        
        for color_name in self.color_config.keys():
            self.masks[color_name] = self.segment_by_color(hsv_image, color_name)
        
        return self.masks
    
    def apply_morphology(self, mask: np.ndarray, 
                        kernel_size: int = 5,
                        erosion_iter: int = 1,
                        dilation_iter: int = 2) -> np.ndarray:
        """
        Aplica operaciones morfológicas para limpiar máscara
        
        Args:
            mask: Máscara binaria
            kernel_size: Tamaño del kernel morfológico
            erosion_iter: Iteraciones de erosión
            dilation_iter: Iteraciones de dilatación
            
        Returns:
            Máscara procesada
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        
        # Erosión para eliminar ruido pequeño
        if erosion_iter > 0:
            mask = cv2.erode(mask, kernel, iterations=erosion_iter)
        
        # Dilatación para restaurar tamaño
        if dilation_iter > 0:
            mask = cv2.dilate(mask, kernel, iterations=dilation_iter)
        
        return mask
    
    def opening(self, mask: np.ndarray, kernel_size: int = 5) -> np.ndarray:
        """
        Operación de apertura (erosión + dilatación)
        Elimina ruido pequeño
        
        Args:
            mask: Máscara binaria
            kernel_size: Tamaño del kernel
            
        Returns:
            Máscara procesada
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    def closing(self, mask: np.ndarray, kernel_size: int = 5) -> np.ndarray:
        """
        Operación de cierre (dilatación + erosión)
        Rellena agujeros pequeños
        
        Args:
            mask: Máscara binaria
            kernel_size: Tamaño del kernel
            
        Returns:
            Máscara procesada
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    def find_largest_contour(self, mask: np.ndarray) -> Tuple[np.ndarray, float]:
        """
        Encuentra el contorno más grande en la máscara
        
        Args:
            mask: Máscara binaria
            
        Returns:
            (contorno, área) o (None, 0) si no hay contornos
        """
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            return None, 0
        
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        
        return largest_contour, area
    
    def count_pixels(self, mask: np.ndarray) -> int:
        """
        Cuenta píxeles no ceros en la máscara
        
        Args:
            mask: Máscara binaria
            
        Returns:
            Número de píxeles blancos
        """
        return cv2.countNonZero(mask)
    
    def calculate_color_ratio(self, mask: np.ndarray, 
                              total_pixels: int = None) -> float:
        """
        Calcula el ratio de píxeles del color en la máscara
        
        Args:
            mask: Máscara binaria
            total_pixels: Total de píxeles (si None, usa tamaño de mask)
            
        Returns:
            Ratio entre 0 y 1
        """
        color_pixels = self.count_pixels(mask)
        
        if total_pixels is None:
            total_pixels = mask.shape[0] * mask.shape[1]
        
        if total_pixels == 0:
            return 0
        
        return color_pixels / total_pixels
