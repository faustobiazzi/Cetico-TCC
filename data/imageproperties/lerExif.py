# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: funções do aplicativo (pseudo interface)
@programa: "Cético"

"""

from PIL import Image
from PIL.ExifTags import TAGS

#from tkinter import messagebox
# from tkinter.filedialog import askopenfilename
#from __error import *


def lertag(arquivo):
    ret = {}
    i = Image.open(arquivo)

    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
