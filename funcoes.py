# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: funções do aplicativo (pseudo interface)
@programa: "Cético"

"""

#sub-sistemas
from __error import *

#modulos de funções
from facedetector.detectaface import detectorRosto
from imageproperties.lerExif import lertag
from thirdparty._illuminants import *

def buscarRosto(imagePath):
    try:
        face = detectorRosto(imagePath)
        return face
    except:
        erro_RetornoGenerico()

def propriedadesImagem(imagePath):
    try:
        ret = lertag(imagePath)
        return (ret)
    except:
        erroExif()

def illuminant (imagePath, vetorDeFaces):
    if vetorDeFaces!= []:
        if imagePath != "":
            try:
                ret = recebeImagemaSerAnalisada(imagePath, vetorDeFaces)
                return ret
            except:
                erroModuloGenérico()
        else:
            erroImagemNaoCarregada()
    else:
        erro_RetornoGenerico()