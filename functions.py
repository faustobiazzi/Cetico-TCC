# comandos de área de trabalho


import subprocess
import configparser
from error import *
from services import *
from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
import io


def readconfigFile(self):
    def ConfigSectionMap(section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    configlocation = (os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/data/cetico.cfg'))
    Config = configparser.ConfigParser()
    Config.read(configlocation)
    Config.sections()

    # Get Identification

    self.logo = ConfigSectionMap('identification')['logo']
    if self.logo == 'logo.png':
        self.logo = (os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/data/logo.png'))
    else:
        print("logo location " + self.logo)
    self.id = ConfigSectionMap('identification')['company']
    self.dpto = ConfigSectionMap('identification')['dpto']
    self.user = ConfigSectionMap('identification')['user']
    self.address = ConfigSectionMap('identification')['address']

    # personalization
    self.corAutoMark = ConfigSectionMap('color')['automark']
    self.corManualMark = ConfigSectionMap('color')['manualmark']

    # report config
    self.margin = []
    self.pagesize = ConfigSectionMap('reportconfig')['pagesize']
    m = ConfigSectionMap('reportconfig')['right']
    self.margin.append(m)
    m = ConfigSectionMap('reportconfig')['left']
    self.margin.append(m)
    m = ConfigSectionMap('reportconfig')['top']
    self.margin.append(m)
    m = ConfigSectionMap('reportconfig')['bottom']
    self.margin.append(m)
    # modules
    self.face = ConfigSectionMap('modules')['faces']
    self.thumb = ConfigSectionMap('modules')['thumbnails']
    self.tbo = ConfigSectionMap('modules')['tborientation']
    self.exif = ConfigSectionMap('modules')['exif']
    self.emode = ConfigSectionMap('modules')['exifmode']
    # thirdyparty
    self.illum = ConfigSectionMap('thyrdparty')['illuminants']


def saveconfigFile(self, modconfig):
    for values in modconfig:
        print(values)
    return "Salvo"


def configWindow(self):
    self.confDetecta = Toplevel(self.interface)
    self.confDetecta.title("Configurar Detecção automatica de rostos")
    self.confDetecta.wm_protocol("WM_DELETE_WINDOW", lambda: self.closeWindows("Detecta"))
    self.confDetecta.resizable(width=FALSE, height=FALSE)

    self.confDetecta.geometry("%dx%d+%d+%d" % (250, 200, self.confDetecta.winfo_screenwidth() / 2 - 125, self.confDetecta.winfo_screenmmheight() / 2 + 100))
    label1 = Label(self.confDetecta, text="Mínimo X: ")
    label2 = Label(self.confDetecta, text="Mínimo Y: ")
    label3 = Label(self.confDetecta, text="Mínimo Vizinhos: ")
    label4 = Label(self.confDetecta, text="Escala: ")

    self.input1 = Entry(self.confDetecta)
    self.input2 = Entry(self.confDetecta)
    self.input3 = Entry(self.confDetecta)
    self.input4 = Entry(self.confDetecta)

    button = Button(self.confDetecta, text="Fechar", underline=0,
                    command=lambda: self.closeWindows("Detecta"))
    button2 = Button(self.confDetecta, text="Setar Valores", underline=0, command=lambda: setFaceDetector(self))
    self.confDetecta.bind("<Escape>", (lambda e: self.closeWindows("Detecta")))
    self.confDetecta.bind("<Return>", (lambda e: setFaceDetector(self)))


def commondialogbox(fn):
    path=""
    formats = (("JPG image", "*.jpg"), ("JPEG image", "*.jpeg"), ("Bitmap image", "*.bmp"),
                           ("PNG image", "*.png"),("All Files", "*.*"))
    boxtitle = "%s File"% fn
    if fn == "Open":
        path = askopenfilename(filetypes=formats, title=boxtitle)
        return path

    elif fn == "Save":
        path = asksaveasfilename(filetypes=formats, title=boxtitle)
        print(path)
        return path

    elif fn == "PDF":
        pdf = "Save PDF report"
        format = (("Adobe PDF File", "*.pdf"), ("All Files", "*.*"))
        path = asksaveasfilename(filetypes=format, title=pdf)
        return path


# Face detector
def faceDetectorWindow(self):
    if self.path != "":

        if self.VarFDetc == False:
            self.confDetecta = Toplevel(self.interface)
            self.confDetecta.title("Configurar Detecção automatica de rostos")
            self.confDetecta.wm_protocol("WM_DELETE_WINDOW", lambda: self.closeWindows("Detecta"))
            self.confDetecta.resizable(width=FALSE, height=FALSE)

            self.confDetecta.geometry("%dx%d+%d+%d" % (250, 200, self.confDetecta.winfo_screenwidth() / 2 - 125,
                                                       self.confDetecta.winfo_screenmmheight() / 2 + 100))
            label1 = Label(self.confDetecta, text="Mínimo X: ")
            label2 = Label(self.confDetecta, text="Mínimo Y: ")
            label3 = Label(self.confDetecta, text="Mínimo Vizinhos: ")
            label4 = Label(self.confDetecta, text="Escala: ")

            self.input1 = Entry(self.confDetecta)
            self.input2 = Entry(self.confDetecta)
            self.input3 = Entry(self.confDetecta)
            self.input4 = Entry(self.confDetecta)

            button = Button(self.confDetecta, text="Fechar", underline=0,
                            command=lambda: self.closeWindows("Detecta"))
            button2 = Button(self.confDetecta, text="Setar Valores", underline=0, command=lambda: setFaceDetector(self))
            self.confDetecta.bind("<Escape>", (lambda e: self.closeWindows("Detecta")))
            self.confDetecta.bind("<Return>", (lambda e: setFaceDetector(self)))
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


def setFaceDetector(self):
    param = [int(self.input1.get()), int(self.input2.get()), int(self.input3.get()), float(self.input4.get())]

    if not self.marcas == []:
        if messagebox.askyesno("Alerta!",
                               "já existem marcações feitas na imagem.\n Deseja apaga-las?"):
            self.clearMarkups()
            applyFaceDetector(self, param)

            self.closeWindows("Detecta")
        else:
            applyFaceDetector(self, param)

            self.closeWindows("Detecta")
    else:
        applyFaceDetector(self, param)
        self.closeWindows("Detecta")


def applyFaceDetector(self, param):
    try:
        face = findFaces(self.path, param)
    except:
        erroImp_Detecface()

    for (x0, y0, w1, h1) in face:
        self.marcas.append([x0, y0, w1, h1])
        self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)
        if self.VarLVetW:
            self.refreshMarkups()


def clearLogs(self):
    text_file= open("Illuminants.log", "w")
    text_file.write("")
    text_file.close()


#metadata
def w_readmetadata(self):
    if self.path != "":
        self.metadata = ""
        def sel():
            if var.get() == "Tag":
                erro_RetornoGenerico()
            else:
                textPad.config(state='normal')
                textPad.delete('1.0', END)
                self.metadata = propriedadesImagem(var.get(), self.path)
                textPad.insert('1.0', self.metadata)
                textPad.config(state=DISABLED)
                textPad.pack()

        self.metadatareader = Toplevel(self.interface)
        self.metadatareader.title("Metadata")
        self.metadatareader.resizable(width=TRUE, height=TRUE)

        self.metadatareader.geometry("%dx%d+%d+%d" % (400, 400, self.metadatareader.winfo_screenwidth() / 2 - 200,
                                                   self.metadatareader.winfo_screenmmheight() / 2 - 200))

        textPad = ScrolledText(self.metadatareader, width=self.metadatareader.winfo_screenwidth(), height=self.metadatareader.winfo_screenwidth())

        var = StringVar()
        R1 = Radiobutton(self.metadatareader, text="No decoded", variable=var, value="Nodecoded", command=sel)
        R1.pack(anchor=W)

        R2 = Radiobutton(self.metadatareader, text="Full", variable=var, value="Full", command=sel)
        R2.pack(anchor=W)

        R3 = Radiobutton(self.metadatareader, text="Simple", variable=var, value="Simple", command=sel)
        R3.pack(anchor=W)

        R4 = Radiobutton(self.metadatareader, text="Find Tag", variable=var, value="Tag", command=sel)
        #R4.pack(anchor=W)

        textPad.pack()

    else:
        erroImagemNaoCarregada()


def w_thumbnailviewer(self):

    var = IntVar()
    readconfigFile(self)
    def sel():
        canvas.delete("all")

        indice = (var.get())
        image = ImageTk.PhotoImage(Image.open(self.thumbs[indice]))
        canvas.create_image(0, 0, anchor=NW, image=image)
        thumbwindow.mainloop()
    clrthumbs()
    sizes = [72, 75, 100, 125, 150, 200]

    thumbwindow = Toplevel()
    thumbwindow.title("Thumbnail viewer")
    thumbwindow.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(thumbwindow)
    canvas.pack()
    Radiobutton(thumbwindow, text="72x72", variable=var, value=0, command=sel).pack()
    Radiobutton(thumbwindow, text="75x75", variable=var, value=1, command=sel).pack()
    Radiobutton(thumbwindow, text="100x100", variable=var, value=2, command=sel).pack()
    Radiobutton(thumbwindow, text="125x125", variable=var, value=3, command=sel).pack()
    Radiobutton(thumbwindow, text="150x150", variable=var, value=4, command=sel).pack()
    Radiobutton(thumbwindow, text="200x200", variable=var, value=5, command=sel).pack()

    try:
        for i in sizes:

                self.thumbs.append(thumbvwr(self.path, i, self.tbo))

        image = ImageTk.PhotoImage(Image.open(self.thumbs[0]))
        canvas.create_image(0, 0, anchor=NW, image=image)

    except:
        thumbwindow.destroy()
        erro_RetornoGenerico()
    thumbwindow.mainloop()

# report
def report_preparedata(self):
    readconfigFile(self)
    dados = []
    dados.append("path:" + str(self.path))
    dados.append("logo:" + str(self.logo))
    dados.append("company:" + str(self.id))
    dados.append("dpto:" + str(self.dpto))
    dados.append("user:" + str(self.user))
    dados.append("address:"+str(self.address))

    if self.exif == "True":

        if self.metadata == "":
            self.exif = "exif:" + str(propriedadesImagem(self.emode, self.path))
            dados.append(self.exif)
        else:
            self.exif = "exif:" + str(self.metadata)
            dados.append(self.exif)

    if self.face == "True":

        imagemarks = (os.path.join(os.path.abspath(os.path.dirname(__file__)) + "/data/reportgenerator/temp/img.jpg"))
        #self.canvas.postscript(file=imagemarks, colormode='color')
        ps = self.canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save(imagemarks)
        dados.append("mark " + str(self.marcas))

        if platform.system() == 'Windows':
            imagemarks= str(imagemarks.replace("\\", "/"))
            dados.append("markimg" + str(imagemarks))
        else:
            dados.append("markimg" + str(imagemarks))
    if self.thumb == "True":
        sizes = [72, 75, 100, 125, 150, 200]
        for i in sizes:
            try:
                caminhos ="thumbs:"+thumbvwr(self.path, i, self.tbo)
                dados.append(caminhos)
            except:
                pass
    # insert logs and data in report
    if self.illum == "True":

        # Insert Illuminants result LOG in report
        arquivo = open("Illuminants.log", "r")
        log = arquivo.read()
        arquivo.close()
        if log !="['\n']":
            illuminants = ("trdp:"+str(log))
            dados.append(illuminants)

    filelocation = commondialogbox("PDF")
    reportgenerator(filelocation, self.pagesize, self.margin, dados)

    #open file after creation

    if sys.platform == 'win32':
        os.startfile(filelocation)

    elif sys.platform == 'darwin':
        subprocess.Popen(['open', filelocation])

    else:
        try:
            subprocess.Popen(['xdg-open', filelocation])
        except OSError:
            pass


