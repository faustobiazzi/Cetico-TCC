# ui/face_detection_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from system.error_mgnt import ErrorManager # Importação centralizada
from system.faceDetection import detectFaces # Importação da função de detecção

class FaceDetectionWindow:
    def __init__(self, parent, app_instance):
        self.window = tk.Toplevel(parent)
        self.app = app_instance  # Referência ao Cético principal
        self.window.title("Configurar Detecção")
        self.window.geometry("500x450")
        self.window.resizable(False, False)
        self.window.grab_set()

        # Título
        ttk.Label(self.window, text="Detecção de Faces", font=("Arial", 16, "bold")).pack(pady=15)

        # Frame de configurações
        config_frame = ttk.LabelFrame(self.window, text="Configurações", padding=15)
        config_frame.pack(fill=tk.X, padx=20, pady=10)

        # Escala / Precisão
        ttk.Label(config_frame, text="Escala de Detecção:").grid(row=0, column=0, sticky="w", pady=5)
        self.scale_var = tk.DoubleVar(value=1.1)
        ttk.Spinbox(config_frame, from_=1.0, to=2.0, increment=0.05, 
                    textvariable=self.scale_var, width=10).grid(row=0, column=1, sticky="w", padx=10)

        # Número mínimo de vizinhos
        ttk.Label(config_frame, text="Vizinhos mínimos:").grid(row=1, column=0, sticky="w", pady=5)
        self.neighbors_var = tk.IntVar(value=5)
        ttk.Spinbox(config_frame, from_=1, to=10, increment=1,
                    textvariable=self.neighbors_var, width=10).grid(row=1, column=1, sticky="w", padx=10)

        # Botão Detectar
        detect_btn = ttk.Button(self.window, text="🔍 Iniciar Detecção de Faces", 
                                command=self.start_detection)
        detect_btn.pack(pady=20)

        # Área de log
        self.log_text = tk.Text(self.window, height=6, state="disabled", bg="#1e1e1e", fg="#00ff00", font=("Consolas", 9))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def start_detection(self):
        # 1. Busca o caminho da imagem (Prioridade para o Workspace)
        image_path = None
        if hasattr(self.app, 'workspace') and hasattr(self.app.workspace, 'current_path'):
            image_path = self.app.workspace.current_path
        elif hasattr(self.app, 'path'):
            image_path = self.app.path

        if not image_path:
            ErrorManager.handle_error("NO_IMAGE", "O sistema não localizou a imagem aberta.")
            return

        # 2. Coleta parâmetros da UI de forma segura
        try:
            params = [
                getattr(self, 'min_x_var', tk.IntVar(value=30)).get(),
                getattr(self, 'min_y_var', tk.IntVar(value=30)).get(),
                self.neighbors_var.get(),
                self.scale_var.get()
            ]
        except Exception as e:
            self.log(f"Erro nos parâmetros: {e}")
            return

        self.log(f"Iniciando OpenCV em: {image_path.split('/')[-1]}")

        # 3. Executa a detecção
        try:
            faces = detectFaces(image_path, params)
            
            if faces is not None and len(faces) > 0:
                self.log(f"Sucesso! {len(faces)} rostos identificados.")
                self.apply_results(faces)
            else:
                self.log("Nenhum rosto encontrado.")
                self.log("Dica: Tente Escala 1.05 e Vizinhos 3.")
                
        except Exception as e:
            self.log(f"Falha na execução: {str(e)}")
            ErrorManager.handle_error("DETECTION_FAIL", str(e))

    def apply_results(self, faces):
        # Acessa o canvas e a lista de marcas da aplicação
        # Ajustado para buscar o canvas dentro do workspace se necessário
        target_canvas = getattr(self.app.workspace, 'canvas', self.app.canvas)
        
        for (x, y, w, h) in faces:
            # Salva na lista global de marcas para futura análise/relatório
            self.app.marcas.append([x, y, w, h])
            
            # Desenha o retângulo no canvas visível
            target_canvas.create_rectangle(
                x, y, x + w, y + h, 
                outline=getattr(self.app, 'corAutoMark', 'red'), 
                width=2
            )
        
        # Opcional: Se tiver uma função de atualização de UI, chama aqui
        if hasattr(self.app, 'refreshMarkups'):
            self.app.refreshMarkups()
            
        self.window.destroy() # Fecha a janelinha de config após o sucesso

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"> {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")
        self.window.update_idletasks()