# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
@author: Fausto Biazzi de Sousa
@modulo: leitor de informaçoes de imagem
@programa: "Cético"

"""

import os, sys
from data.libs import exifread
from PIL import Image
from PIL.ExifTags import TAGS


def nodecoded(arquivo):
    i = Image.open(arquivo)
    return i.info


def full(arquivo):
    ret = {}
    i = Image.open(arquivo)

    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def exiftaged (arquivo):
    ret = []
    f = open(arquivo, 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        ret.append("Key: %s, value %s" % (tag, tags[tag]))
    return ret
'''
def exiftaged(arquivo):
    ret = {}
    i = Image.open(arquivo)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
'''

def tag(arquivo,field):
    i = Image.open(arquivo)
    info = i._getexif()
    for tag, value in info.items():
        if TAGS.get(tag) == field:
            return value

