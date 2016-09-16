# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:51:18 2016
Modified on Sun Sep 18 08:42:55 2016
@author: Fausto Biazzi de Sousa
programa = "Cético"
versão = "Alpha 0.0.0.5"

"""

import shutil
import platform
import os
from thirdparty.illuminants.sourcecode.extractGGEMaps import extractNewGrayWorldMaps
from thirdparty.illuminants.sourcecode.extractIICMaps import extractIlluminantMaps
from thirdparty.illuminants.sourcecode.extractAllFeatureVectors import main as extractAllFeatureVectors
from thirdparty.illuminants.sourcecode.classifySVMCetico import fullClassification
programa = "Cético"
Modulo = "Illuminants"


def SegmentacaoDeimagens(path):
    database_file = os.path.dirname(__file__)+"/illuminants/data-base/images/"
    segmented_dir = os.path.dirname(__file__) + "/illuminants/data-base/segmented/"
    #os.system("rm -f " + segmented_dir + "*")
    copiarImagemDatabase(path)

    application_dir = os.path.dirname(__file__)+"/illuminants/illuminants/build/bin/"
    string = "python "+os.path.dirname(__file__) + "/illuminants/sourcecode/segmentAllImagesForIlluminantMethod.py "+database_file+" "+segmented_dir+" "+application_dir
    os.system(string)

def copiarImagemDatabase(path):
    database_dir = os.path.dirname(__file__)
    database_dir += "/illuminants/data-base/images/"
    os.system("rm -f "+database_dir+"*")
    shutil.copy2(path, database_dir)


def extrairIIC():
    extractIlluminantMaps(os.path.dirname(__file__),"segmented","IIC")


def extrairGGE():
    extractNewGrayWorldMaps(os.path.dirname(__file__), "segmented", "GGE", 1, 1, 3)


def gerarTXTcomFacePositions(listadefaces):
    print("gerando arquivo facepositions:\n")
    sourcefolder = os.path.dirname(__file__)
    filedir = sourcefolder + "/illuminants/face-positions/"
    command = "rm -f " + filedir+ "*"
    os.system(command)
    im = os.listdir(sourcefolder+"/illuminants/data-base/segmented/")

    def convertervaloreslista():
        posFaces = ""
        ID = 0
        for vetor in listadefaces:
            ID += 1
            # ordem dos vetores armazenados([x0, y0, w1, h1])
            xtopleft = int(vetor[0])
            ytopleft = int(vetor[1])
            xbottomright = int(vetor[2])+int(vetor[0])
            ybottomright = int(vetor[3])+int(vetor[1])
            posFaces += (str(ID)+"\tLABEL"+str(ID)+"\t"+str(xtopleft)+"\t"+str(xbottomright)+"\t"+str(ytopleft)+"\t"+str(ybottomright))+"\n"

        return posFaces
    for i in im:
        tt = i.split(".")
        nome_arquivo = tt[0] + ".txt"
        arquivo = open(filedir+nome_arquivo, "w")
        print(nome_arquivo)
        type(arquivo)
        conteudoArquivo = convertervaloreslista()
        print(conteudoArquivo)
        arquivo.write(conteudoArquivo)
        arquivo.close()
    return 0


def extrairFeaturesVector(descritores):
    folder = os.path.dirname(__file__)
    extractAllFeatureVectors(descritores, folder)

def limparPastasTemporarias():
    sourcefolder = os.path.dirname(__file__)
    # limpar pasta temp faces
    filedir = sourcefolder + "/temp/faces/"
    command = "rm -f " + filedir + "*"
    os.system(command)
    # limpar pasta temp vectors
    filedir = sourcefolder + "/illuminants/temp/vectors/"
    command = "rm -f " + filedir + "*"
    os.system(command)

def limparTudo():
    # limpa pasta face-positions"
    sourcefolder = os.path.dirname(__file__)
    filedir = sourcefolder + "/illuminants/face-positions/"
    command = "rm -f " + filedir+ "*"
    # limpa pasta data-base/images/
    os.system(command)
    filedir = sourcefolder + "/illuminants/data-base/images/"
    command = "rm -f " + filedir+ "*"
    os.system(command)
    # limpa pasta data-base/GGE/
    os.system(command)
    filedir = sourcefolder + "/illuminants/data-base/GGE/"
    command = "rm -f " + filedir+ "*"
    os.system(command)
    # limpa pasta data-base/IIC/
    os.system(command)
    filedir = sourcefolder + "/illuminants/data-base/IIC/"
    command = "rm -f " + filedir+ "*"
    os.system(command)
    # limpa pasta data-base/segmented/
    os.system(command)
    filedir = sourcefolder + "/illuminants/data-base/segmented/"
    command = "rm -f " + filedir+ "*"
    os.system(command)
    # limpa pasta data-base/faces/
    os.system(command)
    # limpar pasta extracted-feature-vectors
    filedir = sourcefolder + "/illuminants/extracted-feature-vectors/"
    command = "rm -rf " + filedir + "*"
    os.system(command)
    limparPastasTemporarias()



def classificadorSVMCetico(descritores):
    baseDir =os.path.dirname(__file__)
    imgDir = baseDir+"/illuminants/data-base/images/"
    im = os.listdir(imgDir)
    for i in im:
        print (i)
        tt = i.split(".")
        imagem = tt[0] + ".png"
    resultadoSVM = fullClassification(baseDir, descritores, imagem)
    return resultadoSVM