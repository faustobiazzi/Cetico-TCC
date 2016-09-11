# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: funções do aplicativo (pseudo interface)
@programa: "Cético"

"""

#sub-sistemas
from __error import *

#modulos de funç
from facedetector.detectaface import *
from imageproperties.lerExif import lertag
from thirdparty._illuminants import *
from tkinter import *


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


def illuminant(imagePath, vetorDeFaces):
    if vetorDeFaces != []:
        if imagePath != "":
            try:
                # ret = recebeImagemaSerAnalisada(imagePath, vetorDeFaces)
                print("entrou na função illuminantes")
                ret = Illuminants(imagePath, vetorDeFaces)

                return ret
            except NameError:
                erroModuloGenérico(str(NameError))
        else:
            erroImagemNaoCarregada()
    else:
        erro_RetornoGenerico()

