import numpy as np

def estimate_illuminants_local_grayworld(image: np.ndarray, segments: np.ndarray) -> np.ndarray:
    """Estimativa de iluminante por superpixel (Gray-World local)"""
    unique_segments = np.unique(segments)
    illuminants = np.zeros((len(unique_segments), 3), dtype=np.float32)
    
    for i, label in enumerate(unique_segments):
        mask = (segments == label)
        region = image[mask]
        if len(region) > 10:  # evita superpixels muito pequenos
            mean_color = np.mean(region, axis=0)
            # Normaliza (evita bias de intensidade)
            norm = np.linalg.norm(mean_color)
            if norm > 1e-6:
                illuminants[i] = mean_color / norm
            else:
                illuminants[i] = [1/3, 1/3, 1/3]
        else:
            illuminants[i] = [1/3, 1/3, 1/3]
    
    # Cria o mapa de iluminantes (mesma shape da imagem)
    illuminant_map = np.zeros_like(image, dtype=np.float32)
    for i, label in enumerate(unique_segments):
        mask = (segments == label)
        illuminant_map[mask] = illuminants[i]
    
    return illuminant_map, illuminants  # mapa + vetor por superpixel