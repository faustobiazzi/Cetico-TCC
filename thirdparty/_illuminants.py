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


programa = "Cético"
Modulo = "Illuminants"


def SegmentaçãoDeimagens(path):

    database_file = os.path.dirname(__file__)+"/illuminants/data-base/images/"
    segmented_dir = os.path.dirname(__file__) + "/illuminants/data-base/segmented/"
    os.system("rm -f " + segmented_dir + "*")

    copiarImagemDatabase(path)

    #script_file = "." + os.path.dirname(__file__) + "/illuminants/sourcecode/segmentAllImagesForIlluminantMethod.py"
    #os.system(script_file)


    application_dir = os.path.dirname(__file__)+"/illuminants/illuminants/build/bin/"
    string = application_dir + "./vole felzenszwalb -I " + path + " --deterministic_coloring -O " + segmented_dir + "file.png --k 200 --max_intensity 255"
    print(string)
    os.system(string)


def copiarImagemDatabase(path):
    database_dir = os.path.dirname(__file__)
    database_dir += "/illuminants/data-base/images/"
    os.system("rm -f "+database_dir+"*")
    shutil.copy2(path, database_dir)
    resposta=("imagem copiada de %s para %s", path, database_dir)


def extrairIIC():
    try:
        script_file = os.path.dirname(__file__) + "/illuminants/sourcecode/./extractIICMaps.py"
        print(script_file)
        os.system(script_file)
    except:
        pass


def extrairGGE():
    try:
        script_file = os.path.dirname(__file__) + "/illuminants/sourcecode/./extractGGEMaps.py"

        print(script_file)
        os.system(script_file)
    except:
        pass

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
