from ibtsfif import detect_forgery, save_illuminant_map
from pathlib import Path

if __name__ == "__main__":
    resultado = detect_forgery("sua_imagem.jpg")  # ou caminho completo
    
    print("🔍 Resultado da perícia:")
    print(f"  → Imagem FORJADA? {'SIM' if resultado['is_forged'] else 'NÃO'}")
    print(f"  → Confiança: {resultado['probability']:.1%}")
    
    # Salva o mapa de iluminantes pra você ver as inconsistências
    save_illuminant_map(resultado["illuminant_map"], "illuminant_map.png")
    print("✅ Mapa de iluminantes salvo como 'illuminant_map.png'")