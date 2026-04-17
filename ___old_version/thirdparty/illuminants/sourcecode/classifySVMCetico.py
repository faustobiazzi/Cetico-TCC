import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV
#import getSpaceChannelName as sc
from thirdparty.illuminants.sourcecode.getSpaceChannelName import getSpaceChannelName as sc

def readTrainingTestFiles(outfile):
    try:
        ofid = open(outfile, 'rt')
        ofid.seek(0)
        lines = ofid.readlines()
        ofid.close()
        features = []
        labels = []
        for i in lines:
            label = 0
            tmp = i[:-3].split(" ")
            row = []
            for j in tmp:
                if (label != 0):
                    tmp2 = j.split(":")
                    row.append(tmp2[1])
                else:
                    label = j
                    labels.append(j)
            features.append(row)
        return (features, labels)

    except:
        pass


def svmTestBySample(basedir, imgName,descriptor,space,channel,illuminant="IIC"):
    nameSpace,nameChannel = sc(space,channel)
    tt = descriptor.upper()
    outfile = basedir+"/illuminants/extracted-feature-vectors/" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + "/fv-" + imgName[:-4] + ".txt"
    try:
        ft,lb = readTrainingTestFiles(outfile)
        testMatrixF = np.array(ft)
        testMatrixL = np.array(lb)

        # Scale Train Features
        # testMatrixFScaled = preprocessing.scale(testMatrixF)

        # Scale features between [-1,1]
        max_abs_scaler = preprocessing.MaxAbsScaler()
        testMatrixFScaled = max_abs_scaler.fit_transform(testMatrixF)

        npath = basedir + "/illuminants/models/" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + "/"
        modelName = npath + "model-DSO-" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + ".pkl"
        clf = joblib.load(modelName)
        outLabels = clf.predict(testMatrixFScaled)
        scores = clf.score(testMatrixFScaled, testMatrixL)
        return (outLabels, scores)
        # print(outLabels,scores)

    except:
        pass




def svmTestByImage(basedir, imgName,descriptor,space,channel,illuminant="IIC"):
    nameSpace,nameChannel = sc(space,channel)
    tt = descriptor.upper()
    outfile = basedir+"/illuminants/extracted-feature-vectors/" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + "/fv-" + imgName[:-4] + ".txt"
    try:
        outLabels,scores = svmTestBySample(basedir,imgName,descriptor,space,channel,illuminant)
        labelsDefault,imageLables = readTrainingTestFiles(outfile)
        imageClass = 1
        for i in outLabels:
            if i == '-1':
                imageClass = -1
        return imageClass
    except:
        print("erro")
        pass



