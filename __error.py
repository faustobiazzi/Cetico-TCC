# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016

@author: Fausto Biazzi de Sousa
@modulo: erros de sistema
@programa: "Cético"

"""
from tkinter import messagebox

def erroAbrirArquivo():
    try:
        messagebox.showerror("ERRO!", "Não foi possível carregar imagem.")
    except:
        print("ERRO!" , "Não foi possível carregar imagem.")
def erroImagemNaoCarregada():
    try:
        messagebox.showerror("ERRO!", "Não existe imagem carregada.")
    except:
        print("ERRO!" , "Não existe imagem carregada.")
def erroImp_Detecface():
    try:
        messagebox.showerror("ERRO!" , "Não foi possivel detectar faces")
    except:
        print("ERRO!", "Não foi possivel detectar faces")
def erroModuloGenérico():
    try:
        messagebox.showerror("ERRO!" , "Não executar o módulo selecionado.")
    except:
        print("ERRO!", "Não executar o módulo selecionado.")

def dialogofechar():
    try:
        if messagebox.askyesno("Sair", "tem certeza que deseja sair?"):
            exit()
    except:
        print("saindo do cético")        
        exit()



def erroExif():
    try:
        messagebox.showerror("Alerta!", "Não foi possível carregar as \npropriedades(EXIF) da imagem.")
    except:
        print ("Alerta!", "Não foi possível carregar as \npropriedades(EXIF) da imagem.")

def dialogo():
    try:
        messagebox.showerror("ERRO!" , "Função ainda não implementada.")
    except:
        print ("ERRO!", "Função ainda não implementada.")
    
     
def erro_RetornoGenerico():
    try:
        messagebox.showerror("ERRO!", "Não foi possivel retornar os dados")
    except:
        print ("ERRO!", "Não foi possivel retornar os dados.")