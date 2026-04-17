import sys
import os
import cv2
from subprocess import *

# Extract an specific descriptor from one image (Ex. SASI, BIC, etc)
# IN:
#   fileName -- image file name
#	descriptor -- descriptor name
#   space -- image color space
#   channel -- image color channel where descriptor will be extracted
#
# OUT:
#   a text file containing descriptor values


def extractDescriptor(folder, fileName, descriptor,space,channel):
    print (folder)
    print("entrou em extractDescriptor")


    descriptorName = fileName[:-4] + "-" + descriptor + "-descriptor.txt"
    print(descriptorName)
    nameSpace = ""
    nname = fileName

    newName = nname[:-3] + "ppm"
    print(newName)
    sourceImg = cv2.imread(fileName)
    if space == 0:
        destImg = cv2.cvtColor(sourceImg, cv2.COLOR_BGR2HSV)
    elif space == 1:
        destImg = cv2.cvtColor(sourceImg, cv2.COLOR_BGR2RGB)
    elif space == 2:
        destImg = cv2.cvtColor(sourceImg, cv2.COLOR_BGR2YCR_CB)
    elif space == 4:
        destImg = cv2.cvtColor(sourceImg, cv2.COLOR_BGR2LAB)
    else:
        destImg = sourceImg
    print("passou if elses")
    cv2.imwrite(nname, destImg)

    command = "convert " + nname + " " + newName
    os.system(command)
    print(command)
    command = "rm " + fileName
    os.system(command)
    print(command)
    upperDesc = descriptor.upper()
    if (upperDesc == "ACC") or (upperDesc == "BIC") or (upperDesc == "LCH") or (upperDesc == "CCV"):
        command = folder+"/illuminants/descriptors/" + descriptor + "/source/bin/./" + descriptor + "_extraction " + newName + " " + descriptorName
        print(command)
    else:
        command = folder+"/illuminants/descriptors/" + descriptor + "/source/bin/./" + descriptor + "_extraction " + newName + " " + descriptorName + " " + str(channel)
        print(command)
    os.system(command)

