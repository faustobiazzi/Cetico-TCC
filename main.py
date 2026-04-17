# main.py
import sys
import os
from system.error_mgnt import ErrorManager

'''
@author: Fausto Biazzi de Sousa
@modulo: interface gráfica Cético + funções.
'''

# Adiciona o diretório atual ao path pra importar os módulos da ui
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from ui.mainGUI import MainGUI
except ImportError as e:
    print(f"Erro ao importar GUI: {e}")
    print("Verifique se a pasta ui/ existe e se mainGUI.py está dentro dela.")
    sys.exit(1)

if __name__ == "__main__":
    import tkinter as tk
    
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()