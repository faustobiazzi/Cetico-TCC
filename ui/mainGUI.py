# ui/mainGUI.py
import tkinter as tk
from tkinter import ttk
from ui.menu import MenuBar
from ui.toolbar import ToolBar
from ui.workspace import Workspace
from system.error_mgnt import ErrorManager

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cético - TCC")
        self.root.geometry("1100x750")
        self.root.configure(bg="#2b2b2b")

        # Variáveis de MARCAÇÃO DO FACE DETECTION
        self.path = "" 
        self.marcas = []
        self.corAutoMark = "red" # Cor padrão para os retângulos

        # Menu
        self.menu = MenuBar(root, main_app=self)

        # Toolbar
        self.toolbar = ToolBar(root, main_app=self)

        # Frame principal (conteúdo)
        self.main_frame = ttk.Frame(root, padding=5)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas / Área de trabalho (placeholder por enquanto)
        self.workspace = Workspace(self.main_frame, main_app=self)

        # Label de status no rodapé
        self.status_bar = ttk.Label(root, text=" Pronto - Modo quebra-galho | Python 3.7 ", 
                                    relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind da tecla Esc pra fechar (opcional)
        self.root.bind("<Escape>", lambda e: root.quit())

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()