def fullClassification(basedir,desc, imgName):
    listOfParams = []
    classifiersFake = []
    classifiersNormal = []
    for i in desc:
        if i == "acc":
            listOfParams += [("acc",4,3,"IIC"), ("acc",1,3,"IIC"), ("acc",2,3,"IIC"), ("acc",4,3,"GGE"), ("acc",1,3,"GGE"), ("acc",2,3,"GGE")]
        elif i == "ccv":
            listOfParams += [("ccv",4,3,"IIC"), ("ccv",1,3,"IIC"), ("ccv",2,3,"IIC"), ("ccv",4,3,"GGE"), ("ccv",1,3,"GGE"), ("ccv",2,3,"GGE")]
        elif i == "bic":
            listOfParams += [("bic",4,3,"IIC"), ("bic",1,3,"IIC"), ("bic",2,3,"IIC"), ("bic",4,3,"GGE"), ("bic",1,3,"GGE"), ("bic",2,3,"GGE")]

        elif i == "lch":
            listOfParams += [("lch",4,3,"IIC"), ("lch",1,3,"IIC"), ("lch",2,3,"IIC"), ("lch",4,3,"GGE"), ("lch",1,3,"GGE"), ("lch",2,3,"GGE")]

        elif i == "sasi":
            listOfParams += [("sasi",4,2,"IIC"), ("sasi",0,0,"IIC"), ("sasi",2,2,"IIC"), ("sasi",4,2,"GGE"), ("sasi",0,0,"GGE"), ("sasi",2,2,"GGE")]

        elif i == "las":
            listOfParams += [("las",4,2,"IIC"), ("las",0,0,"IIC"), ("las",2,2,"IIC"), ("las",4,2,"GGE"), ("las",0,0,"GGE"), ("las",2,2,"GGE")]

        elif i == "unser":
            listOfParams += [("unser",4,2,"IIC"), ("unser",0,0,"IIC"), ("unser",2,2,"IIC"), ("unser",4,2,"GGE"), ("unser",0,0,"GGE"), ("unser",2,2,"GGE")]

        elif i == "eoac":
            listOfParams += [("eoac",4,2,"IIC"), ("eoac",0,0,"IIC"), ("eoac",2,2,"IIC"), ("eoac",4,2,"GGE"), ("eoac",0,0,"GGE"), ("eoac",2,2,"GGE")]

        elif i == "spytec":
            listOfParams += [("spytec",4,2,"IIC"), ("spytec",0,0,"IIC"), ("spytec",2,2,"IIC"), ("spytec",4,2,"GGE"), ("spytec",0,0,"GGE"), ("spytec",2,2,"GGE")]

        else:
            listOfParams = [("acc",4,3,"IIC"), ("acc",1,3,"IIC"), ("acc",2,3,"IIC"), ("acc",4,3,"GGE"), ("acc",1,3,"GGE"), ("acc",2,3,"GGE"), ("ccv",4,3,"IIC"), ("ccv",1,3,"IIC"), ("ccv",2,3,"IIC"), ("ccv",4,3,"GGE"), ("ccv",1,3,"GGE"), ("ccv",2,3,"GGE"), ("bic",4,3,"IIC"), ("bic",1,3,"IIC"), ("bic",2,3,"IIC"), ("bic",4,3,"GGE"), ("bic",1,3,"GGE"), ("bic",2,3,"GGE"), ("lch",4,3,"IIC"), ("lch",1,3,"IIC"), ("lch",2,3,"IIC"), ("lch",4,3,"GGE"), ("lch",1,3,"GGE"), ("lch",2,3,"GGE"),("sasi",4,2,"IIC"), ("sasi",0,0,"IIC"), ("sasi",2,2,"IIC"), ("sasi",4,2,"GGE"), ("sasi",0,0,"GGE"), ("sasi",2,2,"GGE"), ("las",4,2,"IIC"), ("las",0,0,"IIC"), ("las",2,2,"IIC"), ("las",4,2,"GGE"), ("las",0,0,"GGE"), ("las",2,2,"GGE"), ("unser",4,2,"IIC"), ("unser",0,0,"IIC"), ("unser",2,2,"IIC"), ("unser",4,2,"GGE"), ("unser",0,0,"GGE"), ("unser",2,2,"GGE"), ("eoac",4,2,"IIC"), ("eoac",0,0,"IIC"), ("eoac",2,2,"IIC"), ("eoac",4,2,"GGE"), ("eoac",0,0,"GGE"), ("eoac",2,2,"GGE"), ("spytec",4,2,"IIC"), ("spytec",0,0,"IIC"), ("spytec",2,2,"IIC"), ("spytec",4,2,"GGE"), ("spytec",0,0,"GGE"), ("spytec",2,2,"GGE")]

    for i in listOfParams:
        print(str(i))

    outClassification = []
    finalClass = "Modificada"
    votesNormal = 0
    votesFake = 0

    for i in listOfParams:
        desc,space,channel,illumi = i
        classPredic = svmTestByImage(basedir,imgName,desc,space,channel,illumi)
        outClassification.append((desc,space,channel,illumi,classPredic))
        if (classPredic == 1):
            votesNormal += 1
        else:
            votesFake += 1
    if (votesNormal > votesFake):
        finalClass = "NORMAL"



    print("Votos Normal: %d\nVotos Fake: %d\nClassificacao Final: %s" %(votesNormal,votesFake,finalClass))
    return (outClassification, votesNormal, votesFake, finalClass)


#fullClassification("pessoas.png")