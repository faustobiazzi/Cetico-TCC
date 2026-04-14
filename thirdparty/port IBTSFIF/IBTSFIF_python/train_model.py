from __future__ import annotations
import numpy as np
from pathlib import Path
from ibtsfif import load_image, segment_image, estimate_illuminants_local_grayworld, extract_inconsistency_features
from ibtsfif.classifier import IlluminantSVM
from tqdm import tqdm
import pickle

def extract_features_from_image(image_path: str) -> np.ndarray | None:
    try:
        img = load_image(image_path)
        segments = segment_image(img, scale=150)
        illuminant_map, _ = estimate_illuminants_local_grayworld(img, segments)
        features = extract_inconsistency_features(img, segments, illuminant_map)
        return features
    except Exception as e:
        print(f"Erro na imagem {image_path}: {e}")
        return None

def train_from_data_base(data_base_path: str = "../IBTSFIF/data-base"):
    data_base_path = Path(data_base_path)
    if not data_base_path.exists():
        print(f"❌ Pasta data-base não encontrada em: {data_base_path}")
        print("Verifique o caminho e tente novamente.")
        return
    
    X = []
    y = []
    
    # Aqui vamos precisar ajustar conforme a estrutura real da sua data-base
    # Por enquanto assumindo subpastas "real" e "fake" ou "authentic" e "forged"
    print("🔍 Buscando imagens na data-base...")
    
    for label, class_name in enumerate(["real", "fake"]):   # <--- MUDE AQUI conforme suas pastas
        class_path = data_base_path / class_name
        if not class_path.exists():
            print(f"Aviso: pasta {class_name} não encontrada")
            continue
            
        image_files = list(class_path.glob("*.jpg")) + list(class_path.glob("*.png"))
        print(f"Encontradas {len(image_files)} imagens em {class_name}")
        
        for img_path in tqdm(image_files):
            features = extract_features_from_image(str(img_path))
            if features is not None:
                X.append(features)
                y.append(label)   # 0 = real, 1 = fake
    
    if len(X) == 0:
        print("Nenhuma feature extraída. Verifique a estrutura da data-base.")
        return
    
    X = np.array(X)
    y = np.array(y)
    
    print(f"\n✅ Extraídas {len(X)} amostras ({sum(y==0)} reais e {sum(y==1)} forjadas)")
    
    # Treina o modelo
    svm = IlluminantSVM()
    svm.train(X, y)
    svm.save("modelo_svm.pkl")
    
    print("🎉 Modelo treinado e salvo como 'modelo_svm.pkl'")

if __name__ == "__main__":
    train_from_data_base()