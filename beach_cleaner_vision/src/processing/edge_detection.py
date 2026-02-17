"""
Detección de bordes y contornos
"""

import cv2
import numpy as np
from typing import List, Tuple


class EdgeDetector:
    """Clase para detección de bordes"""
    
    def __init__(self, config: dict = None):
        """
        Inicializa el detector de bordes
        
        Args:
            config: Configuración del detector
        """
        self.config = config or {}
    
    def canny_edge(self, image: np.ndarray, 
                   threshold1: int = 50, 
                   threshold2: int = 150) -> np.ndarray:
        """
        Detección de bordes usando Canny
        
        Args:
            image: Imagen en escala de grises
            threshold1: Umbral inferior
            threshold2: Umbral superior
            
        Returns:
            Imagen con bordes detectados
        """
        return cv2.Canny(image, threshold1, threshold2)
    
    def sobel_edge(self, image: np.ndarray) -> np.ndarray:
        """
        Detección de bordes usando Sobel
        
        Args:
            image: Imagen en escala de grises
            
        Returns:
            Imagen con bordes detectados
        """
        # Gradientes en X e Y
        grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        
        # Magnitud del gradiente
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        
        edges = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        return edges
    
    def laplacian_edge(self, image: np.ndarray) -> np.ndarray:
        """
        Detección de bordes usando Laplaciano
        
        Args:
            image: Imagen en escala de grises
            
        Returns:
            Imagen con bordes detectados
        """
        laplacian = cv2.Laplacian(image, cv2.CV_64F)
        return cv2.convertScaleAbs(laplacian)
    
    def find_contours(self, mask: np.ndarray) -> List[np.ndarray]:
        """
        Encuentra contornos en una máscara binaria
        
        Args:
            mask: Máscara binaria
            
        Returns:
            Lista de contornos
        """
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)
        return contours
    
    def filter_contours_by_area(self, contours: List[np.ndarray],
                                min_area: float = 100,
                                max_area: float = 50000) -> List[np.ndarray]:
        """
        Filtra contornos por área
        
        Args:
            contours: Lista de contornos
            min_area: Área mínima
            max_area: Área máxima
            
        Returns:
            Lista de contornos filtrados
        """
        filtered = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if min_area <= area <= max_area:
                filtered.append(contour)
        return filtered
    
    def approximate_contour(self, contour: np.ndarray, 
                           epsilon_factor: float = 0.02) -> np.ndarray:
        """
        Aproxima un contorno a una forma más simple
        
        Args:
            contour: Contorno a aproximar
            epsilon_factor: Factor de aproximación
            
        Returns:
            Contorno aproximado
        """
        epsilon = epsilon_factor * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        return approx
    
    def detect_circles(self, image: np.ndarray,
                      min_radius: int = 10,
                      max_radius: int = 100) -> List[Tuple[int, int, int]]:
        """
        Detecta círculos usando transformada de Hough
        
        Args:
            image: Imagen en escala de grises
            min_radius: Radio mínimo
            max_radius: Radio máximo
            
        Returns:
            Lista de círculos [(x, y, radius), ...]
        """
        circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30,
                                   minRadius=min_radius,
                                   maxRadius=max_radius)
        
        if circles is None:
            return []
        
        circles = np.uint16(np.around(circles))
        return [(int(x), int(y), int(r)) for x, y, r in circles[0, :]]
    
    def detect_lines(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        Detecta líneas usando transformada de Hough
        
        Args:
            image: Imagen de bordes (binaria)
            
        Returns:
            Lista de líneas [(x1, y1, x2, y2), ...]
        """
        lines = cv2.HoughLinesP(image, 1, np.pi/180, 50,
                                minLineLength=50, maxLineGap=10)
        
        if lines is None:
            return []
        
        return [(int(x1), int(y1), int(x2), int(y2)) 
                for x1, y1, x2, y2 in lines[:, 0]]
