# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016

@author: Fausto Biazzi de Sousa
@modulo: interface gráfica (inicial) Cético.
programa = "Cético"
versao = "Alpha 0.0.1.2"

"""

from tkinter import *
from funcoes import *
from __error import *
from PIL import Image, ImageTk
import cv2

programa = "Cético"
versao = "Alpha 0.0.1.2"



class window():
    path = ""
    corMark="red"
    marcas = []
    a1 = ""
    corAutoMark = "#00FF00"       
    def __init__(self):
        #definição da janela principal        
        self.janela = Tk()
        self.janela.title(programa+"- Versão "+versao)
        try:
            self.janela.iconbitmap("icone.ico")
        except:
            print ("não foi possivel carregar icone")
        self.janela.wm_protocol ("WM_DELETE_WINDOW",dialogofechar)
        
        
        
        
        
        self.shown = BooleanVar()
        self.shown.set(False)
        #tamanho incial da janela (definido 800x600 por ser uma resolução comum 
        #entre monitores CRTS e a minima suportada por alguns sistemas)        
        w=800
        h=600
        #redimendiona janela pro tamanho definido        
        self.janela.geometry("%dx%d" % (w, h))
         
        #area util
        self.x = self.y = 0
        self.canvas = Canvas(width=w, height=h, cursor="cross")
        self.canvas.pack(side="top", fill="none", expand=True)

        
        
        #ZOOM
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomP)
        self.canvas.bind("<Button-5>", self.zoomM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomW)        
        
        #criação do menu
        
        #menu arquivo
        menubar = Menu(self.janela)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Carregar imagem", command=self.abrirImagem)
        filemenu.add_command(label="Fechar imagem", command=self.fecharImagem)
        filemenu.add_separator()
        filemenu.add_command(label="Gerar relatório", command=dialogo)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=dialogofechar)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        
        #menu exibir
        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Zoom +", command=dialogo)
        viewmenu.add_command(label="Zoom -", command=dialogo)
        viewmenu.add_command(label="Ajustar imagem a janela", command=dialogo)
        viewmenu.add_separator()
        menubar.add_cascade(label="Exibir", menu=viewmenu)
        
        #menu ferramentas
        toolsmenu = Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Detector de rostos",command=self.detectaRosto)
        toolsmenu.add_command(label="Ler EXIF da imagem",command=self.propriedadesImg)
        toolsmenu.add_separator()
        toolsmenu.add_command(label="Limpar Marcas",command=dialogo)
        toolsmenu.add_checkbutton (label='habilitar marcação',command=self.bolDesenharMarcas,variable=self.shown,onvalue = True,offvalue = False)
        menubar.add_cascade(label="Ferramentas", menu=toolsmenu)
        
        #menu ajuda
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tópicos de ajuda", command=dialogo)
        helpmenu.add_command(label="Sobre...", command=self.about)
        menubar.add_cascade(label="Ajuda", menu=helpmenu)
        self.janela.config(menu=menubar)
    
        #rodar janela
        self.janela.mainloop()
    
    
    #comandos de mouse
                 
    def bolDesenharMarcas(self):
       
        if (self.shown == False):
            self.shown = (True)
            self.desenharMarcas()
            print(self.shown)
        else:
            self.shown = (False)
            self.desenharMarcas()
            print (self.shown)
       
    def desenharMarcas(self):
        if (self.shown==True):
            print("função desenho habilitada")
            #desenhar retangulo
            self.canvas.bind("<ButtonPress-1>", self.on_button_press)
            self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        else:
             print("função desenho desabilitada")
  
    def on_button_press(self, event):
        self.x = event.x
        self.y = event.y

    def on_button_release(self, event):
        x0,y0 = (self.x, self.y)
        x1,y1 = (event.x, event.y)

        self.canvas.create_rectangle(x0,y0,x1,y1,outline = (self.corMark), width=2)
        self.marcas.append((x0,y0,x1,y1))
        print (self.marcas)
        
          
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
        
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    
    #Zoom windows
    def zoomW(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    
    #zoom linux
    def zoomP(self,event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomM(self,event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #comandos de arquivo
        
    def abrirArquivo(self):
        name = askopenfilename(
                               filetypes =(("Todos os Arquivos","*.*"),("imagem JPG", "*.jpg\;*.jpeg"),("imagem bitmap", "*.bmp"),
                                           ("imagem PNG", "*.png")),
                               title = "Selecione um arquivo."
                               )
        try:
            print (name)
            return name
           
            
        except:
            erroAbrirArquivo()

  
    def fecharImagem (self):
        self.canvas.delete("all")
        self.path = ""
        self.marcas = []
     
    def about(self):
         ajuda.janela()
    
    def abrirImagem(self):
        try:
            self.path = self.abrirArquivo()
            self.imagem = ImageTk.PhotoImage(Image.open(self.path))
           
            self.canvas.create_image(0, 0, anchor=NW,image = self.imagem)#funciona o carregamento mas não funciona o zoom!
            
            
            print ("Exibindo imagem "+self.path)
           
            
        except:
            if (self.path ==""):
                print ("nenhuma imagem carregada")
            else:
               erroAbrirArquivo()
        
    def propriedadesImg(self):
        propriedadesImagem(self.path)

    def detectaRosto(self):
      if (self.path != ""):
            try:
                print("\n \n teste cv " + self.path)
                faces= (detectorRosto(self.path))
            except:
                erroImp_Detecface()
      else:
          erroImagemNaoCarregada()
      for (x0, y0, w1, h1) in faces:
          self.marcas.append((x0,y0,w1,h1))
          self.canvas.create_rectangle(x0, y0, x0+w1, y0+h1, fill=None,outline = (self.corAutoMark), width=2)
      print (faces)
      print (self.marcas)
    
      
            
    

class ajuda():
    def janela(): 
        filewin = Tk()
        filewin.title("Sobre "+programa+" "+versao)
        filewin.iconbitmap("ICONE.ICO")
        filewin.resizable(width=FALSE, height=FALSE)
        filewin.attributes("-toolwindow",1)
        filewinlabel = Label(filewin, text="Sobre o Cético... \n"
                                        +"Cético é um programa \ndesenvolvido pelo"+
                                        "Aluno Fausto Biazzi de Sousa \n como parte"+
                                        "integrante de seu \nTrabalho de Conclusão de Curso"+
                                        "\n(TCC) do Curso de graduação \nem tecnologia de Analise e"+
                                        "Desenvolvimento\n de Sistema no IFSP-Campinas.")
        filewinlabel.pack(side=TOP)
                    
        button = Button(filewin,  text="Fechar",command=filewin.destroy)
        button.pack(side = BOTTOM )
        
        w=300
        h=400
        #redimendiona janela pro tamanho definido        
        filewin.geometry("%dx%d" % (w, h))
    def ok(self):

        self.destroy(filewin)

def main():
    app = window()

if __name__ == '__main__':
    main()

