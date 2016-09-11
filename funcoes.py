# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: funções do aplicativo (pseudo interface)
@programa: "Cético"

"""

#sub-sistemas
from __error import *
from tkinter import *
import os


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
    if operacao == "segmentar":
        SegmentaçãoDeimagens(imagePath)
        extrairGGE()
        extrairIIC()
    if operacao == "TODOS" or "acc" or "bic" or  "ccv" or  "eoac" or  "las" or  "lch" or  "sasi" or  "spytec" or  "unser":
        extrairDescritores(operacao)

