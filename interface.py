# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016

@author: Fausto Biazzi de Sousa
@modulo: interface gráfica (inicial) Cético.
programa = "Cético"
versão = "Alpha 0.0.1.6"

"""

from tkinter import *
from funcoes import *
from __error import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

programa = "Cético"
versao = "Alpha 0.0.1.6"


class Window:
    path = ""
    corMark = "red"
    marcas = []
    a1 = ""
    corAutoMark = "#00FF00"
    mouseX = 0
    mouseY = 0
    def __init__(self):
        # definição da janela principal
        self.janela = Tk()
        self.janela.title(programa + "- Versão " + versao)
        try:
            self.janela.iconbitmap("icone.ico")
        except:
            print("não foi possivel carregar icone")
        self.janela.wm_protocol("WM_DELETE_WINDOW", dialogofechar)
        self.shown = BooleanVar()
        self.shown.set(False)
        w = self.janela.winfo_screenwidth()
        h = self.janela.winfo_screenheight()

        # redimendiona janela pro tamanho definido
        self.janela.geometry("%dx%d" % (w, h))

        # area util
        self.x = 0
        self.y = 0
        self.canvas = Canvas(width=w, height=h, cursor="cross")
        self.canvas.pack(side="top", fill="none", expand=True)

        # criação do menu

        # menu arquivo
        menubar = Menu(self.janela)

        # menu Arquivo
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Carregar imagem", underline=0, command=self.abrirImagem, accelerator="Ctrl+A")
        filemenu.add_command(label="Fechar imagem",  underline=0, command=self.fecharImagem, accelerator="Ctrl+Q")
        filemenu.add_separator()
        filemenu.add_command(label="Gerar relatório", command=dialogo)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", underline=3, command=dialogofechar, accelerator="Alt+F4")
        menubar.add_cascade(label="Arquivo", underline=0, menu=filemenu)
        menubar.bind("<Control-a>", self.abrirImagem())
        # menu exibir
        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Zoom +", command=dialogo)
        viewmenu.add_command(label="Zoom -", command=dialogo)
        viewmenu.add_command(label="Ajustar imagem a janela", command=dialogo)
        viewmenu.add_separator()
        menubar.add_cascade(label="Exibir",  underline=1, menu=viewmenu)

        # menu ferramentas
        toolsmenu = Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Detector de rostos", command=self.menudetectaRosto)
        toolsmenu.add_command(label="Ler EXIF da imagem", command=self.propriedadesImg)
        toolsmenu.add_separator()
        # entradas de menu para códigos de terceiros
        toolsmenu.add_command(label="illuminants", command=self.illuminants)
        toolsmenu.add_command(label="copy-move detetector", command=dialogo)
        toolsmenu.add_command(label="fingersprint", command=dialogo)
        toolsmenu.add_command(label="face recognition", command=dialogo)


        # fim de entrada de menu para códigos de terceiros
        toolsmenu.add_separator()
        toolsmenu.add_command(label="Limpar Marcas", command=self.limparMarcas)
        toolsmenu.add_command(label="Remover última Marca", command=self.remUltimaMarca)
        toolsmenu.add_separator()
        toolsmenu.add_checkbutton(label='habilitar marcação', command=self.bolDesenharMarcas, variable=self.shown,
                                  onvalue=True, offvalue=False)
        menubar.add_cascade(label="Ferramentas", underline=0, menu=toolsmenu)

        # menu ajuda
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tópicos de ajuda", underline=0, command=dialogo)
        helpmenu.add_command(label="Sobre...", underline=0, command=self.about)
        menubar.add_cascade(label="Ajuda", underline=1, menu=helpmenu)
        self.janela.config(menu=menubar)

        # rodar janela
        self.janela.mainloop()

    # comandos de mouse

    def bolDesenharMarcas(self):

        if not self.shown:
            self.shown = True
            self.desenharMarcas()
            print(self.shown)
        else:
            self.shown = False
            print(self.shown)

    def desenharMarcas(self):

        if self.shown:
            print("função desenho habilitada")
            # desenhar retangulo
            self.canvas.bind("<ButtonPress-1>", self.on_button_press)
            self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        else:
            print("função desenho desabilitada")

    def on_button_press(self, event):
        self.mouseX = event.x
        self.mouseY = event.y

    def on_button_release(self, event):
        x0, y0 = (self.mouseX, self.mouseY)
        x1, y1 = (event.x, event.y)
        w1 = x1-x0
        h1 = y1-y0

        self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, outline=self.corMark, width=2)
        self.marcas.append((x0, y0, w1, h1))
        print(self.marcas)

    # comandos de arquivo
    def abrirArquivo(self):

        name = askopenfilename(
            filetypes=(("Todos os Arquivos", "*.*"), ("imagem JPG", "*.jpg\;*.jpeg"), ("imagem bitmap", "*.bmp"),
                       ("imagem PNG", "*.png")),
            title="Selecione um arquivo."
        )
        try:
            print(name)
            return name
        except:
            erroAbrirArquivo()

    def fecharImagem(self):
        self.canvas.delete("all")
        self.path = ""
        self.marcas = []

    def about(self):
        ajuda.janela()

    def abrirImagem(self):
        self.marcas = []

        try:
            self.path = self.abrirArquivo()
            self.imagem = ImageTk.PhotoImage(Image.open(self.path))
            self.canvas.create_image(self.x, self.y, anchor=NW, image=self.imagem)
            # print ("Exibindo imagem "+self.path)
        except:
            if self.path == "":
                print("nenhuma imagem carregada")
            else:
                erroAbrirArquivo()

    def propriedadesImg(self):
        print(propriedadesImagem(self.path))

    def limparMarcas(self):
        if messagebox.askyesno("Limpar marcas",
                               "isso ira remover todas as marcações feitas na imagem.\nTem certeza que deseja fazer isso?"):
            self.canvas.delete("all")
            self.marcas = []
            self.canvas.create_image(self.x, self.y, anchor=NW, image=self.imagem)
            print("marcas limpas")
            print(self.marcas)

    def remUltimaMarca(self):
        if messagebox.askyesno("remover última marcação",
                               "isso ira remover a última marcação feitas na imagem.\nTem certeza que deseja fazer isso?"):
            self.canvas.delete("all")
            self.marcas.pop()
            #del self.marcas[-1]
            self.canvas.create_image(self.x, self.y, anchor=NW, image=self.imagem)
            for (x0, y0, w1, h1) in self.marcas:
                self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)
            print("marcas apos remoção"+str(self.marcas))

    def menudetectaRosto(self):
        if self.marcas > []:
            if messagebox.askyesno("Alerta!",
                                   "já existem marcações feitas na imagem.\n Deseja apaga-las?"):
                self.limparMarcas()
                self.detectaRosto()
            else:
                self.detectaRosto()
        else:
            self.detectaRosto()

    def detectaRosto(self):
        if self.path != "":
            try:
                face = buscarRosto(self.path)
            except:
                erroImp_Detecface()
        else:
            erroImagemNaoCarregada()
        for (x0, y0, w1, h1) in face:
            self.marcas.append((x0, y0, w1, h1))
            self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)

    # acesso a funções de terceiros

    def illuminants(self):
        resultado = illuminant(self.path, self.marcas)
        print(resultado)


class ajuda():
    def janela():
        filewin = Tk()
        filewin.title("Sobre " + programa + " " + versao)
        #filewin.iconbitmap("ICONE.ICO")
        filewin.resizable(width=FALSE, height=FALSE)
        #filewin.attributes("-toolwindow", 1)
        filewinlabel = Label(filewin, text="Sobre o Cético... \n"
                                           + "Cético é um programa \ndesenvolvido pelo" +
                                           "Aluno Fausto Biazzi de Sousa \n como parte" +
                                           "integrante de seu \nTrabalho de Conclusão de Curso" +
                                           "\n(TCC) do Curso de graduação \nem tecnologia de Analise e" +
                                           "Desenvolvimento\n de Sistema no IFSP-Campinas.")
        filewinlabel.pack(side=TOP)

        button = Button(filewin, text="Fechar", underline=0, command=filewin.destroy)
        button.pack(side=BOTTOM)

        w = 300
        h = 400
        # redimendiona janela pro tamanho definido
        filewin.geometry("%dx%d" % (w, h))

    def ok(self):
        self.destroy()



def main():
    Window()

if __name__ == '__main__':
    main()

