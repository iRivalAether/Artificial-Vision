"""
Preprocesamiento de imágenes para mejorar calidad de detección
"""

import cv2
import numpy as np
from typing import Tuple


class ImagePreprocessor:
    """Clase para preprocesar imágenes"""
    
    def __init__(self, config: dict = None):
        """
        Inicializa el preprocesador
        
        Args:
            config: Configuración de preprocesamiento
        """
        self.config = config or {}
        self.gaussian_kernel = self.config.get('gaussian_kernel', 5)
    
    def preprocess(self, image: np.ndarray, enhance_lighting: bool = True,
                   reduce_noise: bool = True) -> np.ndarray:
        """
        Aplica preprocesamiento completo a la imagen
        
        Args:
            image: Imagen de entrada
            enhance_lighting: Mejorar iluminación
            reduce_noise: Reducir ruido
            
        Returns:
            Imagen preprocesada
        """
        processed = image.copy()
        
        if enhance_lighting:
            processed = self.enhance_lighting(processed)
        
        if reduce_noise:
            processed = self.reduce_noise(processed)
        
        return processed
    
    def enhance_lighting(self, image: np.ndarray) -> np.ndarray:
        """
        Mejora la iluminación usando CLAHE
        
        Args:
            image: Imagen de entrada
            
        Returns:
            Imagen con iluminación mejorada
        """
        # Convertir a LAB para mejorar solo luminancia
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Aplicar CLAHE a canal L
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        
        # Recombinar
        enhanced_lab = cv2.merge([l, a, b])
        enhanced = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        
        return enhanced
    
    def reduce_noise(self, image: np.ndarray) -> np.ndarray:
        """
        Reduce ruido en la imagen
        
        Args:
            image: Imagen de entrada
            
        Returns:
            Imagen con ruido reducido
        """
        # Filtro bilateral: reduce ruido manteniendo bordes
        return cv2.bilateralFilter(image, 9, 75, 75)
    
    def gaussian_blur(self, image: np.ndarray, kernel_size: int = None) -> np.ndarray:
        """
        Aplica desenfoque gaussiano
        
        Args:
            image: Imagen de entrada
            kernel_size: Tamaño del kernel (debe ser impar)
            
        Returns:
            Imagen desenfocada
        """
        ksize = kernel_size or self.gaussian_kernel
        if ksize % 2 == 0:
            ksize += 1
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    
    def adjust_white_balance(self, image: np.ndarray) -> np.ndarray:
        """
        Ajusta balance de blancos automáticamente
        
        Args:
            image: Imagen de entrada
            
        Returns:
            Imagen con balance ajustado
        """
        result = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        avg_a = np.average(result[:, :, 1])
        avg_b = np.average(result[:, :, 2])
        
        result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
        result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
        
        result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
        return result
    
    def auto_canny(self, image: np.ndarray, sigma: float = 0.33) -> np.ndarray:
        """
        Detección de bordes Canny con umbrales automáticos
        
        Args:
            image: Imagen de entrada (escala de grises)
            sigma: Factor para calcular umbrales
            
        Returns:
            Imagen con bordes detectados
        """
        # Calcular mediana de la intensidad
        v = np.median(image)
        
        # Calcular umbrales automáticamente
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        
        return cv2.Canny(image, lower, upper)
    
    def sharpen(self, image: np.ndarray) -> np.ndarray:
        """
        Aumenta nitidez de la imagen
        
        Args:
            image: Imagen de entrada
            
        Returns:
            Imagen más nítida
        """
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        return cv2.filter2D(image, -1, kernel)
