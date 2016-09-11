# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: Detector de faces baseado no trabalho de Paul Viola com harcascade
@programa: "Cético"
"""

from __error import *
import cv2
import platform
import os

def detectorRosto(imagePath, propriedades):

    minX, minY, minNei, scale = propriedades
    script_dir = os.path.dirname(__file__)
    if platform.system() == 'Windows':
        cascPath = script_dir+"\default.xml"
        print(cascPath)
    else:
        cascPath = script_dir+"/default.xml"

    #print("detecta rostos" + imagePath)
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        #scaleFactor=1.1,
        #minNeighbors=1,
        #minSize=(30, 30),
        scaleFactor=scale,
        minNeighbors=minNei,
        minSize=(minX, minY),
        flags=cv2.CASCADE_SCALE_IMAGE)

    print(" {0} face(s) encontrada(s) automáticamente!".format(len(faces)))
    try:
        return faces
    except:
        erro_RetornoGenerico()
