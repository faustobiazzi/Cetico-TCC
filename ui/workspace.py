# ui/workspace.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from pathlib import Path
from system.error_mgnt import ErrorManager

class Workspace:
    """Área de trabalho única e inteligente para imagens e vídeos"""

    def __init__(self, parent, main_app=None):
        self.parent = parent
        self.main_app = main_app

        self.current_mode = None      # "image" ou "video"
        self.current_media = None     # PIL Image ou caminho do vídeo

        # Frame principal da área de trabalho
        self.frame = ttk.LabelFrame(parent, text=" Área de Trabalho ", padding=5)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # Canvas base (único)
        self.canvas = tk.Canvas(self.frame, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Variáveis para imagem
        self.photo_image = None
        self.image_id = None
        self.zoom_factor = 1.0

        # Variáveis para vídeo
        self.cap = None               # cv2.VideoCapture
        self.video_playing = False
        self.current_frame = None

        # Bindings básicos
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

    # ====================== MODO IMAGEM ======================
    def load_image(self, image_path):
        self.current_path = image_path
        """Carrega uma imagem estática"""
        try:
            self.clear()
            self.current_mode = "image"
            self.current_media = Image.open(image_path)

            self.frame.config(text=f" Imagem: {Path(image_path).name} ")
            self.fit_image_to_canvas()

            ErrorManager.log_info(f"Imagem carregada: {image_path}")
            return True

        except Exception as e:
            ErrorManager.show_error("Erro ao carregar imagem", str(e), parent=self.parent)
            ErrorManager.log_error("Falha ao carregar imagem", e)
            return False

    def fit_image_to_canvas(self):
        if not self.current_media or self.current_mode != "image":
            return

        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()

        if canvas_w < 20 or canvas_h < 20:
            return

        img_w, img_h = self.current_media.size
        ratio = min(canvas_w / img_w, canvas_h / img_h) * 0.95

        new_size = (int(img_w * ratio), int(img_h * ratio))
        resized = self.current_media.resize(new_size, Image.Resampling.LANCZOS)

        self.photo_image = ImageTk.PhotoImage(resized)
        self.zoom_factor = ratio

        if self.image_id:
            self.canvas.delete(self.image_id)

        self.image_id = self.canvas.create_image(
            canvas_w // 2, canvas_h // 2,
            image=self.photo_image,
            anchor=tk.CENTER
        )

    # ====================== MODO VÍDEO ======================
    def load_video(self, video_path: str):
        """Carrega um arquivo de vídeo"""
        try:
            self.clear()
            self.current_mode = "video"
            self.cap = cv2.VideoCapture(video_path)
            self.frame.config(text=f" Vídeo: {Path(video_path).name} ")

            if not self.cap.isOpened():
                raise Exception("Não foi possível abrir o vídeo")

            self.show_first_frame()
            self.show_video_controls()
            self.update_timeline()
            ErrorManager.log_info(f"Vídeo carregado: {video_path}")
            return True

        except Exception as e:
            ErrorManager.show_error("Erro ao carregar vídeo", str(e))
            return False

    def show_first_frame(self):
        if not self.cap:
            return
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
            self.display_frame(frame)

    def display_frame(self, frame):
        """Converte frame do OpenCV para exibir no Tkinter"""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_frame)
        
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()

        ratio = min(canvas_w / pil_img.width, canvas_h / pil_img.height) * 0.95
        new_size = (int(pil_img.width * ratio), int(pil_img.height * ratio))
        
        resized = pil_img.resize(new_size, Image.Resampling.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(resized)

        if self.image_id:
            self.canvas.delete(self.image_id)

        self.image_id = self.canvas.create_image(
            canvas_w // 2, canvas_h // 2,
            image=self.photo_image, anchor=tk.CENTER
        )

    # ====================== CONTROLES GERAIS ======================
    def clear(self):
        """Limpa tudo"""
        self.canvas.delete("all")
        self.photo_image = None
        self.image_id = None
        self.zoom_factor = 1.0

        if self.cap:
            self.cap.release()
            self.cap = None

        self.current_mode = None
        self.current_media = None
        self.hide_video_controls()
        self.frame.config(text=" Área de Trabalho ")
        

    def on_resize(self, event):
        if self.current_mode == "image" and self.current_media:
            self.fit_image_to_canvas()
        elif self.current_mode == "video" and self.current_frame is not None:
            self.display_frame(self.current_frame)

    def on_mousewheel(self, event):
        if self.current_mode == "image":
            # Zoom para imagem
            if event.delta > 0:
                self.zoom_factor *= 1.1
            else:
                self.zoom_factor /= 1.1
            self.zoom_factor = max(0.1, min(self.zoom_factor, 10.0))
            self.fit_image_to_canvas()

    # ====================== MÉTODOS FUTUROS ======================
    def play_video(self):
        """Implementar reprodução de vídeo depois"""
        pass

    def pause_video(self):
        pass

        # ====================== ZOOM ======================
    def zoom_in(self):
        """Zoom +"""
        if self.current_mode == "image" and self.current_media:
            self.zoom_factor *= 1.15
            self.zoom_factor = min(self.zoom_factor, 10.0)
            self.fit_image_to_canvas()

    def zoom_out(self):
        """Zoom -"""
        if self.current_mode == "image" and self.current_media:
            self.zoom_factor /= 1.15
            self.zoom_factor = max(self.zoom_factor, 0.1)
            self.fit_image_to_canvas()

    def reset_zoom(self):
        """Voltar ao zoom original"""
        if self.current_mode == "image" and self.current_media:
            self.zoom_factor = 1.0
            self.fit_image_to_canvas()

    # ====================== ABRIR MÍDIA ======================
    def open_media(self):
        """Abre diálogo para selecionar imagem ou vídeo"""
        from tkinter import filedialog

        filetypes = [
            ("Imagens e Vídeos", "*.png *.jpg *.jpeg *.bmp *.mp4 *.avi *.mov"),
            ("Imagens", "*.png *.jpg *.jpeg *.bmp"),
            ("Vídeos", "*.mp4 *.avi *.mov"),
            ("Todos os arquivos", "*.*")
        ]

        filepath = filedialog.askopenfilename(
            title="Abrir Imagem ou Vídeo",
            filetypes=filetypes
        )

        if not filepath:
            return False

        # Detecta automaticamente o tipo pelo extensão
        ext = Path(filepath).suffix.lower()

        if ext in ['.png', '.jpg', '.jpeg', '.bmp']:
            return self.load_image(filepath)
        elif ext in ['.mp4', '.avi', '.mov']:
            return self.load_video(filepath)
        else:
            ErrorManager.show_warning("Formato não suportado", 
                                    f"Formato {ext} não é suportado no momento.")
            return False
        
        # ====================== CONTROLES DE VÍDEO ======================
    def create_video_controls(self):
        """Cria o painel de controles de vídeo (aparece só quando vídeo está carregado)"""
        if hasattr(self, 'video_control_frame') and self.video_control_frame:
            self.video_control_frame.destroy()

        self.video_control_frame = ttk.Frame(self.frame)
        self.video_control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(5, 0))

        # Botões de controle
        btn_prev = ttk.Button(self.video_control_frame, text="⏮ Frame Anterior", 
                              command=self.prev_frame)
        btn_prev.pack(side=tk.LEFT, padx=2)

        self.btn_play = ttk.Button(self.video_control_frame, text="▶ Play", 
                                   command=self.toggle_play)
        self.btn_play.pack(side=tk.LEFT, padx=2)

        btn_next = ttk.Button(self.video_control_frame, text="Frame Seguinte ⏭", 
                              command=self.next_frame)
        btn_next.pack(side=tk.LEFT, padx=2)

        # Timeline (Slider)
        self.timeline_var = tk.DoubleVar(value=0)
        self.timeline = ttk.Scale(self.video_control_frame, 
                                  from_=0, to=100, 
                                  orient=tk.HORIZONTAL,
                                  variable=self.timeline_var,
                                  command=self.seek_frame)
        self.timeline.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        # Label de status do vídeo
        self.video_status_label = ttk.Label(self.video_control_frame, text="00:00 / 00:00")
        self.video_status_label.pack(side=tk.RIGHT, padx=5)

        # Esconde os controles inicialmente
        self.video_control_frame.pack_forget()

    def show_video_controls(self):
        """Mostra os controles quando um vídeo é carregado"""
        if not hasattr(self, 'video_control_frame') or not self.video_control_frame:
            self.create_video_controls()
        self.video_control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(5, 0))

    def hide_video_controls(self):
        """Esconde os controles quando não é vídeo"""
        if hasattr(self, 'video_control_frame') and self.video_control_frame:
            self.video_control_frame.pack_forget()

    # ====================== FUNÇÕES DE VÍDEO ======================
    def toggle_play(self):
        """Play/Pause (por enquanto só placeholder - vamos implementar frame a frame depois)"""
        if self.current_mode != "video" or not self.cap:
            return
        self.video_playing = not self.video_playing
        self.btn_play.config(text="⏸ Pause" if self.video_playing else "▶ Play")
        print("Play/Pause clicado - Implementação frame a frame em breve")

    def next_frame(self):
        """Avança para o próximo frame"""
        if self.current_mode != "video" or not self.cap:
            return

        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
            self.display_frame(frame)
            self.update_timeline()
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # volta pro início

    def prev_frame(self):
        """Volta um frame"""
        if self.current_mode != "video" or not self.cap:
            return

        current_pos = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, current_pos - 2))
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
            self.display_frame(frame)
            self.update_timeline()

    def seek_frame(self, value):
        """Seek pela timeline"""
        if self.current_mode != "video" or not self.cap:
            return
        total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        target_frame = int(float(value) / 100 * total_frames)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
            self.display_frame(frame)

    def update_timeline(self):
        """Atualiza a posição da timeline"""
        if not self.cap:
            return
        current = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        total = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        if total > 0:
            progress = (current / total) * 100
            self.timeline_var.set(progress)

            # Atualiza label de tempo (simples)
            fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
            current_sec = current / fps
            total_sec = total / fps
            self.video_status_label.config(
                text=f"{current_sec:.1f}s / {total_sec:.1f}s"
            )