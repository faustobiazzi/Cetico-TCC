from __future__ import annotations
import pickle
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from pathlib import Path
from typing import Tuple

class IlluminantSVM:
    def __init__(self):
        self.scaler = StandardScaler()
        self.svm = SVC(kernel='rbf', C=10, probability=True)
        self.is_trained = False
    
    def train(self, X: np.ndarray, y: np.ndarray):
        X_scaled = self.scaler.fit_transform(X)
        self.svm.fit(X_scaled, y)
        self.is_trained = True
        print(f"Modelo treinado com {len(y)} amostras")
    
    def predict(self, features: np.ndarray) -> Tuple[bool, float]:
        if not self.is_trained:
            raise RuntimeError("Treine o modelo primeiro!")
        
        X_scaled = self.scaler.transform(features.reshape(1, -1))
        prob = self.svm.predict_proba(X_scaled)[0][1]
        return (prob > 0.5), float(prob)
    
    def save(self, path: str = "modelo_svm.pkl"):
        with open(path, "wb") as f:
            pickle.dump((self.scaler, self.svm), f)
        print(f"Modelo salvo em {path}")
    
    @classmethod
    def load(cls, path: str = "modelo_svm.pkl"):
        model = cls()
        with open(path, "rb") as f:
            model.scaler, model.svm = pickle.load(f)
        model.is_trained = True
        return model