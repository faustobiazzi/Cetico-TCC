import sys, os
from tkinter import *


def vetoresRecebidos(faces):
    vetReceb = Tk()
    vetReceb.title("Illuminants -vetores")
    teste2 = ''
    for f in faces:
        teste = ("{}\n".format(f))
        teste2 += teste
        print("teste")
    label2 = Label(vetReceb, text=teste2)
    label2.pack()
    button = Button(vetReceb, text="Fechar", command=vetReceb.destroy)
    button.pack(side=BOTTOM)
    return 1


def janela(path, faces):
    definePropriedades = Tk()
    print("entrou na em illuminantes na função janela")
    definePropriedades.title("Illuminants -propriedades")

    Label(definePropriedades , text="Selecione os descritores desjados:").grid(row=0, sticky=W)
    var1 = IntVar()
    Checkbutton(definePropriedades, text="ACC", variable=var1).grid(row=1, sticky=W)
    Checkbutton(definePropriedades, text="BIC", variable=var1).grid(row=2, sticky=W)
    Checkbutton(definePropriedades, text="CCV", variable=var1).grid(row=3, sticky=W)
    Checkbutton(definePropriedades, text="EOAC", variable=var1).grid(row=4, sticky=W)
    Checkbutton(definePropriedades, text="LAS", variable=var1).grid(row=5, sticky=W)
    Checkbutton(definePropriedades, text="LCH", variable=var1).grid(row=6, sticky=W)
    Checkbutton(definePropriedades, text="SASI", variable=var1).grid(row=7, sticky=W)
    Checkbutton(definePropriedades, text="SPYTEC", variable=var1).grid(row=8, sticky=W)
    Checkbutton(definePropriedades, text="UNSER", variable=var1).grid(row=9, sticky=W)

    # Para extrair descritor de iagens do illuminat maps (IIC e GGE) de todas as imagens na pasta
    # /database/images/ execute a função DS

    Checkbutton(definePropriedades, text="DS", variable=var1).grid(row=11, sticky=W)

    button = Button(definePropriedades, text="Executar", command=printCommando(var1))
    button.pack(side=BOTTOM)


    #vetoresRecebidos(faces)
    return 1


def printCommando(var):
    print(var)

def recebeImagemaSerAnalisada(imagepath, faces):
    #entrar em database imagens e inserir a imagem a ser analisada, remover imagens anteriores
    #executar a função /source-code/segmentAllImagesForIlluminantMethod.py
    return 'teste'


