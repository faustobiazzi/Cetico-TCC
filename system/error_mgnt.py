# system/error_mgnt.py
import tkinter as tk
from tkinter import messagebox

class ErrorManager:
    @classmethod
    def handle_error(cls, error_code, message): # Adicionado cls e decorador
        print(f"[{error_code}] {message}")
        messagebox.showerror(f"Erro {error_code}", message)

    @classmethod
    def log_info(cls, message):
        print(f"[INFO] {message}")

    @classmethod
    def show_error(cls, title, message, parent=None):
        messagebox.showerror(title, message, parent=parent)