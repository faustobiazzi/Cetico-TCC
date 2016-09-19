# -*- coding: utf-8 -*-
"""
Modified on Sun Sep 18 08:42:55 2016
@author: Fausto Biazzi de Sousa
@modulo: funções do aplicativo (pseudo interface)
@programa: "Cético"

"""

#sub-sistemas
from __error import *
from tkinter import *
import os
#import loading



#modulos de funções
from facedetector.detectaface import *
from imageproperties.lerExif import lertag
from thirdparty._illuminants import *


def buscarRosto(imagePath, values):
    try:

        face = detectorRosto(imagePath, values)

        return face
    except:
        erro_RetornoGenerico()


def propriedadesImagem(imagePath):
    try:
        ret = lertag(imagePath)
        return (ret)
    except:
        erroExif()


    
def Moduloilluminant(operacao, imagePath, vetorDeFaces):
    if platform.system() == 'Windows':
        funcaoIndisponivel(platform.system())
        print(platform.system())
    else:
        #loading.main()
        print("iniciando módulo illuminants")
        limparTudo()
        print("Pastas limpas")
        SegmentacaoDeimagens(imagePath)
        print("Imagem Segmentada")
        extrairGGE()
        print("Extraído GGE")
        extrairIIC()
        print("Extraído IIC")
        gerarTXTcomFacePositions(vetorDeFaces)
        print("Gerada posições de faces")
        extrairFeaturesVector(operacao)
        print("Vetores extraídos")
        limparPastasTemporarias()
        print("Limpando pastas temporárias")
        resultado =classificadorSVMCetico(operacao)
        print("Concluida analise SVM")
        analiseIlluminantsterminada()
    return resultado

