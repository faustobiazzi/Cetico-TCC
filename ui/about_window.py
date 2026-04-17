# ui/about_window.py
import tkinter as tk
from tkinter import ttk
from system.error_mgnt import ErrorManager

programa = "Cético"
versao = "Alpha 0.0.3.0"


class AboutWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title(f"Sobre o {programa} - {versao}")
        self.window.geometry("520x420")
        self.window.resizable(False, False)
        self.window.grab_set()          # torna modal
        
        # Título grande
        title = ttk.Label(self.window, 
                          text=programa,
                          font=("Arial", 28, "bold"),
                          foreground="#00ccff")
        title.pack(pady=(30, 5))

        version = ttk.Label(self.window, 
                            text=f"Versão {versao}",
                            font=("Arial", 10))
                            
        version.pack(pady=(0, 20))

        # Texto principal
        about_text = (
            "Cético é uma ferramenta desenvolvida para análise de imagens,\n"
            "detecção de faces, esteganografia e processamento visual.\n\n"
            "Desenvolvido por: Fausto Sousa\n"
            f"Versão atual: {versao}\n\n"
            "Este software ainda está em desenvolvimento."
        )

        text_label = ttk.Label(self.window, 
                               text=about_text,
                               font=("Arial", 11),
                               justify="center",
                               wraplength=450)
        text_label.pack(pady=10, padx=30)

        # Separador
        ttk.Separator(self.window, orient="horizontal").pack(fill="x", padx=40, pady=15)

        # Contato / Créditos
        contact = ttk.Label(self.window, 
                            text="Contato: fausto.sousa (ou seu email)\n"
                                 "GitHub / LinkedIn / etc.",
                            font=("Arial", 9),
                            foreground="#aaaaaa",
                            justify="center")
        contact.pack(pady=10)

        # Botão Fechar
        close_btn = ttk.Button(self.window, 
                        text="Fechar", 
                        command=self.close_window)
        # Atalho Esc
        self.window.bind("<Escape>", lambda e: self.window.destroy())

        # Centraliza a janela na tela
        self.center_window()
    
    def close_window(self):
        try:
            self.window.destroy()
        except Exception as e:
            ErrorManager.log_error("Erro ao fechar janela Sobre", e)

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")