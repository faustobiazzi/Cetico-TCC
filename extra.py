from error import *
from services import *


# acesso a módulos de terceiros
def illuminants(self):
    self.resultIlluminants = []
    if self.VarIllum == False:
        if self.path != "":
            if self.marcas != [] and len(self.marcas) > 1:
                try:
                    janelaIlluminants(self)
                    self.VarIllum = True
                except NameError:
                    erroModuloGenerico(str(NameError))
            else:
                erro_Illuminants()
        else:
            erroImagemNaoCarregada()


def janelaIlluminants(self):

    sub = self

    def extrairDescritoresdaImagem(_self, v1, v2, v3, v4, v5, v6, v7, v8, v9, v0):
        comando = []
        if v0:
            comando = ["acc", "bic", "ccv", "eoac", "las", "lch", "sasi", "spytec", "unser"]

        else:
            if v1:
                comando.append("acc")

            if v2:
                comando.append("bic")

            if v3:
                comando.append("ccv")

            if v4:
                comando.append("eoac")

            if v5:
                comando.append("las")

            if v6:
                comando.append("lch")

            if v7:
                comando.append("sasi")

            if v8:
                comando.append("spytec")

            if v9:
                comando.append("UNSER")
        sub.resultIlluminants = resultado = Moduloilluminant(comando, self.path, self.marcas)
        janelaResultado(_self, resultado)
        _self.closeWindows("Illuminants")

    def janelaResultado(_self, resultado):

        outClassification, votesNormal, votesFake, finalClass = resultado

        normal = IntVar()
        normal.set(votesNormal)
        fake = IntVar()
        fake.set(votesFake)
        final = IntVar()
        final.set(finalClass)
        # saida = IntVar()
        # saida.set(outClassification)

        _self.j_Resultilluminants = Toplevel(self.interface)
        _self.j_Resultilluminants.title("Resultado")
        _self.j_Resultilluminants.wm_protocol("WM_DELETE_WINDOW",
                                              lambda: _self.closeWindows("resultadoIllu"))
        _self.j_Resultilluminants.resizable(width=FALSE, height=FALSE)
        Label(_self.j_Resultilluminants, text="Resultado:", anchor=CENTER)
        Label(_self.j_Resultilluminants, text="Normal :").grid(column=0, row=1)
        Label(_self.j_Resultilluminants, text="Modificada :").grid(column=0, row=2)
        Label(_self.j_Resultilluminants, text="Classificação Final:").grid(column=0, row=3)
        Label(_self.j_Resultilluminants, textvariable=normal).grid(column=1, row=1)
        Label(_self.j_Resultilluminants, textvariable=fake).grid(column=1, row=2)
        Label(_self.j_Resultilluminants, textvariable=final).grid(column=1, row=3)
        # Label(_self.j_Resultilluminants, textvariable = saida).grid(column=1, row=4)
        Button(_self.j_Resultilluminants, underline=0, text=u"Fechar",
               command=lambda: _self.closeWindows("resultadoIllu")).grid(row=5, column=1)

    def janelaModulosExtracao(_self):

        def executar():
            extrairDescritoresdaImagem(_self, var1.get(), var2.get(), var3.get(), var4.get(), var5.get(),
                                       var6.get(), var7.get(), var8.get(), var9.get(), var0.get())

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
        _self.j_illuminants.wm_protocol("WM_DELETE_WINDOW", lambda: _self.closeWindows("Illuminants"))
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
        Button(_self.j_illuminants, underline=0, text=u"Cancelar",
               command=lambda: _self.closeWindows("Illuminants")).grid(row=10, column=1)
        Button(_self.j_illuminants, underline=2, text=u"Executar",
               command=executar).grid(row=10, column=2)

    janelaModulosExtracao(self)