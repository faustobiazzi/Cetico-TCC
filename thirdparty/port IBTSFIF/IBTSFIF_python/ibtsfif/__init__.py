from __future__ import annotations
from .segmentation import segment_image
from .illuminant_estimation import estimate_illuminants_local_grayworld
from .feature_extraction import extract_inconsistency_features
from .classifier import IlluminantSVM
from .utils import load_image, save_illuminant_map
from pathlib import Path

__all__ = ["detect_forgery"]

def detect_forgery(image_path):
    image = load_image(image_path)
    
    # 1. Segmentação
    segments = segment_image(image)
    
    # 2. Iluminantes
    illuminant_map, _ = estimate_illuminants_local_grayworld(image, segments)
    
    # 3. Features
    features = extract_inconsistency_features(image, segments, illuminant_map)
    
    # 4. Classificação
    model = IlluminantSVM.load()
    is_forged, prob = model.predict(features)
    
    return {
        "is_forged": is_forged,
        "probability": prob,
        "illuminant_map": illuminant_map,
        "segments": segments,
        "features": features
    }