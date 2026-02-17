"""
Filtros diversos para procesamiento de imagen
"""

import cv2
import numpy as np


class Filters:
    """Clase con diversos filtros de imagen"""
    
    @staticmethod
    def median_filter(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
        """
        Aplica filtro de mediana para reducir ruido
        
        Args:
            image: Imagen de entrada
            kernel_size: Tamaño del kernel (debe ser impar)
            
        Returns:
            Imagen filtrada
        """
        if kernel_size % 2 == 0:
            kernel_size += 1
        return cv2.medianBlur(image, kernel_size)
    
    @staticmethod
    def bilateral_filter(image: np.ndarray, d: int = 9, 
                        sigma_color: float = 75,
                        sigma_space: float = 75) -> np.ndarray:
        """
        Filtro bilateral: reduce ruido preservando bordes
        
        Args:
            image: Imagen de entrada
            d: Diámetro de vecindad
            sigma_color: Filtro en espacio de color
            sigma_space: Filtro en espacio de coordenadas
            
        Returns:
            Imagen filtrada
        """
        return cv2.bilateralFilter(image, d, sigma_color, sigma_space)
    
    @staticmethod
    def morphological_gradient(mask: np.ndarray, 
                               kernel_size: int = 5) -> np.ndarray:
        """
        Gradiente morfológico: diferencia entre dilatación y erosión
        
        Args:
            mask: Máscara binaria
            kernel_size: Tamaño del kernel
            
        Returns:
            Gradiente morfológico
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
    
    @staticmethod
    def top_hat(mask: np.ndarray, kernel_size: int = 9) -> np.ndarray:
        """
        Top Hat: diferencia entre imagen y apertura
        Resalta estructuras pequeñas brillantes
        
        Args:
            mask: Imagen de entrada
            kernel_size: Tamaño del kernel
            
        Returns:
            Transformación top hat
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    
    @staticmethod
    def black_hat(mask: np.ndarray, kernel_size: int = 9) -> np.ndarray:
        """
        Black Hat: diferencia entre cierre e imagen
        Resalta estructuras pequeñas oscuras
        
        Args:
            mask: Imagen de entrada
            kernel_size: Tamaño del kernel
            
        Returns:
            Transformación black hat
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    
    @staticmethod
    def remove_shadows(image: np.ndarray) -> np.ndarray:
        """
        Intenta remover sombras de la imagen
        
        Args:
            image: Imagen BGR de entrada
            
        Returns:
            Imagen con sombras reducidas
        """
        rgb_planes = cv2.split(image)
        result_planes = []
        
        for plane in rgb_planes:
            dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
            bg_img = cv2.medianBlur(dilated_img, 21)
            diff_img = 255 - cv2.absdiff(plane, bg_img)
            result_planes.append(diff_img)
        
        return cv2.merge(result_planes)
    
    @staticmethod
    def adaptive_threshold(image: np.ndarray, 
                          block_size: int = 11,
                          c: int = 2) -> np.ndarray:
        """
        Umbralización adaptativa
        
        Args:
            image: Imagen en escala de grises
            block_size: Tamaño del vecindario (debe ser impar)
            c: Constante a restar
            
        Returns:
            Imagen binaria
        """
        if block_size % 2 == 0:
            block_size += 1
        
        return cv2.adaptiveThreshold(image, 255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, block_size, c)
    
    @staticmethod
    def normalize_illumination(image: np.ndarray) -> np.ndarray:
        """
        Normaliza la iluminación de la imagen
        
        Args:
            image: Imagen BGR
            
        Returns:
            Imagen con iluminación normalizada
        """
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Normalizar canal L
        l_normalized = cv2.normalize(l, None, 0, 255, cv2.NORM_MINMAX)
        
        merged = cv2.merge([l_normalized, a, b])
        return cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
