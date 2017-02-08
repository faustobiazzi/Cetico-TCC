# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:50:55 2017

@author: Fausto Biazzi de Sousa
@modulo: interface gráfica Cético + funções.
@programa = "Cético"
@versão = "Alpha 0.0.2.8"

"""
import os
from functions import *
from menu import *


programa = "Cético"
versao = "Alpha 0.0.2.8"


class UI():
    imagem = ""
    path = ""
    metadata = ""
    thumbs = []
    marcas = []
    corManualMark = corAutoMark = "#00FF00"    # verde
    VarLVetW = False
    Varabout = False
    VarFDetc = False
    VarIllum = False
    VarMenu = False
    VarCanvas = False
    janelas = []
    areaImgH = 0
    areaImgW = 0

    def __init__(self, master):
        clearLogs(self)
        readconfigFile(self)
        self.interface = master
        self.interface.title(programa + "- Versão " + versao)
        iconfile = (os.path.join(os.path.abspath(os.path.dirname(__file__)) + "/data/icone.ico"))
        try:
            self.interface.iconbitmap(iconfile)
        except:
            pass

        self.interface.wm_protocol("WM_DELETE_WINDOW", closeAPPDialog)
        self.shown = BooleanVar()
        self.shown.set(False)
        w = self.interface.winfo_screenwidth()
        h = self.interface.winfo_screenheight()

        # redimendiona janela pro tamanho definido
        self.interface.geometry("%dx%d" % (w, h))
        #self.createCanvas()

        # criação do menu
        menu(self)

    def createCanvas(self):
        w = self.interface.winfo_screenwidth()
        h = self.interface.winfo_screenheight()

        # redimendiona janela pro tamanho definido
        self.interface.geometry("%dx%d" % (w, h))


        # area util
        self.canvasX = 0
        self.canvasY = 0

        self.canvas = Canvas(self.interface, relief=SUNKEN)

        self.canvas.config(width=400, height=200)

        self.canvas.config(highlightthickness=0)
        self.sbarV = Scrollbar(self.interface, orient=VERTICAL)
        self.sbarH = Scrollbar(self.interface, orient=HORIZONTAL)

        self.sbarV.config(command=self.canvas.yview)
        self.sbarH.config(command=self.canvas.xview)

        self.canvas.config(yscrollcommand=self.sbarV.set)
        self.canvas.config(xscrollcommand=self.sbarH.set)

        self.sbarV.pack(side=RIGHT, fill=Y)
        self.sbarH.pack(side=BOTTOM, fill=X)

        self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)
        self.canvas.config(scrollregion=(0, 0, self.imagem.width(), self.imagem.height()))
        '''
        self.canvas = Canvas(width=self.imagem.width(), height=self.imagem.height(), cursor="cross")
        self.canvas.pack(side=LEFT, anchor=NW, expand=True,fill= "none")
        '''
        self.VarCanvas = True

    def hideCanvas(self):
        if self.VarCanvas:
            self.canvas.pack_forget()
            self.VarCanvas = False
        else:
            self.canvas.pack()
            self.VarCanvas = True

    def closeWindows(self, janela):
        if janela == "Illuminants":
            self.VarIllum = False
            self.j_illuminants.destroy()

        if janela == "resultadoIllu":
            self.VarIllum = False
            self.j_Resultilluminants.destroy()

        if janela == "Sobre":
            self.Varabout = False
            self.about.destroy()

        if janela == "Detecta":
            self.VarFDetc = False
            self.confDetecta.destroy()

        if janela == "Lista":
            self.VarLVetW = False
            self.vetReceb.destroy()

    # comandos de arquivo
    def openImage(self):
        if self.path == "":
            try:
                self.canvas.delete("all")
                self.canvas.destroy()

            except:
                pass
            self.path = commondialogbox("Open")
            if self.path != "":
                try:
                    self.interface.title(programa + "- Versão " + versao + " - [" + self.path + "]")
                except:
                    pass
                self.imagem = ImageTk.PhotoImage(Image.open(self.path))
                self.createCanvas()
                self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
        else:
            if self.closeImage():
                self.openImage()

    def closeImage(self):
        if closeImageDialog():
            clearLogs(self)
            try:
                self.canvas.delete("all")
                self.sbarH.destroy()
                self.sbarV.destroy()
                self.canvas.destroy()
            except:
                pass
            self.shown.set(FALSE)
            self.draw_SquareMark()
            self.path = ""
            self.interface.title(programa + "- Versão " + versao)
            if self.marcas != []:
                self.marcas = []
                if self.VarLVetW:
                    self.closeWindows("Lista")
            return 1
        else:
            return 0

    def exportImage(self):
        filename = commondialogbox("Save")
        self.canvas.postscript(file=filename)

    def generateReport(self):
        if not self.path:
            erroImagemNaoCarregada()
        else:
            report_preparedata(self)

    def printCanvas(self):
        dialogo()

    # comandos de marcação
    def draw_SquareMark(self):
        if self.shown.get():
            self.canvas.bind("<ButtonPress-1>", self.square_MarkupClick)
            self.canvas.bind("<ButtonRelease-1>", self.square_MarkupRelease)
        else:
            pass

    def square_MarkupClick(self, event):
        self.coordXmouse = event.x
        self.coordYmouse = event.y

    def square_MarkupRelease(self, event):
        x0, y0 = (self.coordXmouse, self.coordYmouse)
        x1, y1 = (event.x, event.y)
        w1 = x1 - x0
        h1 = y1 - y0
        if self.shown.get():
            self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, outline=self.corManualMark, width=2)
            self.marcas.append([x0, y0, w1, h1])
            if self.VarLVetW:
                self.refreshMarkups()

    def clearMarkups(self):
        if self.marcas != []:
            if messagebox.askyesno("Limpar marcas",
                                   "isso ira remover todas as marcações feitas na imagem.\n"
                                   "Tem certeza que deseja fazer isso?"):
                self.canvas.delete("all")
                self.marcas = []
                self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
                if self.VarLVetW:
                    self.refreshMarkups()

    def removeLastMark(self):
        if messagebox.askyesno("remover última marcação",
                               "isso ira remover a última marcação feitas na imagem.\n"
                               "Tem certeza que deseja fazer isso?"):
            self.canvas.delete("all")

            self.marcas.pop()
            if self.VarLVetW:
                self.refreshMarkups()
            self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
            for (x0, y0, w1, h1) in self.marcas:
                self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)

    def refreshMarkups(self):
        if self.VarLVetW:
            self.vetReceb.destroy()
            self.MarkupEditor()

        else:
            self.VarLVetW = False
            self.MarkupEditor()

    def MarkupEditor(self):
        self.VarLVetW = True
        self.vetReceb = Tk()
        self.vetReceb.title("Coordenadas")
        self.vetReceb.wm_attributes("-topmost", 1)
        self.vetReceb.wm_protocol("WM_DELETE_WINDOW", lambda: self.closeWindows("Lista"))
        self.vetReceb.resizable(width=FALSE, height=FALSE)
        self.vetReceb.bind("<Escape>", (lambda e: self.closeWindows("Lista")))
        scrollbar = Scrollbar(self.vetReceb)
        scrollbar.pack(side=RIGHT, fill=Y)
        w = 150
        h = 400

        lista = Listbox(self.vetReceb, yscrollcommand=scrollbar.set)
        for item in self.marcas:
            lista.insert(END, str(item))

        lista.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=lista.yview)

        self.vetReceb.geometry("%dx%d+%d+%d" % (w, h, self.vetReceb.winfo_screenwidth() - (w + 10), 100))

    # Ajuda

    def aboutCetico(self):
        if self.Varabout == False:
            self.Varabout = True
            self.about = Toplevel()
            self.about.title("Sobre " + programa + " " + versao)
            self.about.wm_protocol("WM_DELETE_WINDOW", lambda: self.closeWindows("Sobre"))

            self.about.resizable(width=FALSE, height=FALSE)

            label = Label(self.about, text="Sobre o Cético... \n"
                                           + "Cético é um programa \ndesenvolvido pelo" +
                                           "Aluno Fausto Biazzi de Sousa \n como parte" +
                                           "integrante de seu \nTrabalho de Conclusão de Curso" +
                                           "\n(TCC) do Curso de graduação \nem tecnologia de Analise e" +
                                           "Desenvolvimento\n de Sistema no IFSP-Campinas.")

            label.pack(side=TOP)
            self.about.bind("<Escape>", (lambda e: self.closeWindows("Sobre")))
            button = Button(self.about, text="Fechar", underline=0,
                            command=lambda: self.closeWindows("Sobre"))
            button.pack(side=BOTTOM)

            w = 300
            h = 280
            # redimendiona janela pro tamanho definido
            self.about.geometry("%dx%d" % (w, h))

            clogo = Canvas(self.about)
            logopath = (os.path.join(os.path.abspath(os.path.dirname(__file__)) + "/data/cetico.jpg"))
            logoimg = ImageTk.PhotoImage(Image.open(logopath))
            clogo.create_image(w/2, 60, image=logoimg)
            clogo.pack()
            self.about.mainloop()

    # Inserir comandos de módulos a partir dessa seção

    # Pegar propriedade das imagens
    def propriedadesImg(self):
        self.exif = propriedadesImagem("Nodecoded", self.path)
        print(self.exif)


def main():
    root = Tk()
    app = UI(root)

    root.mainloop()

    root.after(0, app.openImage())


if __name__ == '__main__':
    main()

