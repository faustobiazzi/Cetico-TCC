from __future__ import annotations
from .segmentation import segment_image
from .illuminant_estimation import estimate_illuminants_local_grayworld
from .feature_extraction import extract_inconsistency_features
from .classifier import IlluminantSVM
from .utils import load_image, save_illuminant_map
from pathlib import Path

__all__ = ["detect_forgery"]

def detect_forgery(image_path: str, model_path: str | None = None) -> dict:
    """Função principal para detectar falsificação por inconsistência de iluminantes"""
    img = load_image(image_path)
    segments = segment_image(img, scale=150)
    illuminant_map, _ = estimate_illuminants_local_grayworld(img, segments)
    features = extract_inconsistency_features(img, segments, illuminant_map)
    
    if model_path and Path(model_path).exists():
        svm = IlluminantSVM.load(model_path)
        is_forged, prob = svm.predict(features)
    else:
        # Fallback simples
        inconsistency_score = float(features[3] + features[4] + features[5])
        is_forged = inconsistency_score > 0.32
        prob = inconsistency_score
    
    return {
        "is_forged": bool(is_forged),
        "probability": float(prob),
        "features": features.tolist(),
        "illuminant_map": illuminant_map
    }