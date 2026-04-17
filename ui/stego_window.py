# ui/stego_window.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from system.error_mgnt import ErrorManager

class SteganographyWindow:
    def __init__(self, parent, mode="hide"):
        self.window = tk.Toplevel(parent)
        self.mode = mode
        self.window.title("Esteganografia - Esconder Mensagem" if mode == "hide" else "Esteganografia - Revelar Mensagem")
        self.window.geometry("560x480")
        self.window.grab_set()

        title = "Esconder Mensagem na Imagem" if mode == "hide" else "Revelar Mensagem da Imagem"
        ttk.Label(self.window, text=title, font=("Arial", 16, "bold")).pack(pady=15)

        # Frame principal
        main_f = ttk.Frame(self.window, padding=15)
        main_f.pack(fill=tk.BOTH, expand=True)

        if mode == "hide":
            # Imagem original
            ttk.Label(main_f, text="Imagem Original:").pack(anchor="w")
            self.img_path = tk.StringVar()
            ttk.Entry(main_f, textvariable=self.img_path, width=60).pack(fill=tk.X, pady=5)
            ttk.Button(main_f, text="Selecionar Imagem", command=self.select_image).pack(anchor="w")

            # Mensagem
            ttk.Label(main_f, text="Mensagem para esconder:").pack(anchor="w", pady=(15,5))
            self.message_text = tk.Text(main_f, height=6)
            self.message_text.pack(fill=tk.X, pady=5)

        else:  # reveal mode
            ttk.Label(main_f, text="Imagem com mensagem escondida:").pack(anchor="w")
            self.img_path = tk.StringVar()
            ttk.Entry(main_f, textvariable=self.img_path, width=60).pack(fill=tk.X, pady=5)
            ttk.Button(main_f, text="Selecionar Imagem", command=self.select_image).pack(anchor="w")

        # Botão principal
        btn_text = "Esconder Mensagem" if mode == "hide" else "Revelar Mensagem"
        action_btn = ttk.Button(self.window, text=btn_text, command=self.execute)
        action_btn.pack(pady=20)

    def select_image(self):
        path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.bmp")])
        if path:
            self.img_path.set(path)

    def execute(self):
        if not self.img_path.get():
            messagebox.showwarning("Atenção", "Selecione uma imagem primeiro!")
            return

        if self.mode == "hide":
            msg = self.message_text.get("1.0", tk.END).strip()
            if not msg:
                messagebox.showwarning("Atenção", "Digite uma mensagem para esconder!")
                return
            messagebox.showinfo("Esteganografia", f"Mensagem de {len(msg)} caracteres pronta para esconder.\n\n(Função ainda não implementada)")
        else:
            messagebox.showinfo("Esteganografia", "Iniciando revelação da mensagem...\n\n(Função ainda não implementada)")