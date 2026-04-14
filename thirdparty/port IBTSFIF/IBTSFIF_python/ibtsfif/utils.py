from __future__ import annotations
import cv2
import numpy as np
from pathlib import Path

def load_image(image_path: str | Path) -> np.ndarray:
    """Carrega imagem e converte para RGB"""
    img = cv2.imread(str(image_path))
    if img is None:
        raise FileNotFoundError(f"Não consegui carregar a imagem: {image_path}")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def save_illuminant_map(illuminant_map: np.ndarray, output_path: str | Path):
    """Salva o mapa de iluminantes para visualização"""
    vis = (illuminant_map / illuminant_map.max() * 255).astype(np.uint8)
    cv2.imwrite(str(output_path), cv2.cvtColor(vis, cv2.COLOR_RGB2BGR))