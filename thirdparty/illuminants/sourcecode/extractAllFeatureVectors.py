import os
import sys
from thirdparty.illuminants.sourcecode import composeFinalFeatureVector
from subprocess import *
from thirdparty.illuminants.sourcecode import getSpaceChannelName as sc


#channel values are associated like that: first channel is higher, middle channel is midle value, last channel is smaller( Ex. R = 2, G = 1, B = 0)
#space 0 HSV
#space 1 RGB
#space 2 Ycbcr
#space 4 Lab

def extractAllFeatureVectors(folder,descriptor,space,channel):
    print(str(descriptor))
    path = folder+"/illuminants/data-base/images/"
    print(path)
    dirList = os.listdir(path)
    dirList.sort()
    nameSpace,nameChannel = sc.getSpaceChannelName(space, channel)
    print(str(nameSpace))
    print(str(nameChannel))
    tt = descriptor.upper()
    npath = folder+"/illuminants/extracted-feature-vectors/" + tt + "-" + "IIC-" + nameSpace + "-" + nameChannel+"/"
    print(npath)
    if not os.path.exists(npath):
        os.makedirs(npath)
    print("\n..........................Processing IIC Maps..........................\n")
    for fname in dirList:
        try:
            print (str(fname))
            img = fname[:-3] + "png"
            print("\nExtracting feature vector from image ",img)
            faces = composeFinalFeatureVector.composeFinalFeatureVector(folder, img, descriptor, space, channel, "IIC")
            name = folder+"/illuminants/temp/vectors/fv-" + img[:-3] + "txt"
            command = "cp " + name + " " + npath + "/"
            os.system(command)
            command = "rm "+folder+"/illuminants/data-base/faces/*.ppm"
            os.system(command)
            command = "rm "+folder+"/illuminants/temp/faces/*"
            os.system(command)
            command = "rm "+folder+"/illuminants/temp/vectors/*"
            os.system(command)
        except:
            print("Erro to process image ", fname)



    npath = ""+folder+"/illuminants/extracted-feature-vectors/" + tt + "-" + "GGE-" + nameSpace + "-" + nameChannel
    if not os.path.exists(npath):
        os.makedirs(npath)

    print("\n..........................Processing GGE Maps..........................\n")
    for fname in dirList:
        try:
            img = fname[:-3] + "png"
            print("\nExtracting feature vectors from image ",img)
            faces = composeFinalFeatureVector.composeFinalFeatureVector(folder,img,descriptor,space,channel,"GGE")

            name = folder + "/illuminants/temp/vectors/fv-" + img[:-3] + "txt"
            command = "cp " + name + " " + npath + "/"
            print("CP em extract ALL featuresVectors "+command)
            os.system(command)
            teste = "rm  "+str(folder)+"/illuminants/data-base/faces/*.ppm"
            print(command)
            command = teste
            os.system(command)
            command = "rm  "+str(folder)+"/illuminants/temp/faces/*"
            os.system(command)
            print(command)
            command = "rm  "+str(folder)+"/illuminants/temp/vectors/*"
            os.system(command)
            print(command)
            print(folder)
        except:
            print("Erro to process image ", fname)


def main(desc, folder):

    command = "rm " + folder + "/illuminants/data-base/images/*.jpg"
    os.system(command)
    command = "rm " + folder + "/illuminants/data-base/images/*.jpeg"
    os.system(command)
    #if (len(sys.argv) != 2):
     #   print("Number of parameters invalid! extractAllFeatureVectors.py <string with descriptors names separed by space>")
  #  else:
        #desc = sys.argv[1].split(" ")
    for i in desc:
        try:
            tt = i.upper()
            if (tt == "ACC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing ACC Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"acc",4,3)
                extractAllFeatureVectors(folder,"acc",1,3)
                extractAllFeatureVectors(folder,"acc",2,3)
            elif (tt == "BIC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing BIC Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"bic",4,3)
                extractAllFeatureVectors(folder,"bic",1,3)
                extractAllFeatureVectors(folder,"bic",2,3)
            elif (tt == "CCV"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing CCV Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"ccv",4,3)
                extractAllFeatureVectors(folder,"ccv",1,3)
                extractAllFeatureVectors(folder,"ccv",2,3)
            elif (tt == "LCH"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing LCH Color Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"lch",4,3)
                extractAllFeatureVectors(folder,"lch",1,3)
                extractAllFeatureVectors(folder,"lch",2,3)
            elif (tt == "SASI"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing SASI Texture Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"sasi",4,2)
                extractAllFeatureVectors(folder,"sasi",0,0)
                extractAllFeatureVectors(folder,"sasi",2,2)
            elif (tt == "LAS"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing LAS Texture Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"las",4,2)
                extractAllFeatureVectors(folder,"las",0,0)
                extractAllFeatureVectors(folder,"las",2,2)
            elif (tt == "UNSER"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing UNSER Texture Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"unser",4,2)
                extractAllFeatureVectors(folder,"unser",0,0)
                extractAllFeatureVectors(folder,"unser",2,2)
            elif (tt == "EOAC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing EOAC Shape Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"eoac",4,2)
                extractAllFeatureVectors(folder,"eoac",0,0)
                extractAllFeatureVectors(folder,"eoac",2,2)
            elif (tt == "SPYTEC"):
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>> Processing SPYTEC Shape Descriptor <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n")
                extractAllFeatureVectors(folder,"spytec",4,2)
                extractAllFeatureVectors(folder,"spytec",0,0)
                extractAllFeatureVectors(folder,"spytec",2,2)
            else:
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>> Image Descriptor %s not available! <<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n " %tt)
        except ValueError:
            print("Image Descriptor needs to be a valid string")



if __name__ == "__main__":
    main()