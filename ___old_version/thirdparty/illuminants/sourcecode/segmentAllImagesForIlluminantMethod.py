
from subprocess import *
import os
import sys

max_intensity=0.98823529411764705882
min_intensity=.05882352941176470588


def segmentAllImagesForIlluminantMethod(database, segmentedDBOutput, vole_dir, sigma,k,min_size, maxintensity, minintensity):
    
    command = "rm -f " + segmentedDBOutput + "*"
    os.system(command)
    im = database
    for i in os.listdir(im):
        print(str(i))
        try:
            tt = i.split(".")
            newname = i

            if tt[1] != "png":
                cmd = "convert " + str(database) + "" + i + " " + str(database) + "" + tt[0] + ".png"
                os.system(cmd)
                newname = tt[0] + ".png"
            application_dir = vole_dir

            command = application_dir+"./vole felzenszwalb -I " + str(database) + "" + newname + " --deterministic_coloring -O " + str(segmentedDBOutput)+ "" + newname + " --sigma " + str(sigma) + " --k " + str(k) + " --min_size " + str(min_size) + " --max_intensity " + str(maxintensity) + " --min_intensity " + str(minintensity)
            print(command)
            os.system(command)
        except:
            # print("Erro ao processar imagem ",targetImage,"\n")
            print("Erro ao processar imagem \n")


param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]

# segmentAllImagesForIlluminantMethod("images","segmented",0.2,300,15,max_intensity,min_intensity)
segmentAllImagesForIlluminantMethod(param1,param2, param3, 0.2, 300, 15, max_intensity, min_intensity)