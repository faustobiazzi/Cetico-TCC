
from functions import *
from extra import *

def menu(master):
    self = master
    menubar = Menu(self.interface)
    # hotkeys
    # FUNCTIONS KEYS
    self.interface.bind_all("<F1>", lambda e: dialogo())
    self.interface.bind_all("<Control-Alt-M>", lambda e: self.hideCanvas())
    self.interface.bind_all("<Control-Alt-m>", lambda e: self.hideCanvas())
    self.interface.bind_all("<Control-Shift-S>", lambda e: dialogo())
    self.interface.bind_all("<Control-Shift-s>", lambda e: dialogo())
    self.interface.bind_all("<Control-Shift-F4>", lambda e: exit())#saída rápida
    # control + key min
    self.interface.bind_all("<Control-a>", lambda e: self.openImage())
    self.interface.bind_all("<Control-q>", lambda e: self.closeImage())
    self.interface.bind_all("<Control-d>", lambda e: faceDetectorWindow(self))
    self.interface.bind_all("<Control-r>", lambda e: self.removeLastMark())
    self.interface.bind_all("<Control-l>", lambda e: self.clearMarkups())
    self.interface.bind_all("<Control-g>", lambda e: self.generateReport(self.logo))
    self.interface.bind_all("<Control-p>", lambda e: self.printCanvas())

    # control + key caps
    self.interface.bind_all("<Control-A>", lambda e: self.openImage())
    self.interface.bind_all("<Control-Q>", lambda e: self.closeImage())
    self.interface.bind_all("<Control-D>", lambda e: self.faceDetectorWindow())
    self.interface.bind_all("<Control-R>", lambda e: self.removeLastMark())
    self.interface.bind_all("<Control-L>", lambda e: self.clearMarkups())
    self.interface.bind_all("<Control-G>", lambda e: self.generateReport())
    self.interface.bind_all("<Control-P>", lambda e: self.printCanvas())


    # menu arquivo
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Carregar imagem", underline=0, command=self.openImage, accelerator="Ctrl+A")
    filemenu.add_command(label="Fechar imagem", underline=0, command=self.closeImage, accelerator="Ctrl+Q")
    filemenu.add_separator()
    filemenu.add_command(label="Exportar Imagem", command=self.exportImage, accelerator= "Ctrl+I")
    filemenu.add_separator()
    filemenu.add_command(label="Configurações", command=lambda: dialogo(), accelerator="Ctrl+Shift+S")
    filemenu.add_separator()
    filemenu.add_command(label="Gerar relatório", command=self.generateReport, accelerator="Ctrl+G")
    filemenu.add_command(label="Imprimir Imagem", command=self.printCanvas, accelerator="Ctrl+P")
    filemenu.add_separator()
    filemenu.add_command(label="Sair", underline=3, command=closeAPPDialog, accelerator="Alt+F4")
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
    toolsmenu.add_command(label="Detector de rostos", command=lambda: faceDetectorWindow(self), accelerator="Ctrl+D")
    toolsmenu.add_command(label="Ler EXIF da imagem", command=lambda: w_readmetadata(self))
    toolsmenu.add_command(label="Visualizar Thumbnail", command=lambda:w_thumbnailviewer(self))
    toolsmenu.add_separator()

    # entradas de menu para códigos de terceiros
    toolsmenu.add_command(label="illuminants", command=lambda: illuminants(self))
    #toolsmenu.add_command(label="copy-move detetector", command=dialogo)
    #toolsmenu.add_command(label="fingersprint", command=dialogo)
    #toolsmenu.add_command(label="face recognition", command=dialogo)

    # fim de entrada de menu para códigos de terceiros
    toolsmenu.add_separator()
    toolsmenu.add_command(label="Editor de marcações", command=self.MarkupEditor)
    toolsmenu.add_command(label="Limpar Marcas", command=self.clearMarkups, accelerator="Ctrl+L")
    toolsmenu.add_command(label="Remover última Marca", command=self.removeLastMark, accelerator="Ctrl+R")
    toolsmenu.add_separator()
    toolsmenu.add_checkbutton(label='habilitar marcação', command=self.draw_SquareMark,
                              variable=self.shown,
                              onvalue=True, offvalue=False)
    menubar.add_cascade(label="Ferramentas", underline=0, menu=toolsmenu)

    # menu Janela
    windPrincipal = Menu(menubar, tearoff=0)
    windPrincipal.add_command(label="Ocultar imagem", command=self.hideCanvas, accelerator="Ctrl+Alt+M")
    # windPrincipal.add_command(label="Fechar janelas auxiliares", command=lambda:self.fecharJanelasSubordinadas("todas"))
    menubar.add_cascade(label="Janela", underline=1, menu=windPrincipal)

    # menu ajuda
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Tópicos de ajuda", underline=0, command=dialogo)
    helpmenu.add_command(label="Sobre...", underline=0, command=self.aboutCetico)
    menubar.add_cascade(label="Ajuda", underline=1, menu=helpmenu)
    self.interface.config(menu=menubar)
