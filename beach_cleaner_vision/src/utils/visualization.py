"""
Visualización de resultados de detección
"""

import cv2
import numpy as np
from typing import List, Tuple, Dict, Any
from .helpers import draw_text_with_background


class Visualizer:
    """Clase para visualizar resultados de detección"""
    
    # Colores para visualización (BGR)
    COLORS = {
        'can_black': (0, 0, 0),
        'can_yellow': (0, 255, 255),
        'container_red': (0, 0, 255),
        'container_green': (0, 255, 0),
        'boundary_warning': (0, 165, 255),  # Naranja
        'obstacle': (0, 255, 255),  # Amarillo
        'detection': (0, 255, 0),  # Verde
        'text': (255, 255, 255),
        'background': (0, 0, 0)
    }
    
    def __init__(self, show_fps=True, show_labels=True):
        """
        Inicializa el visualizador
        
        Args:
            show_fps: Mostrar FPS
            show_labels: Mostrar etiquetas de objetos
        """
        self.show_fps = show_fps
        self.show_labels = show_labels
        self.fps = 0
    
    def draw_detections(self, image: np.ndarray, 
                        detections: Dict[str, List[Dict[str, Any]]]) -> np.ndarray:
        """
        Dibuja todas las detecciones sobre la imagen
        
        Args:
            image: Imagen donde dibujar
            detections: Diccionario con detecciones por tipo
            
        Returns:
            Imagen con detecciones dibujadas
        """
        vis_image = image.copy()
        
        # Dibujar latas
        if 'cans' in detections:
            for can in detections['cans']:
                self._draw_can(vis_image, can)
        
        # Dibujar contenedores
        if 'containers' in detections:
            for container in detections['containers']:
                self._draw_container(vis_image, container)
        
        # Dibujar límites/advertencias
        if 'boundaries' in detections:
            for boundary in detections['boundaries']:
                self._draw_boundary(vis_image, boundary)
        
        # Dibujar obstáculos
        if 'obstacles' in detections:
            for obstacle in detections['obstacles']:
                self._draw_obstacle(vis_image, obstacle)
        
        # Dibujar FPS
        if self.show_fps:
            self._draw_fps(vis_image)
        
        return vis_image
    
    def _draw_can(self, image: np.ndarray, can: Dict[str, Any]):
        """Dibuja una lata detectada"""
        center = can.get('center', (0, 0))
        radius = can.get('radius', 10)
        can_type = can.get('type', 'inorganic')
        
        # Color según tipo
        color = self.COLORS['can_yellow'] if can_type == 'organic' else self.COLORS['can_black']
        
        # Dibujar círculo
        cv2.circle(image, center, radius, color, 2)
        cv2.circle(image, center, 3, color, -1)
        
        # Etiqueta
        if self.show_labels:
            label = f"Lata {'ORGANICA' if can_type == 'organic' else 'INORGANICA'}"
            if 'distance' in can:
                label += f" ({can['distance']:.0f}px)"
            draw_text_with_background(image, label, 
                                      (center[0] - 40, center[1] - radius - 10),
                                      font_scale=0.5, thickness=1,
                                      text_color=color)
    
    def _draw_container(self, image: np.ndarray, container: Dict[str, Any]):
        """Dibuja un contenedor detectado"""
        center = container.get('center', (0, 0))
        radius = container.get('radius', 20)
        color_type = container.get('color', 'red')
        
        # Color según tipo
        color = self.COLORS[f'container_{color_type}']
        
        # Dibujar círculo
        cv2.circle(image, center, radius, color, 3)
        
        # Etiqueta
        if self.show_labels:
            label = f"Contenedor {color_type.upper()}"
            draw_text_with_background(image, label,
                                      (center[0] - 50, center[1] - radius - 15),
                                      font_scale=0.6, thickness=2,
                                      text_color=color)
    
    def _draw_boundary(self, image: np.ndarray, boundary: Dict[str, Any]):
        """Dibuja advertencia de límite"""
        if 'region' in boundary:
            x, y, w, h = boundary['region']
            cv2.rectangle(image, (x, y), (x+w, y+h), 
                         self.COLORS['boundary_warning'], 2)
            
            if self.show_labels:
                draw_text_with_background(image, "¡LIMITE!",
                                          (x, y - 10),
                                          font_scale=0.7, thickness=2,
                                          text_color=(0, 0, 255),
                                          bg_color=(255, 255, 255))
    
    def _draw_obstacle(self, image: np.ndarray, obstacle: Dict[str, Any]):
        """Dibuja un obstáculo detectado"""
        if 'region' in obstacle:
            x, y, w, h = obstacle['region']
            cv2.rectangle(image, (x, y), (x+w, y+h),
                         self.COLORS['obstacle'], 2)
            
            if self.show_labels:
                draw_text_with_background(image, "OBSTACULO",
                                          (x, y - 10),
                                          font_scale=0.6, thickness=2,
                                          text_color=self.COLORS['obstacle'])
    
    def _draw_fps(self, image: np.ndarray):
        """Dibuja FPS en la esquina"""
        fps_text = f"FPS: {self.fps:.1f}"
        draw_text_with_background(image, fps_text, (10, 30),
                                  font_scale=0.7, thickness=2,
                                  text_color=self.COLORS['text'],
                                  bg_color=self.COLORS['background'])
    
    def update_fps(self, fps: float):
        """Actualiza el valor de FPS"""
        self.fps = fps
    
    def draw_hsv_ranges(self, image: np.ndarray, masks: Dict[str, np.ndarray]) -> np.ndarray:
        """
        Dibuja las máscaras de color HSV lado a lado
        
        Args:
            image: Imagen original
            masks: Diccionario con máscaras por color
            
        Returns:
            Imagen con máscaras visualizadas
        """
        h, w = image.shape[:2]
        
        # Crear imagen de salida
        num_masks = len(masks)
        if num_masks == 0:
            return image
        
        rows = (num_masks + 2) // 3
        cols = min(3, num_masks)
        
        cell_h = h // rows
        cell_w = w // cols
        
        output = np.zeros((cell_h * rows, cell_w * cols, 3), dtype=np.uint8)
        
        for idx, (name, mask) in enumerate(masks.items()):
            row = idx // cols
            col = idx % cols
            
            # Convertir máscara a BGR
            mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            mask_resized = cv2.resize(mask_bgr, (cell_w, cell_h))
            
            # Colocar en grid
            y1 = row * cell_h
            y2 = y1 + cell_h
            x1 = col * cell_w
            x2 = x1 + cell_w
            
            output[y1:y2, x1:x2] = mask_resized
            
            # Etiqueta
            draw_text_with_background(output, name.upper(),
                                      (x1 + 10, y1 + 30),
                                      font_scale=0.5, thickness=1)
        
        return output
