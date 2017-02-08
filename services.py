# -*- coding: utf-8 -*-
"""
Modified on Sun Sep 18 08:42:55 2016
@author: Fausto Biazzi de Sousa
@modulo: funções do aplicativo (pseudo interface)
@programa: "Cético"

"""

#sub-sistemas
from error import *
from data.facedetector.detectaface import *
from data.homography import homography
from data.imageproperties.readMetadata import *
from data.reportgenerator import reportgen
from data.thumbnailreader import thumbviewer
from thirdparty._illuminants import *


def clrthumbs():
    thumbviewer.clearthumbs()


def thumbvwr(imagePath,size,rotation):
    try:
        ret = thumbviewer.tviewer(imagePath,size,rotation)
        return ret
    except:
        pass

def reportgenerator(filelocation, pagesize, margin, data):
    reportgen.dataparser(filelocation,pagesize, margin,  data)


def findFaces(imagePath, values):
    try:
        face = detectFaces(imagePath, values)
        return face
    except:
        erro_RetornoGenerico()


def propriedadesImagem(parametro, imagepath):
   if parametro == "Nodecoded":
        ret = nodecoded(imagepath)
        return ret

   if parametro == "Full":
        ret = full(imagepath)
        return ret
   elif parametro == "Simple":
        ret = exiftaged(imagepath)
        return ret
   else:
        ret = tag(imagepath, parametro)
        return ret


def homografia(file, pto, ptd):
    try:
        result = homography(file, pto, ptd)
        return result
    except:
        return 0

    
def Moduloilluminant(operacao, imagePath, vetorDeFaces):
    if platform.system() == 'Windows':
        funcaoIndisponivel(platform.system())
        print(platform.system())
    else:
        print("iniciando módulo illuminants")
        limparTudo()
        print("Pastas limpas")
        SegmentacaoDeimagens(imagePath)
        print("Imagem Segmentada")
        extrairGGE()
        print("Extraído GGE")
        extrairIIC()
        print("Extraído IIC")
        gerarTXTcomFacePositions(vetorDeFaces)
        print("Gerada posições de faces")
        extrairFeaturesVector(operacao)
        print("Vetores extraídos")
        limparPastasTemporarias()
        print("Limpando pastas temporárias")
        resultado =classificadorSVMCetico(operacao)
        print("Concluida analise SVM")
        analiseIlluminantsterminada()

        outClassification, votesNormal, votesFake, finalClass = resultado
        resultlog = ""
        resultlog += ("Illuminant-based Transformed Spaces for Image Forensics - RESULT]\nParameters analysed:\n")
        for i in outClassification:
            resultlog += ("\t %s\n" % str(i))
        resultlog += ("Normal Votes: %s \n" % str(votesNormal))
        resultlog += ("Modified Votes: %s \n" % str(votesFake))
        resultlog += ("Final Classification: %s" % finalClass)
        text_file = open("Illuminants.log", "w")
        text_file.write(resultlog)
        text_file.close()

    return resultado

