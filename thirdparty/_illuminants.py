# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:51:18 2016

@author: Fausto Biazzi de Sousa
programa = "Cético"
versão = "Alpha 0.0.0.3"

"""

import shutil
import platform
import os
from thirdparty.illuminants.sourcecode.extractGGEMaps import extractNewGrayWorldMaps
from thirdparty.illuminants.sourcecode.extractIICMaps import extractIlluminantMaps

programa = "Cético"
Modulo = "Illuminants"


def SegmentaçãoDeimagens(valores, path):
    database_file = os.path.dirname(__file__)+"/illuminants/data-base/images/"
    segmented_dir = os.path.dirname(__file__) + "/illuminants/data-base/segmented/"
    #os.system("rm -f " + segmented_dir + "*")
    copiarImagemDatabase(path)

    if valores[0] == "Illu":
        application_dir = os.path.dirname(__file__)+"/illuminants/illuminants/build/bin/"
        string = "python "+os.path.dirname(__file__) + "/illuminants/sourcecode/segmentAllImagesForIlluminantMethod.py "+database_file+" "+segmented_dir+" "+application_dir
        print(string)
        os.system(string)
    #extrairGGE(os.path.dirname(__file__))




def copiarImagemDatabase(path):
    database_dir = os.path.dirname(__file__)
    database_dir += "/illuminants/data-base/images/"
    os.system("rm -f "+database_dir+"*")
    shutil.copy2(path, database_dir)
    resposta=("imagem copiada de %s para %s", path, database_dir)


def extrairIIC():
        #script_file = os.path.dirname(__file__) + "/illuminants/sourcecode/./extractIICMaps.py"
        #print(script_file)
        #os.system(script_file)
    extractIlluminantMaps(os.path.dirname(__file__),"segmented","IIC")


def extrairGGE():
    #script_file = os.path.dirname(__file__) + "/illuminants/sourcecode/./extractGGEMaps.py"
    #print(script_file)
    #os.system(script_file)
    extractNewGrayWorldMaps(os.path.dirname(__file__), "segmented", "GGE", 1, 1, 3)


def extrairDescritores(descritor):
    if descritor == "TODOS":
        print(descritor)
        todos = ["acc", "bic", "ccv", "eoac", "las", "lch", "sasi", "spytec", "unser"]
        for descriptor in todos:
            script_file = os.path.dirname(__file__) + "/descriptors/" + descriptor + "/source/app/./extractGGEMaps.py"
            print(script_file)
            os.system(script_file)


    if descritor == "acc" or "bic" or "ccv" or "eoac" or "las" or "lch" or "sasi" or "spytec" or "unser":
        print(descritor)
        script_file = os.path.dirname(__file__) + "/descriptors/"+descritor+"/source/app"
        print(script_file)
        os.system(script_file)


def gerarTXTcomFacePositions(self, listadefaces):
    return 0

def apagarArquivos(caminhoImageTrabalho, caminhoImagensSegmentadas, caminhosArquivosTXT):
    return 0
