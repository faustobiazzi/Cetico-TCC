# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:03:58 2016

@author: Fausto Biazzi de Sousa
@modulo: interface gráfica Cético + funções.
programa = "Cético"
versão = "Alpha 0.0.2.1"

"""


programa = "Cético"
versao = "Alpha 0.0.2.1"

from funcoes import *
from __error import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


class Cetico():
    path = ""
    marcas = []
    corAutoMark = "#00FF00"  # verde
    corManualMark = "#FF0000"  # vermelho
    coordXmouse = 0
    coordYmouse = 0
    VarLVetW = False
    Varabout = False
    VarFDetc = False
    VarIllum = False

    def __init__(self, master):

        self.interface = master
        self.interface.title(programa + "- Versão " + versao)
        try:
            self.interface.iconbitmap("icone.ico")
        except:
            print("não foi possivel carregar icone")
        self.interface.wm_protocol("WM_DELETE_WINDOW", dialogofechar)
        self.shown = BooleanVar()
        self.shown.set(False)
        w = self.interface.winfo_screenwidth()
        h = self.interface.winfo_screenheight()

        # redimendiona janela pro tamanho definido
        self.interface.geometry("%dx%d" % (w, h))

        # area util
        self.canvasX = 0
        self.canvasY = 0
        self.canvas = Canvas(width=w, height=h, cursor="cross")
        self.canvas.pack(side="top", fill="none", expand=True)

        # criação do menu

        # menu arquivo
        menubar = Menu(self.interface)

        # menu Arquivo
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Carregar imagem", underline=0, command=self.abrirImagem, accelerator="Ctrl+A")
        filemenu.add_command(label="Fechar imagem", underline=0, command=self.fecharImagem, accelerator="Ctrl+Q")
        filemenu.add_separator()
        filemenu.add_command(label="Gerar relatório", command=dialogo)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", underline=3, command=dialogofechar, accelerator="Alt+F4")
        menubar.add_cascade(label="Arquivo", underline=0, menu=filemenu)
        # menu exibir
        # viewmenu = Menu(menubar, tearoff=0)
        # viewmenu.add_command(label="Zoom +", command=dialogo)
        # viewmenu.add_command(label="Zoom -", command=dialogo)
        # viewmenu.add_command(label="Ajustar imagem a janela", command=dialogo)
        # viewmenu.add_separator()
        # menubar.add_cascade(label="Exibir", underline=1, menu=viewmenu)

        # menu ferramentas
        toolsmenu = Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Detector de rostos", command=self.configDetecta)
        toolsmenu.add_command(label="Ler EXIF da imagem", command=self.propriedadesImg)
        toolsmenu.add_separator()

        # entradas de menu para códigos de terceiros
        toolsmenu.add_command(label="illuminants", command=self.illuminants)
        toolsmenu.add_command(label="copy-move detetector", command=dialogo)
        toolsmenu.add_command(label="fingersprint", command=dialogo)
        toolsmenu.add_command(label="face recognition", command=dialogo)

        # fim de entrada de menu para códigos de terceiros
        toolsmenu.add_separator()
        toolsmenu.add_command(label="Limpar Marcas", command=self.limparTodasMarcas)
        toolsmenu.add_command(label="Remover última Marca", command=self.removeUltimaMarca)
        toolsmenu.add_separator()
        toolsmenu.add_checkbutton(label='habilitar marcação', command=self.desenharMarcasManual, variable=self.shown,
                                  onvalue=True, offvalue=False)
        menubar.add_cascade(label="Ferramentas", underline=0, menu=toolsmenu)

        # menu ajuda
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tópicos de ajuda", underline=0, command=dialogo)
        helpmenu.add_command(label="Sobre...", underline=0, command=self.sobreCetico)
        menubar.add_cascade(label="Ajuda", underline=1, menu=helpmenu)
        self.interface.config(menu=menubar)

    # comandos de arquivo

    def abrirImagem(self):
        if self.marcas != []:
            try:
                self.atualizarMarcas()
                self.vetReceb.destroy()
            except:
                print ("erro")

        self.marcas = []
        self.path = askopenfilename(
        filetypes=(("Todos os Arquivos", "*.*"), ("imagem JPG", "*.jpg\;*.jpeg"), ("imagem bitmap", "*.bmp"),
                   ("imagem PNG", "*.png")),
        title="Selecione um arquivo.")
        self.imagem = ImageTk.PhotoImage(Image.open(self.path))
        self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)

    def fecharImagem(self):
        self.canvas.delete("all")
        self.path = ""
        if self.marcas != []:
            self.marcas = []
            self.fecharJanelasSubordinadas("Lista")

    # comandos de marcação
    def desenharMarcasManual(self):
        if self.shown.get():
            print("função desenho habilitada")
            # desenhar retangulo

            self.canvas.bind("<ButtonPress-1>", self.marca_cliqueDireito_mouse)
            self.canvas.bind("<ButtonRelease-1>", self.marca_liberaClique_mouse)
        else:
            print("função desenho desabilitada")

    def marca_cliqueDireito_mouse(self, event):
        self.coordXmouse = event.x
        self.coordYmouse = event.y

    def marca_liberaClique_mouse(self, event):
        x0, y0 = (self.coordXmouse, self.coordYmouse)
        x1, y1 = (event.x, event.y)
        w1 = x1-x0
        h1 = y1-y0
        if self.shown.get():
            self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, outline=self.corManualMark, width=2)
            self.marcas.append([x0, y0, w1, h1])
            self.atualizarMarcas()

    def limparTodasMarcas(self):
        if self.marcas!=[]:
            if messagebox.askyesno("Limpar marcas",
                                   "isso ira remover todas as marcações feitas na imagem.\n"
                                   "Tem certeza que deseja fazer isso?"):
                self.canvas.delete("all")
                self.marcas = []
                self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
                print("marcas limpas")
                print(self.marcas)
            self.atualizarMarcas()

    def removeUltimaMarca(self):
        if messagebox.askyesno("remover última marcação",
                               "isso ira remover a última marcação feitas na imagem.\n"
                               "Tem certeza que deseja fazer isso?"):
            self.canvas.delete("all")

            self.marcas.pop()
            #del self.marcas[-1]

            self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
            for (x0, y0, w1, h1) in self.marcas:
                self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)
            self.atualizarMarcas()

    def atualizarMarcas(self):
        if self.VarLVetW:
            self.vetReceb.destroy()
            self.listaMarcas()
        else:
            self.VarLVetW = False
            self.listaMarcas()

    def listaMarcas(self):
        self.VarLVetW = True
        self.vetReceb = Tk()
        self.vetReceb.title("Coordenadas")
        self.vetReceb.wm_protocol("WM_DELETE_WINDOW", lambda: self.fecharJanelasSubordinadas("Lista"))
        self.vetReceb.resizable(width=FALSE, height=FALSE)

        scrollbar = Scrollbar(self.vetReceb)
        scrollbar.pack(side=RIGHT, fill=Y)
        w = 150
        h = 400

        lista = Listbox(self.vetReceb, yscrollcommand=scrollbar.set)
        for item in self.marcas:
            lista.insert(END, str(item))

        lista.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=lista.yview)

        self.vetReceb.geometry("%dx%d+%d+%d" % (w, h, self.vetReceb.winfo_screenwidth()-(w+10), 100))


    # Ajuda

    def sobreCetico(self):
        if self.Varabout == False:
            self.Varabout= True
            self.about = Toplevel(self.interface)
            self.about.title("Sobre " + programa + " " + versao)
            self.about.wm_protocol("WM_DELETE_WINDOW", lambda: self.fecharJanelasSubordinadas("Sobre"))

            self.about.resizable(width=FALSE, height=FALSE)

            label = Label(self.about, text="Sobre o Cético... \n"
                                                  + "Cético é um programa \ndesenvolvido pelo" +
                                                    "Aluno Fausto Biazzi de Sousa \n como parte" +
                                                    "integrante de seu \nTrabalho de Conclusão de Curso" +
                                                    "\n(TCC) do Curso de graduação \nem tecnologia de Analise e" +
                                                    "Desenvolvimento\n de Sistema no IFSP-Campinas.")
            label.pack(side=TOP)

            button = Button(self.about, text="Fechar", underline=0, command=lambda: self.fecharJanelasSubordinadas("Sobre"))
            button.pack(side=BOTTOM)

            w = 300
            h = 400
            # redimendiona janela pro tamanho definido
            self.about.geometry("%dx%d" % (w, h))

    # Inserir comandos de módulos a partir dessa seção

    # Detecção de rostos

    def configDetecta(self):
        if self.path != "":

            if self.VarFDetc == False:
                self.confDetecta = Toplevel(self.interface)
                self.confDetecta.title("Configurar Detecção automatica de rostos")
                self.confDetecta.wm_protocol("WM_DELETE_WINDOW", lambda: self.fecharJanelasSubordinadas("Detecta"))
                self.confDetecta.resizable(width=FALSE, height=FALSE)

                self.confDetecta.geometry("%dx%d+%d+%d" % (250, 200, self.confDetecta.winfo_screenwidth()/2-125,
                                                           self.confDetecta.winfo_screenmmheight()/2+100))
                label1 = Label(self.confDetecta, text="Mínimo X: ")
                label2 = Label(self.confDetecta, text="Mínimo Y: ")
                label3 = Label(self.confDetecta, text="Mínimo Vizinhos: ")
                label4 = Label(self.confDetecta, text="Escala: ")

                self.input1 = Entry(self.confDetecta)
                self.input2 = Entry(self.confDetecta)
                self.input3 = Entry(self.confDetecta)
                self.input4 = Entry(self.confDetecta)

                button = Button(self.confDetecta, text="Fechar", underline=0, command=lambda: self.fecharJanelasSubordinadas("Detecta"))
                button2 = Button(self.confDetecta, text="Setar Valores", underline=0, command=self.setarConfigDetecta)

                label1.pack(anchor=W)
                self.input1.insert(0, 30)
                self.input1.pack(anchor=E)

                label2.pack(anchor=W)
                self.input2.insert(0, 30)
                self.input2.pack(anchor=E)

                label3.pack(anchor=W)
                self.input3.insert(0, 1)
                self.input3.pack(anchor=E)

                label4.pack(anchor=W)
                self.input4.insert(0, 1.1)
                self.input4.pack(anchor=E)

                button.pack(side=LEFT)
                button2.pack(side=RIGHT)
                self.VarFDetc = True

        else:
            erroImagemNaoCarregada()

    def setarConfigDetecta(self):
        parametros = [int(self.input1.get()), int(self.input2.get()), int(self.input3.get()), float(self.input4.get())]

        if not self.marcas == []:
            if messagebox.askyesno("Alerta!",
                                   "já existem marcações feitas na imagem.\n Deseja apaga-las?"):
                self.limparTodasMarcas()
                self.aplicaDetectaRosto(parametros)
            else:
                self.aplicaDetectaRosto(parametros)
        else:
            self.aplicaDetectaRosto(parametros)
            self.fecharJanelasSubordinadas("Detecta")

    def aplicaDetectaRosto(self, parametros):

        try:
            face = buscarRosto(self.path, parametros)
        except:
            erroImp_Detecface()

        for (x0, y0, w1, h1) in face:
            self.marcas.append([x0, y0, w1, h1])
            self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)
        self.atualizarMarcas()


    # Pegar propriedade das imagens
    def propriedadesImg(self):
        print(propriedadesImagem(self.path))

    # acesso a módulos de terceiros

    def illuminants(self):
        if self.VarIllum == False:
            if self.marcas != []:
                if self.path != "":
                    try:
                        self.janelaIlluminants()
                        self.VarIllum = True
                    except NameError:
                        erroModuloGenérico(str(NameError))
                else:
                    erroImagemNaoCarregada()
            else:
                erro_RetornoGenerico()

    def janelaIlluminants(self):

        sub = self
        def extrairDescritoresdaImagem(v1, v2, v3, v4, v5, v6, v7, v8, v9, v0):
            comando = "/source-code/segmentAllImagesForIlluminantMethod.py"
            if v0:
                Moduloilluminant("TODOS", self.path, self.marcas)
                comando += " ACC BIC CCV EOAC LAS LCH SASI SPYTEC UNSER"
            else:
                if v1:
                    Moduloilluminant("acc",self.path, self.marcas)
                    comando += " ACC"

                if v2:
                    Moduloilluminant("bic", self.path, self.marcas)
                    comando += " BIC"

                if v3:
                    Moduloilluminant("ccv", self.path, self.marcas)
                    comando += " CCV"
                if v4:
                    Moduloilluminant("eoac", self.path, self.marcas)
                    comando += " EOAC"

                if v5:
                    Moduloilluminant("las", self.path, self.marcas)
                    comando += " LAS"

                if v6:
                    Moduloilluminant("lch", self.path, self.marcas)
                    comando += " LCH"
                if v7:
                    Moduloilluminant("sasir", self.path, self.marcas)
                    comando += " SASIR"

                if v8:
                    Moduloilluminant("spytec", self.path, self.marcas)
                    comando += " SPYTEC"

                if v9:
                    Moduloilluminant("unser", self.path, self.marcas)
                    comando += " UNSER"
            print(comando)

        def janelaModulosExtracao(_self):
            def verificaChkBox():
                if var0.get():
                    var1.set(0), var2.set(0), var3.set(0), var4.set(0), var5.set(0), var6.set(0), var7.set(0), var8.set(
                        0), var9.set(0)
                if var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get():
                    var0.set(0)
                if var1.get() and var2.get() and var3.get() and var4.get() and var5.get() and var6.get() and var7.get() and var8.get() and var9.get():
                    var0.set(0)

            _self.j_illuminants = Toplevel(self.interface)
            _self.j_illuminants.title("Illuminants")
            _self.j_illuminants.resizable(width=FALSE, height=FALSE)
            _self.j_illuminants.wm_protocol("WM_DELETE_WINDOW", lambda : _self.fecharJanelasSubordinadas("Illuminants"))
            Label(_self.j_illuminants, text="Selecione os descritores desejados:").grid(column=0, row=0)

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

            Checkbutton(_self.j_illuminants, anchor=W, text="ACC", variable=var1, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=1)
            Checkbutton(_self.j_illuminants, anchor=W, text="BIC", variable=var2, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=2)
            Checkbutton(_self.j_illuminants, anchor=W, text="CCV", variable=var3, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=3)
            Checkbutton(_self.j_illuminants, anchor=W, text="EOAC", variable=var4, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=4)
            Checkbutton(_self.j_illuminants, anchor=W, text="LAS", variable=var5, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=5)
            Checkbutton(_self.j_illuminants, anchor=W, text="LCH", variable=var6, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=6)
            Checkbutton(_self.j_illuminants, anchor=W, text="SASI", variable=var7, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=7)
            Checkbutton(_self.j_illuminants, anchor=W, text="SPYTEC", variable=var8, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=8)
            Checkbutton(_self.j_illuminants, anchor=W, text="UNSER", variable=var9, offvalue=0,
                        onvalue=1, width=20, command=verificaChkBox).grid(column=0, row=9)

            Checkbutton(_self.j_illuminants, anchor=W, text="TODOS", variable=var0, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=10)
            Button(_self.j_illuminants, underline= 0, text=u"Cancelar", command=lambda : _self.fecharJanelasSubordinadas("Illuminants")).grid(row=10, column=1)
            Button(_self.j_illuminants, underline= 2,text=u"Executar",
                   command=lambda: extrairDescritoresdaImagem(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var0.get())).grid(row=10, column=2)

        Moduloilluminant("segmentar", self.path, self.marcas)
        janelaModulosExtracao(sub)


    def fecharJanelasSubordinadas(self, janela):
        if janela =="Illuminants":
            self.VarIllum = False
            self.j_illuminants.destroy()

        if janela =="Sobre":
            self.Varabout = False
            self.about.destroy()

        if janela =="Detecta":
            self.VarFDetc = False
            self.confDetecta.destroy()

        if janela =="Lista":
            self.VarLVetW = False
            self.vetReceb.destroy()


def main():
    root = Tk()
    Cetico(root)
    root.mainloop()

if __name__ == '__main__':
    main()