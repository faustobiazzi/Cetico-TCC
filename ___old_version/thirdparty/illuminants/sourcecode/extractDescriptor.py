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

def extractDescriptor(folder, fileName,descriptor,space,channel):

    descriptorName = "" + fileName[:-4] + "-" + descriptor + "-descriptor.txt"
    print ("extractDescriptor recebeu "+descriptorName)
    nameSpace = ""
    nname = fileName
    print(str(nname))
    newName = nname[:-3] + "ppm"
    print (str(newName))
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
    cv2.imwrite(nname,destImg)

    command = "convert " + nname + " " + newName
    os.system(command)
    command = "rm " + fileName
    os.system(command)

    upperDesc = descriptor.upper()
    if (upperDesc == "ACC") or (upperDesc == "BIC") or (upperDesc == "LCH") or (upperDesc == "CCV"):
        command = folder+"/illuminants/descriptors/" + descriptor + "/source/bin/./" + descriptor + "_extraction " + newName + " " + descriptorName
        print("Executou descritor ACC ou BIC ou LCH ou CCV")
    else:
        command = folder+"/illuminants/descriptors/" + descriptor + "/source/bin/./" + descriptor + "_extraction " + newName + " " + descriptorName + " " + str(channel)
        print("Executou descritor outros descritores")
    os.system(command)

