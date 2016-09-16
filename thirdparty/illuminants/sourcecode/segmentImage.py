import os
import cv2
from subprocess import *

# Crop faces from a given image
# IN:
#   fileName -- image name to crop faces
#   illuminantType -- IIC or GGE
# OUT:
#   the numbers of segmented faces in te image


def segmentImage(basefolder, fileName, illuminantType):
    print("Entrou em segmentImage")
    nameFaces = str(basefolder)+"/illuminants/face-positions/" + fileName[:-4] + ".txt"
    print("nameFaces recebeu = "+str(nameFaces))
    facesFile = open(nameFaces,"rt")
    print(str("faceFile recebeu "+str(facesFile)))
    lines = facesFile.readlines()
    facesFile.close()
    cont = 1
    numberOfFaces = 0
    print("Segmenting Faces...")
    for i in lines:
        temp = i.split("\t")
        if (len(temp) != 1):
            topleftx = int(temp[2])
            toplefty = int(temp[4])
            bottomrightx = int(temp[3])
            bottomrighty = int(temp[5])

            box = (topleftx, toplefty, bottomrightx, bottomrighty)
            print("box recebeu"+str(box))
            pathImage = str(basefolder)+"/illuminants/data-base/" + illuminantType + "/" + fileName[:-4] + "_fhs.png"
            print ("pathImage recebeu = "+ pathImage)
            im = cv2.imread(pathImage)
            region = im[toplefty:bottomrighty, topleftx:bottomrightx]
            nameFace = str(basefolder)+"/illuminants/temp/faces/face-" + str(cont) + ".png"
            print("nameFace recebeu = "+str(nameFace))
            cv2.imwrite(nameFace, region)
            numberOfFaces = cont
            cont = cont + 1
    print("encerrou segmentimage.py")
    return numberOfFaces
