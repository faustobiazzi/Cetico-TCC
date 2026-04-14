from __future__ import annotations

import numpy as np
from pathlib import Path
import requests
from typing import List, Tuple
from collections import Counter

from ibtsfif import (
    load_image,
    segment_image,
    estimate_illuminants_local_grayworld,
    extract_inconsistency_features
)
from ibtsfif.classifier import IlluminantSVM

from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# ==============================
# CONFIG
# ==============================

DATASET_DIR = Path("dataset")
CACHE_DIR = DATASET_DIR / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = Path("modelo_svm.pkl")

IMAGE_EXTENSIONS = ["*.jpg", "*.jpeg", "*.png"]


# ==============================
# DATASET REMOTO (LEVE)
# ==============================

REAL_IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/50/Vd-Orig.png",
    "https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/a3/June_odd-eyed-cat.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/8/89/Taj-Mahal.jpg"
]

FAKE_IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/2/24/Wilhelmshaven_Haven_fake.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/7d/Fake_image_example.jpg"
]

REMOTE_DATASET: List[Tuple[str, int]] = []

for url in REAL_IMAGES:
    REMOTE_DATASET.append((url, 0))

for url in FAKE_IMAGES:
    REMOTE_DATASET.append((url, 1))


# ==============================
# DOWNLOAD COM CACHE
# ==============================

def download_image(url: str) -> Path | None:
    filename = url.split("/")[-1]
    save_path = CACHE_DIR / filename

    if save_path.exists():
        return save_path

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        with open(save_path, "wb") as f:
            f.write(r.content)

        return save_path

    except Exception as e:
        print(f"⚠️ Erro ao baixar {url}: {e}")
        return None


# ==============================
# FEATURE EXTRACTION
# ==============================

def extract_features(image_path: Path) -> np.ndarray | None:
    try:
        img = load_image(str(image_path))

        # variação leve pra generalizar melhor
        scale = np.random.choice([100, 150, 200])
        segments = segment_image(img, scale=scale)

        illuminant_map, _ = estimate_illuminants_local_grayworld(img, segments)

        features = extract_inconsistency_features(img, segments, illuminant_map)

        return features

    except Exception as e:
        print(f"⚠️ Erro em {image_path}: {e}")
        return None


# ==============================
# LOAD LOCAL DATASET
# ==============================

def load_local_dataset():
    X, y = [], []

    for class_name, label in {"real": 0, "fake": 1}.items():
        class_path = DATASET_DIR / class_name

        if not class_path.exists():
            continue

        files = []
        for ext in IMAGE_EXTENSIONS:
            files.extend(class_path.glob(ext))

        print(f"📁 Local {class_name}: {len(files)} imagens")

        for f in tqdm(files, desc=f"Local {class_name}"):
            feat = extract_features(f)
            if feat is not None:
                X.append(feat)
                y.append(label)

    return X, y


# ==============================
# LOAD REMOTE DATASET
# ==============================

def load_remote_dataset():
    X, y = [], []

    print(f"\n🌐 Dataset remoto: {len(REAL_IMAGES)} reais / {len(FAKE_IMAGES)} falsas")

    for url, label in tqdm(REMOTE_DATASET, desc="Remoto"):
        path = download_image(url)
        if path is None:
            continue

        feat = extract_features(path)
        if feat is not None:
            X.append(feat)
            y.append(label)

    return X, y


# ==============================
# TREINO
# ==============================

def train():
    print("🔄 Carregando dados...\n")

    X_local, y_local = load_local_dataset()
    X_remote, y_remote = load_remote_dataset()

    X = np.array(X_local + X_remote)
    y = np.array(y_local + y_remote)

    print("\n📊 Distribuição das classes:", Counter(y))

    if len(X) < 10:
        print("❌ Poucos dados para treinar.")
        return

    # divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # incremental
    if MODEL_PATH.exists():
        print("\n♻️ Carregando modelo existente...")
        model = IlluminantSVM.load(str(MODEL_PATH))
    else:
        print("\n🆕 Criando novo modelo...")
        model = IlluminantSVM()

    model.svm.class_weight = "balanced"

    model.train(X_train, y_train)

    # avaliação
    y_pred = []
    for feat in X_test:
        pred, _ = model.predict(feat)
        y_pred.append(int(pred))

    print("\n📈 Relatório de classificação:")
    print(classification_report(y_test, y_pred, digits=4))

    # salvar modelo
    model.save(str(MODEL_PATH))
    print("\n💾 Modelo salvo com sucesso!")


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    train()