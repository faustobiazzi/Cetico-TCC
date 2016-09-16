import os
import sys

from subprocess import *
#import composeFinalFeatureVector
#import getSpaceChannelName as sc

import thirdparty.illuminants.sourcecode.composeFinalFeatureVector as composeFinalFeatureVector
import thirdparty.illuminants.sourcecode.getSpaceChannelName as sc


# channel values are associated like that: first channel is higher, middle channel is midle value, last channel is smaller( Ex. R = 2, G = 1, B = 0)
# space 0 HSV
# space 1 RGB
# space 2 Ycbcr
# space 4 Lab

def extractAllFeatureVectors(folder, descriptor,space, channel):
    print("Entrou na extração")
    path = folder +"/illuminants/data-base/images/"
    dirList = os.listdir(path)
    dirList.sort()
    print(dirList)
    nameSpace, nameChannel = sc.getSpaceChannelName(space, channel)
    tt = descriptor.upper()
    npath = folder+"/illuminants/extracted-feature-vectors/" + tt + "-" + "IIC-" + nameSpace + "-" + nameChannel+"/"
    print(npath)
    if not os.path.exists(npath):
        print("entrou no ifnot")
        os.makedirs(npath)

    print("\n..........................Processing IIC Maps..........................\n")
    for fname in dirList:
        #try:
            print("entrou no try do icc maps")
            img = fname[:-3] + "png"
            print("img recebeu ="+str(img))
            print("\nExtracting feature vector from image", str(img))
            faces = composeFinalFeatureVector.composeFinalFeatureVector(folder, img, descriptor, space, channel, "IIC")
            print ("faces recebeu = "+str(faces))
            name = folder+"/temp/vectors/fv-" + img[:-3] + "txt"
            print ("name recebeu = "+str(name))
            command = "cp " + name + " " + npath
            print ("copiou "+name+" para "+ npath)
            os.system(command)
            command = "rm " + folder + "/illuminants/data-base/faces/*.ppm"
            print(command)
            os.system(command)
            command = "rm " + folder + "/illuminants/temp/faces/*"
            os.system(command)
            command = "rm " + folder + "/illuminants/temp/vectors/*"
            os.system(command)
        #except:
         #   print("Erro to process image ", fname)



    npath = folder+"/illuminants/extracted-feature-vectors/" + tt + "-" + "GGE-" + nameSpace + "-" + nameChannel
    if not os.path.exists(npath):
        os.makedirs(npath)

    print("\n..........................Processing GGE Maps..........................\n")
    for fname in dirList:
        try:
            img = fname[:-3] + "png"
            print("\nExtracting feature vectors from image ",img)
            faces = composeFinalFeatureVector.composeFinalFeatureVector(folder,img,descriptor,space,channel,"GGE")
            name = folder+"/illuminants/temp/vectors/fv-" + img[:-3] + "txt"
            command = "cp " + name + " " + npath
            os.system(command)
            command = "rm "+folder+"/illuminants/data-base/faces/*.ppm"
            os.system(command)
            command = "rm"+folder+"/illuminants/temp/faces/*"
            os.system(command)
            command = "rm"+folder+"/illuminants/temp/vectors/*"
            os.system(command)
        except:
            print("Erro to process image ", fname)


def main(desc, pastabase):
    pasta = str(pastabase)
    #if (len(sys.argv) != 2):
    #    print("Number of parameters invalid! extractAllFeatureVectors.py <string with descriptors names separed by space>")
    #else:
    #desc = sys.argv[1].split(" ")
    for i in desc:
        print("foram selecionados os seguintes descritores: "+str(desc))
        try:
            print("DESCRITOR SELECIONADO = " + i)
            tt = i.upper()
            if (tt == "ACC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing ACC Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"acc",4,3)
                extractAllFeatureVectors(pasta,"acc",1,3)
                extractAllFeatureVectors(pasta,"acc",2,3)
            elif (tt == "BIC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing BIC Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"bic",4,3)
                extractAllFeatureVectors(pasta,"bic",1,3)
                extractAllFeatureVectors(pasta,"bic",2,3)
            elif (tt == "CCV"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing CCV Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"ccv",4,3)
                extractAllFeatureVectors(pasta,"ccv",1,3)
                extractAllFeatureVectors(pasta,"ccv",2,3)
            elif (tt == "LCH"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing LCH Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"lch",4,3)
                extractAllFeatureVectors(pasta,"lch",1,3)
                extractAllFeatureVectors(pasta,"lch",2,3)
            elif (tt == "SASI"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing SASI Texture Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"sasi",4,2)
                extractAllFeatureVectors(pasta,"sasi",0,0)
                extractAllFeatureVectors(pasta,"sasi",2,2)
            elif (tt == "LAS"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing LAS Texture Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"las",4,2)
                extractAllFeatureVectors(pasta,"las",0,0)
                extractAllFeatureVectors(pasta,"las",2,2)
            elif (tt == "UNSER"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing UNSER Texture Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"unser",4,2)
                extractAllFeatureVectors(pasta,"unser",0,0)
                extractAllFeatureVectors(pasta,"unser",2,2)
            elif (tt == "EOAC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing EOAC Shape Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"eoac",4,2)
                extractAllFeatureVectors(pasta,"eoac",0,0)
                extractAllFeatureVectors(pasta,"eoac",2,2)
            elif (tt == "SPYTEC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing SPYTEC Shape Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(pasta,"spytec",4,2)
                extractAllFeatureVectors(pasta,"spytec",0,0)
                extractAllFeatureVectors(pasta,"spytec",2,2)
            else:
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>> Image Descriptor %s not available! <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n " %tt)
        except ValueError:
            print("Image Descriptor needs to be a valid string")

#if __name__ == "__main__":

    #path = "../data-base/images/"
    #dirList = os.listdir(path)
    #print("DIR"+str(dirList))
 #   a = ["acc", "ccv"]
  #  pasta = "/"
 #main(a, pasta)

