
import thirdparty.illuminants.sourcecode.segmentImage as segmentImage
import thirdparty.illuminants.sourcecode.extractDescriptor as extractDescriptor
import os
import time
import shutil

# Build face's pairs of descriptors
# IN:
#   image -- image name to extract descriptor
#   descriptor -- descriptor name
# 	space -- image color space
#   channel -- image color channel where descriptor will be extracted
#   illuminantType -- IIC or GGE
#
# OUT:
#   all possible combination of faces pairs for a given image


def composeFinalFeatureVector(basefolder, image, descriptor="ACC", space=4, channel=3, illuminantType="GGE"):
#def composeFinalFeatureVector(basefolder, image, descriptor, space, channel, illuminantType):
    print ("entrou em composeFinalFeatureVector")
    print ("valores de entrada na função folder= "+basefolder+" imagem= "+str(image)+" descritor="+str(descriptor)+" space"+str(space)+"channel"+str(channel)+"illuminanttype"+str(illuminantType))
    numberFaces = segmentImage.segmentImage(basefolder, image, illuminantType)
    print ("numberfaces recebeu "+str(numberFaces))
    cont = 1
    nameFaces = ""
    print("Number of faces: %d\nCharacterizing faces..." %numberFaces)
    while (cont <= numberFaces):
        faceName = basefolder+"/illuminants/data-base/faces/face-" + str(cont) + ".png"
        print ("facename dentro do primeiro while (linha29)"+str(faceName))
        extractDescriptor.extractDescriptor(basefolder, faceName,descriptor, space, channel)
        cont = cont + 1
        nameFaces = basefolder+"/illuminants/face-positions/" + image[:-4] + ".txt"
        print (str(nameFaces))
    print(nameFaces)
    facesFile = open(nameFaces, "rt")
    lines = facesFile.readlines()
    facesFile.close()
    firstFace = 1
    contVectors = 0
    # Inherent loops compose a descriptor for each pair of faces at the image
    allVectors = []
    descriptor = descriptor.lower()
    print("Composing features vectors for faces pairs...")
    while (firstFace < numberFaces):
        print("ENTROU NO WHILE DE FIRSTFACE<NUMBERFACE")
        secondFace = firstFace + 1
        lineFace1 = lines[(firstFace - 1)].split("\t")
        stateFace1 = lineFace1[1]
        while (secondFace <= numberFaces):
            contVectors = contVectors + 1
            newVector = []
            # Label 1 point a pristine pair and label -1 point a pair that contains at least one fake image
            label = 1
            lineFace2 = lines[(secondFace - 1)].split("\t")
            stateFace2 = lineFace2[1]
            if ((stateFace1 != "NORMAL") or (stateFace2 != "NORMAL")):
                label = -1
            newVector.append(label)
            if (descriptor == "acc"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-acc-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-acc-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = list(i)
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rb")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = list(i)
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "bic"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-bic-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-bic-descriptor.txt"
                files = open(nf1,"rb")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = list(i)
                    cont = 0
                    totalFeat = len(desc)
                    while (cont < (totalFeat - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = list(i)
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "las"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-las-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-las-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "sasi"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-sasi-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-sasi-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "unser"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-unser-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-unser-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "spytec"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-spytec-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-spytec-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "ccv"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-ccv-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-ccv-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split("\n")
                    cont = 0
                    newVector.append(float(desc[0]))
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split("\n")
                    cont = 0
                    newVector.append(float(desc[0]))
            elif (descriptor == "lch"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-lch-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-lch-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            elif (descriptor == "eoac"):
                nf1 = basefolder+"/illuminants/temp/faces/face-" + str(firstFace) + "-eoac-descriptor.txt"
                nf2 = basefolder+"/illuminants/temp/faces/face-" + str(secondFace) + "-eoac-descriptor.txt"
                files = open(nf1,"rt")
                files.seek(0)
                temp = files.readline()
                linesf1 = files.readlines()
                files.close()
                for i in linesf1:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
                files = open(nf2,"rt")
                files.seek(0)
                temp = files.readline()
                linesf2 = files.readlines()
                files.close()
                for i in linesf2:
                    desc = i.split(" ")
                    cont = 0
                    while (cont < (len(desc) - 1)):
                        newVector.append(float(desc[cont]))
                        cont = cont + 1
            nnf1 = basefolder+"/illuminants/temp/faces/" + image[:-4] + "-" + nf1[14:-4] + "-label-" + str(stateFace1) + ".txt"
            #command = "cp " + nf1 + " " + nnf1
            shutil.copy2(nf1, nnf1)
            print("comando de cópia 1 em FinalFeatureVector")
            #os.system(command)
            nnf2 = basefolder+"/illuminants/temp/faces/" + image[:-4] + "-" + nf2[14:-4] + "-label-" + str(stateFace2) + ".txt"
            #command = "cp " + nf2 + " " + nnf2
            shutil.copy2(nf2, nnf2)
            print("comando de cópia 2 em FinalFeatureVector")
            #os.system(command)
            allVectors.append(newVector)
            secondFace = secondFace + 1
        firstFace = firstFace + 1
        nameFile = basefolder+"/illuminants/temp/vectors/fv-" + image[:-4] + ".txt"
        files = open(nameFile,"wt")
        files.seek(0)
        for i in allVectors:
            temp = i
            cont = 0
            for j in temp:
                if (cont == 0):
                    frase = str(j) + " "
                    files.write(frase)
                else:
                    frase = str(cont) + ":" + str(j) + " "
                    files.write(frase)
                cont = cont + 1
            files.write("\n")
        files.close()
    return numberFaces

# composeFinalFeatureVector("splicing-01.png")
