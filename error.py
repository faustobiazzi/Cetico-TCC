# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:03:58 2016
Modified on Sun Sep 18 08:42:55 2016
@author: Fausto Biazzi de Sousa
@modulo: erros de sistema
@programa: "Cético"

"""
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import os

def erroOpenFile():
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
def erroModuloGenerico(erro):
    try:
        messagebox.showerror("ERRO!" , "Não executar o módulo selecionado. ("+erro+")")
    except:
        print("ERRO!", "Não executar o módulo selecionado.")


def closeImageDialog():
    try:
        if messagebox.askyesno("Fechar Imagem", "tem certeza que deseja abrir uma nova imagem?\n "
                                                "As marcações e modificações já realizadas serão perdidas"):
            return 1
    except:
        print("Imagem fechada!", "selecione uma nova imagem para trabalho.")

def closeAPPDialog():
    try:
        if messagebox.askyesno("Sair", "tem certeza que deseja sair?"):
            exit()
    except:
        exit()

def funcaoIndisponivel(sistema):
    try:
        messagebox.showerror("Alerta!", "Não é possivel executar essa função\n "
                             "Esse recurso ainda nao foi portado para o sistema "+sistema+".")
    except:
        print ("Alerta!", "Não foi possível carregar as \npropriedades(EXIF) da imagem.")

def erroExif():
    try:
        messagebox.showerror("Alerta!", "Não foi possível carregar as \npropriedades(EXIF) da imagem.")
    except:
        print ("Alerta!", "Não foi possível carregar as \npropriedades(EXIF) da imagem.")


def dialogo():
    try:
        messagebox.showerror("ERRO!", "Função ainda não implementada.")
    except:
        print ("ERRO!", "Função ainda não implementada.")
    
def errorCode(code, message):
    try:
        messagebox.showerror("ERRO! "+code+"", "Não foi possivel retornar os dados"+message+"")
    except:
        print("ERRO!"+code+"Não foi possivel retornar os dados"+message+"")

def erro_RetornoGenerico():
    try:
        messagebox.showerror("ERRO!", "Não foi possivel retornar os dados")
    except:
        print("ERRO!", "Não foi possivel retornar os dados.")

def erro_Illuminants():
    try:
        messagebox.showerror("Illuminants!", "Não existem marcações na imagem.\n Marque os pontos a serem analisados antes de entrar na função")
    except:
        print ("ERRO!", "Há marcações suficientes na imagem. Marque ao menos dois pontos a serem analisados antes de entrar na função.")

def analiseIlluminantsterminada():
    try:
        messagebox.showwarning("Illuminants!",
                             "Extração Concluida.")
    except:
        print("Aviso!",
              "Extração concluida.")
