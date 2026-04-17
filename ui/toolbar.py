# ui/toolbar.py
import tkinter as tk
from tkinter import ttk
from system.error_mgnt import ErrorManager

class ToolBar:
    def __init__(self, parent, main_app=None):
        self.parent = parent
        self.main_app = main_app

        self.toolbar = ttk.Frame(parent, relief="raised", padding=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Botões da toolbar (ícones simulados com texto por enquanto)
        btn_new = ttk.Button(self.toolbar, text="Novo", width=6, command=lambda: print("TODO: Novo"))
        btn_new.pack(side=tk.LEFT, padx=2, pady=2)

        btn_open = ttk.Button(self.toolbar, text="Abrir", width=6, command=lambda: print("TODO: Abrir"))
        btn_open.pack(side=tk.LEFT, padx=2, pady=2)

        btn_save = ttk.Button(self.toolbar, text="Salvar", width=6, command=lambda: print("TODO: Salvar"))
        btn_save.pack(side=tk.LEFT, padx=2, pady=2)

        ttk.Separator(self.toolbar, orient="vertical").pack(side=tk.LEFT, fill=tk.Y, padx=4, pady=4)

        btn_analyze = ttk.Button(self.toolbar, text="Analisar Img", width=10,
                                 command=lambda: print("TODO: Análise de Imagem"))
        btn_analyze.pack(side=tk.LEFT, padx=2, pady=2)

        btn_stego = ttk.Button(self.toolbar, text="Esteganografia", width=18,
                               command=lambda: print("TODO: Esteganografia"))
        btn_stego.pack(side=tk.LEFT, padx=2, pady=2)

        btn_illuminants = ttk.Button(self.toolbar, text="Illuminants", width=10,
                                     command=lambda: print("TODO: Conversão Illuminants"))
        btn_illuminants.pack(side=tk.LEFT, padx=2, pady=2)

        ttk.Separator(self.toolbar, orient="vertical").pack(side=tk.LEFT, fill=tk.Y, padx=4, pady=4)

        btn_zoom_in = ttk.Button(self.toolbar, text="🔎 +", width=4, command=lambda: print("TODO: Zoom In"))
        btn_zoom_in.pack(side=tk.LEFT, padx=2, pady=2)

        btn_zoom_out = ttk.Button(self.toolbar, text="🔎 -", width=4, command=lambda: print("TODO: Zoom Out"))
        btn_zoom_out.pack(side=tk.LEFT, padx=2, pady=2)