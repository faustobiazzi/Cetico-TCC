# ui/menu.py
import tkinter as tk
from ui.face_detection_window import FaceDetectionWindow
from ui.stego_window import SteganographyWindow
from ui.about_window import AboutWindow
from system.error_mgnt import ErrorManager

class MenuBar:
    def __init__(self, root, main_app=None):
        self.root = root
        self.main_app = main_app

        self.menubar = tk.Menu(root)

        # ==================== ARQUIVO ====================
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Novo", command=lambda: print("TODO: Novo"))
        file_menu.add_command(label="Abrir Imagem / Vídeo...", command=self.open_media)          # <--- conectado
        file_menu.add_command(label="Salvar", command=lambda: print("TODO: Salvar"))
        file_menu.add_command(label="Salvar Como...", command=lambda: print("TODO: Salvar Como"))
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        self.menubar.add_cascade(label="Arquivo", menu=file_menu)
        
        # ==================== EDITAR ====================
        edit_menu = tk.Menu(self.menubar, tearoff=0)
        edit_menu.add_command(label="Desfazer", command=lambda: print("TODO: Desfazer"))
        edit_menu.add_command(label="Refazer", command=lambda: print("TODO: Refazer"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Copiar", command=lambda: print("TODO: Copiar"))
        edit_menu.add_command(label="Colar", command=lambda: print("TODO: Colar"))
        self.menubar.add_cascade(label="Editar", menu=edit_menu)

        # ==================== FERRAMENTAS ====================
        tools_menu = tk.Menu(self.menubar, tearoff=0)

        # Papiloscopia
        papiloscopia_menu = tk.Menu(tools_menu, tearoff=0)
        papiloscopia_menu.add_command(label="Análise de Impressões Digitais", 
                                      command=lambda: print("TODO: Papiloscopia"))
        tools_menu.add_cascade(label="Papiloscopia", menu=papiloscopia_menu)

        # Detecção facial
        tools_menu.add_command(label="Detectar Faces", command=lambda: FaceDetectionWindow(self.root, self.main_app)) # <--- Adicionado self.main_app
        tools_menu.add_command(label="Reconhecimento Facial", 
                               command=lambda: print("TODO: Face Recognition"))

        tools_menu.add_separator()

        # Análise de Imagem (submenu bem organizado)
        analise_menu = tk.Menu(tools_menu, tearoff=0)
        analise_menu.add_command(label="Análise Completa (Todos módulos)", 
                                 command=lambda: print("TODO: Análise completa"))
        analise_menu.add_command(label="Ler EXIF", 
                                 command=lambda: print("TODO: EXIF"))
        analise_menu.add_command(label="Visualizar Thumbnails", 
                                 command=lambda: print("TODO: Thumbnails"))
        analise_menu.add_separator()
        analise_menu.add_command(label="Copy-Move Detector", command=lambda: print("TODO: Copy-Move"))
        analise_menu.add_command(label="Análise de Erros / Compressão", command=lambda: print("TODO: Erros"))
        analise_menu.add_command(label="Análise de Iluminação (Illuminants)", command=lambda: print("TODO: Illuminants"))
        analise_menu.add_command(label="Análise de Ruído / Sombras / Reflexos", command=lambda: print("TODO: Ruído"))
        tools_menu.add_cascade(label="Análise de Imagem", menu=analise_menu)

        # Homografia
        homo_menu = tk.Menu(tools_menu, tearoff=0)
        homo_menu.add_command(label="RANSAC", command=lambda: print("TODO: RANSAC"))
        homo_menu.add_command(label="SIFT", command=lambda: print("TODO: SIFT"))
        tools_menu.add_cascade(label="Análise de Homografia", menu=homo_menu)

        tools_menu.add_separator()

        # Esteganografia
        stego_menu = tk.Menu(tools_menu, tearoff=0)
        stego_menu.add_command(label="Esconder Mensagem", 
                               command=lambda: SteganographyWindow(root, mode="hide"))
        stego_menu.add_command(label="Revelar Mensagem", 
                               command=lambda: SteganographyWindow(root, mode="reveal"))
        stego_menu.add_command(label="Navegador de Esteganografia", 
                               command=lambda: print("TODO: Navegador Estego"))
        stego_menu.add_command(label="Análise de Esteganografia", 
                               command=lambda: print("TODO: Análise Estego"))
        tools_menu.add_cascade(label="Esteganografia", menu=stego_menu)

        # Análise de Vídeo
        video_menu = tk.Menu(tools_menu, tearoff=0)
        video_menu.add_command(label="Análise Geral de Vídeo", command=lambda: print("TODO: Análise Vídeo"))
        video_menu.add_command(label="Detecção de Deepfake", command=lambda: print("TODO: Deepfake"))
        video_menu.add_command(label="Tracking de Objetos", command=lambda: print("TODO: Tracking"))
        video_menu.add_command(label="Cálculo de Velocidade", command=lambda: print("TODO: Velocidade"))
        video_menu.add_command(label="Reconhecimento Facial em Vídeo", command=lambda: print("TODO: Reconhecimento Vídeo"))
        tools_menu.add_cascade(label="Análise de Vídeo", menu=video_menu)
        #qrcode
        tools_menu.add_command(label="Análise de QR Codes", command=lambda: print("TODO: QR Code"))
        #nuDetection
        tools_menu.add_command(label="Análise de NuDetect", command=lambda: print("TODO: NuDetect")) #carrega janela de análise de nudez pode trabalhar em lote

        tools_menu.add_separator()
        tools_menu.add_command(label="Gerar Relatório Completo", command=lambda: print("TODO: Gerar Relatório"))
        tools_menu.add_separator()
        #ferramentas de terceiros
        tools_menu.add_command(label="Integrar com Ferramenta Externa1", state=tk.DISABLED, command=lambda: print("TODO: Integração Externa"))
        tools_menu.add_command(label="Integrar com Ferramenta Externa2", state=tk.DISABLED, command=lambda: print("TODO: Integração Externa"))
        tools_menu.add_command(label="Integrar com Ferramenta Externa3", state=tk.DISABLED, command=lambda: print("TODO: Integração Externa"))

        self.menubar.add_cascade(label="Ferramentas", menu=tools_menu)

        # ==================== VISUALIZAR ====================
        view_menu = tk.Menu(self.menubar, tearoff=0)
        view_menu.add_command(label="Zoom In",      command=self.zoom_in)
        view_menu.add_command(label="Zoom Out",     command=self.zoom_out)
        view_menu.add_command(label="Tamanho Real", command=self.reset_zoom)
        self.menubar.add_cascade(label="Visualizar", menu=view_menu)

        # ==================== AJUDA ====================
        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="Sobre o Cético", command=lambda: AboutWindow(self.root))
        self.menubar.add_cascade(label="Ajuda", menu=help_menu)

        # Aplica o menu
        root.config(menu=self.menubar)

    # Método exemplo (vamos usar depois)
       # Métodos que chamam o workspace
    def open_media(self):
        if self.main_app and hasattr(self.main_app, 'workspace'):
            self.main_app.workspace.open_media()
        else:
            ErrorManager.show_warning("Erro", "Workspace não encontrado.")

    def zoom_in(self):
        if self.main_app and hasattr(self.main_app, 'workspace'):
            self.main_app.workspace.zoom_in()

    def zoom_out(self):
        if self.main_app and hasattr(self.main_app, 'workspace'):
            self.main_app.workspace.zoom_out()

    def reset_zoom(self):
        if self.main_app and hasattr(self.main_app, 'workspace'):
            self.main_app.workspace.reset_zoom()