import numpy as np
from skimage.segmentation import felzenszwalb

def segment_image(image: np.ndarray, scale: float = 200, sigma: float = 0.8, min_size: int = 50) -> np.ndarray:
    """
    Mesma segmentação Felzenszwalb do método original.
    Parâmetros default próximos dos usados no TCC.
    """
    # skimage espera float [0,1]
    img_float = image.astype(float) / 255.0
    segments = felzenszwalb(img_float, scale=scale, sigma=sigma, min_size=min_size)
    return segments  # labels de 0 a N-1