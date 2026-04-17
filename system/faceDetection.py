import cv2
import os
import numpy as np
from pathlib import Path
from system.error_mgnt import ErrorManager

def detectFaces(imagePath, propriedades):
    try:
        minX, minY, minNei, scale = propriedades
        
        # 1. Localiza o XML de forma agnóstica ao SO
        script_dir = Path(__file__).parent.resolve()
        xml_path = script_dir / "default.xml"

        if not xml_path.exists():
            ErrorManager.handle_error("XML_NOT_FOUND", f"Arquivo não encontrado: {xml_path}")
            return []

        # 2. CARGA SEGURA DO XML (O pulo do gato para Windows/Linux)
        # Em vez de passar o path para o OpenCV, lemos os bytes e usamos um arquivo temporário 
        # ou garantimos a string absoluta normalizada. 
        # No Windows, o OpenCV CascadeClassifier EXIGE um arquivo físico, 
        # então vamos normalizar o caminho para o SO:
        xml_string = str(xml_path.absolute())
        faceCascade = cv2.CascadeClassifier(xml_string)

        # Se o classificador ainda falhar (devido ao caractere especial no path)
        if faceCascade.empty():
            # Plano B: Se o caminho falhar, tentamos forçar a string via sistema de arquivos
            faceCascade = cv2.CascadeClassifier(os.path.normpath(xml_string))

        if faceCascade.empty():
            ErrorManager.handle_error("XML_LOAD_ERROR", "OpenCV não conseguiu abrir o XML. Tente mover o projeto para um caminho sem acentos.")
            return []

        # 3. LEITURA SEGURA DA IMAGEM (Bytes -> Array -> OpenCV)
        try:
            # Lemos os bytes do arquivo (Python lida bem com 'Área de Trabalho')
            img_bytes = Path(imagePath).read_bytes()
            # Convertemos para um array que o OpenCV entende
            nparr = np.frombuffer(img_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        except Exception as e:
            ErrorManager.handle_error("IMG_READ_ERROR", f"Erro ao acessar imagem: {e}")
            return []

        if image is None:
            return []

        # 4. Processamento de Detecção
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=float(scale),
            minNeighbors=int(minNei),
            minSize=(int(minX), int(minY))
        )
        
        return faces

    except Exception as e:
        ErrorManager.handle_error("DETECTION_CORE_ERROR", str(e))
        return []