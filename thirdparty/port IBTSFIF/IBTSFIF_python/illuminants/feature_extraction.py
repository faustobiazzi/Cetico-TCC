import numpy as np
from scipy.stats import entropy

def extract_inconsistency_features(image: np.ndarray, segments: np.ndarray, illuminant_map: np.ndarray) -> np.ndarray:
    """
    Features baseadas nas inconsistências de iluminantes (mantém lógica original).
    Retorna um vetor de 12 features.
    """
    features = []
    
    # 1-3: estatísticas globais do mapa de iluminantes
    for c in range(3):
        channel = illuminant_map[..., c]
        features.extend([channel.mean(), channel.std(), channel.max() - channel.min()])
    
    # 4-6: variância entre superpixels vizinhos (inconsistência local)
    unique = np.unique(segments)
    illuminants_per_sp = []
    for label in unique:
        mask = (segments == label)
        if mask.sum() > 10:
            mean_ill = np.mean(illuminant_map[mask], axis=0)
            illuminants_per_sp.append(mean_ill)
    illuminants_per_sp = np.array(illuminants_per_sp)
    
    if len(illuminants_per_sp) > 1:
        diffs = np.abs(illuminants_per_sp[:-1] - illuminants_per_sp[1:])
        features.extend([diffs.mean(), diffs.std(), diffs.max()])
    else:
        features.extend([0.0, 0.0, 0.0])
    
    # 7-9: entropia por canal (medida de desordem)
    for c in range(3):
        hist, _ = np.histogram(illuminant_map[..., c].flatten(), bins=32, range=(0, 1))
        features.append(entropy(hist + 1e-8))
    
    # 10-12: correlação entre canais (quanto mais "colorido" o iluminante, mais suspeito)
    corr_rg = np.corrcoef(illuminant_map[..., 0].flatten(), illuminant_map[..., 1].flatten())[0, 1]
    corr_rb = np.corrcoef(illuminant_map[..., 0].flatten(), illuminant_map[..., 2].flatten())[0, 1]
    corr_gb = np.corrcoef(illuminant_map[..., 1].flatten(), illuminant_map[..., 2].flatten())[0, 1]
    features.extend([corr_rg, corr_rb, corr_gb])
    
    return np.array(features, dtype=np.float32)