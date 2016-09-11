# -*- coding: utf-8 -*-

from tkinter import *

programa = "Cético"
Modulo= "Illuminants"


class Illuminants:
    path = ""
    faces = []

    def __init__(self,caminho,lista):
        self.path = caminho
        self.faces = lista

        self.definePropriedades = Tk()
        self.definePropriedades.title("Illuminants -propriedades")

        label = Label(self.definePropriedades, text="Selecione os descritores desjados:")

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

        C1 = Checkbutton(self.definePropriedades, anchor=W, text="ACC", variable=var1, offvalue=0, height=2, width=20)
        C2 = Checkbutton(self.definePropriedades, anchor=W, text="BIC", variable=var2, offvalue=0, height=2, width=20)
        C3 = Checkbutton(self.definePropriedades, anchor=W, text="CCV", variable=var3, offvalue=0, height=2, width=20)
        C4 = Checkbutton(self.definePropriedades, anchor=W, text="EOAC", variable=var4, offvalue=0, height=2, width=20)
        C5 = Checkbutton(self.definePropriedades, anchor=W, text="LAS", variable=var5, offvalue=0, height=2, width=20)
        C6 = Checkbutton(self.definePropriedades, anchor=W, text="LCH", variable=var6, offvalue=0, height=2, width=20)
        C7 = Checkbutton(self.definePropriedades, anchor=W, text="SASI", variable=var7, offvalue=0, height=2, width=20)
        C8 = Checkbutton(self.definePropriedades, anchor=W, text="SPYTEC", variable=var8, offvalue=0, height=2, width=20)
        C9 = Checkbutton(self.definePropriedades, anchor=W, text="UNSER", variable=var9, offvalue=0, height=2, width=20)

        # Para extrair descritor de imagens do illuminats maps (IIC e GGE) de todas as imagens na pasta
        # /database/images/ execute a função ./sourcecode/extractAllFeatureVectors.py <DS>
        # Onde DS é uma string que representa o descritor a ser extraido,
        # exemplo para o comand de TODOS os descritores

        C0 = Checkbutton(self.definePropriedades, anchor=W, text="TODOS", variable=var0, offvalue=0, height=2, width=20)

        Executar = Button(self.definePropriedades, text="Executar", command=self.extrairdescritores)

        label.pack()
        C1.pack()
        C2.pack()
        C3.pack()
        C4.pack()
        C5.pack()
        C6.pack()
        C7.pack()
        C8.pack()
        C9.pack()
        C0.pack()
        Executar.pack()
        self.listvet()



    def listvet(self):

        self.vetReceb = Tk()
        self.vetReceb.title("Coordenadas")
        print("entrou lista de vetores")
        self.vetReceb.resizable(width=FALSE, height=FALSE)

        scrollbar = Scrollbar(self.vetReceb)
        scrollbar.pack(side=RIGHT, fill=Y)
        w = 150
        h = 400

        lista = Listbox(self.vetReceb, yscrollcommand=scrollbar.set)
        for line in self.faces:
            lista.insert(END, str(line))

        lista.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=lista.yview)

        self.vetReceb.geometry("%dx%d+%d+%d" % (w, h, self.vetReceb.winfo_screenwidth()-(w+10), 100))

        mainloop()

    def extrairdescritores(self):
        print("entrou em extrair descritores"+ self.path, self.faces)

    def recebeImagemaSerAnalisada(self):
        #entrar em database imagens e inserir a imagem a ser analisada, remover imagens anteriores
        #executar a função /source-code/segmentAllImagesForIlluminantMethod.py


        return 'teste'


def main():
    path = "/home/fausto/Dropbox/Ceticov1.6/imagens/pessoas.jpg"
    faces = [(202, 89, 45, 58)]
    Illuminants(path, faces)

if __name__ == '__main__':
    main()

