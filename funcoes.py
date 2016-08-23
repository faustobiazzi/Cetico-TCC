# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: erros de sistema
@programa: "Cético"

"""
from PIL import Image
from PIL.ExifTags import TAGS


import cv2
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from __error import *



def detectorRosto(imagePath):

    cascPath = "default.xml"
    print ("detecta rostos"+imagePath)
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=1,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE)
        
    
    print (" {0} face(s) encontrada(s) automáticamente!".format(len(faces)))
    try:    
        return (faces)
    except:
        erro_RetornoGenerico()
 
def propriedadesImagem(arquivo):
    print ("entrou nas propriedades da imagem")
    try:
        ret = {}
        i = Image.open(arquivo)
        
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        print (ret)
        return (ret)
    except:
        erroExif()
  
