
# import sys, os
from tkinter import *


def vetoresRecebidos(faces):
    vetReceb = Tk()
    vetReceb.title("Coordenadas")
    teste = ''
    for f in faces:
        teste += ("{}\n".format(f))
    Label(vetReceb, text="Coordenadas recebidas: ").grid(row=0, sticky=W)
    Label(vetReceb, text=teste).grid(row=1, sticky=W)
    Button(vetReceb, text="Fechar", underline=0, command=vetReceb.destroy).grid(row=2, sticky=E)
    mainloop()

def janela(path, faces):
    definePropriedades = Tk()
    print("entrou na em illuminantes na função janela")
    definePropriedades.title("Illuminants -propriedades")

    Label(definePropriedades, text="Selecione os descritores desjados:").grid(row=0, sticky=W)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var0 = IntVar()

    Checkbutton(definePropriedades, text="ACC", variable=var1).grid(row=1, sticky=W)
    Checkbutton(definePropriedades, text="BIC", variable=var2).grid(row=2, sticky=W)
    Checkbutton(definePropriedades, text="CCV", variable=var3).grid(row=3, sticky=W)
    Checkbutton(definePropriedades, text="EOAC", variable=var4).grid(row=4, sticky=W)
    Checkbutton(definePropriedades, text="LAS", variable=var5).grid(row=5, sticky=W)
    Checkbutton(definePropriedades, text="LCH", variable=var6).grid(row=6, sticky=W)
    Checkbutton(definePropriedades, text="SASI", variable=var7).grid(row=7, sticky=W)
    Checkbutton(definePropriedades, text="SPYTEC", variable=var8).grid(row=8, sticky=W)
    Checkbutton(definePropriedades, text="UNSER", variable=var9).grid(row=9, sticky=W)


    # Para extrair descritor de imagens do illuminats maps (IIC e GGE) de todas as imagens na pasta
    # /database/images/ execute a função ./sourcecode/extractAllFeatureVectors.py <DS>
    #Onde DS é uma string que representa o descritor a ser extraido,
    # exemplo para o comand de TODOS os descritores

    Checkbutton(definePropriedades, text="TODOS", variable=var0).grid(row=11, sticky=W)

    #Button(definePropriedades, text="Executar", command=printCommando(var1, path, faces)).grid(row=12, sticky=E)

    vetoresRecebidos(faces)
    mainloop()


def printCommando(var, imagepath,faces):
    print(recebeImagemaSerAnalisada(imagepath, faces))
    return 0


def recebeImagemaSerAnalisada(imagepath, faces):
    #entrar em database imagens e inserir a imagem a ser analisada, remover imagens anteriores
    #executar a função /source-code/segmentAllImagesForIlluminantMethod.py
    print("dentro de +receber imagem + %s %s", imagepath, faces)

    return 'teste'


