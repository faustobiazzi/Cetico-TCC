import sys
import os
from subprocess import *


config = "config.txt"

# Extract IlluminantMaps from all images
# IN: 		scale -- image scale folder
#		configFile -- illuminants config parameters file
# OUT: illuminant maps


def extractIlluminantMaps(sourcefolder, segmentedfolder, outputfolder):
    IIC_folder = sourcefolder + "/illuminants/data-base/"+outputfolder
    #command = "rm ../data-base/IIC/*.png"
    command = "rm -f " + IIC_folder + "/*"
    os.system(command)

    #im = os.listdir("../data-base/" + str(segmentedfolder) + "/")
    im = os.listdir(sourcefolder + "/illuminants/data-base/"+segmentedfolder+"/")
    for i in im:
        try:
            command = sourcefolder+"/illuminants/illuminants/build/bin/./vole liebv --img.image " + str(sourcefolder) + "/illuminants/data-base/images/" + i + " -S " +  str(sourcefolder) +"/illuminants/data-base/" + str(segmentedfolder) + "/" + i + " -O " + IIC_folder + "/" + i[:-4] + "_fhs.png --iebv_config "+sourcefolder+"/illuminants/illuminants/build/bin/" + config
            os.system(command)
            #print(command)
        except:
            print("Erro ao processar imagem ",i,"\n")

#extractIlluminantMaps("images","segmented","IIC")

