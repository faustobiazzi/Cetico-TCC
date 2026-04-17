import os
from subprocess import *

# Extract GrayWorldMaps from all images
# IN: 		scale -- image scale folder
#		sigma -- gray-world parameters
#	            n -- gray-world parameters
#	     	    p -- gray-world parameters
# OUT: gray-world maps

def extractNewGrayWorldMaps(sourcefolder, segmentedfolder, outputfolder, sigma,n,p):
    GGE_folder = sourcefolder+"/illuminants/data-base/GGE/"
    command = "rm -f "+GGE_folder+"*"
    os.system(command)
    im = os.listdir(sourcefolder+"/illuminants/data-base/segmented/")

    for i in im:
        try:
            command = sourcefolder+"/illuminants/illuminants/build/bin/./vole lgrayworld --img.image " + str(sourcefolder) + "/illuminants/data-base/images/" + i + " -S " + sourcefolder+"/illuminants/data-base/" + str(segmentedfolder) + "/" + i + " -O " + str(sourcefolder) +"/illuminants/data-base/"+ str(outputfolder) + "/" + i[:-4] + "_fhs.png --n " +  str(n) + " --p " + str(p) + " --sigma " + str(sigma)
            print(command)
            os.system(command)
        except:
            print ("Erro ao processar imagem ",i,"\n")

#extractNewGrayWorldMaps("images","segmented","GGE",1,1,3)
