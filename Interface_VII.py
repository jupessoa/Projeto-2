# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:14:51 2016
@author: Vitória
"""
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tkm
from firebase import firebase

firebase = firebase.FirebaseApplication("https://sosfinal.firebaseio.com")

class InterfaceApp:
    def __init__(self):
        
        
        self.window = tk.Tk()
        self.window.geometry("400x600+150+50")
        self.window.title("SOS Now")
        self.window.rowconfigure(0, minsize=600)
        self.window.columnconfigure(0, minsize=400)
        self.window.wm_iconbitmap('iconee.ico')
        self.window.background = tk.PhotoImage(file="back2.png")
        self.window.logo = tk.PhotoImage(file="logo3.png")
        self.window.voltar = tk.PhotoImage(file="voltar2.png")
        
        
        # Tela de login
        
        self.login_screen = tk.Frame(self.window)
        self.login_screen.columnconfigure(0, minsize=80)
        self.login_screen.columnconfigure(1, minsize=80)
        self.login_screen.columnconfigure(2, minsize=80)
        self.login_screen.columnconfigure(3, minsize=80)
        self.login_screen.columnconfigure(4, minsize=80)
        self.login_screen.rowconfigure(0, minsize=60)
        self.login_screen.rowconfigure(1, minsize=60)
        self.login_screen.rowconfigure(2, minsize=60)
        self.login_screen.rowconfigure(3, minsize=60)
        self.login_screen.rowconfigure(4, minsize=60)
        self.login_screen.rowconfigure(5, minsize=60)
        self.login_screen.rowconfigure(6, minsize=60)
        self.login_screen.rowconfigure(7, minsize=60)
        self.login_screen.rowconfigure(8, minsize=60)
        self.login_screen.rowconfigure(9, minsize=60)
        
        self.login_screen.grid(row=0, column=0, sticky="nsew")
        
        self.background = tk.Label(self.login_screen, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.logo = tk.Label(self.login_screen, image= self.window.logo) #LOGO
        self.logo.grid(row=0, column=1, columnspan=3, sticky="nsew") #LOGO
        
        self.login = tk.Label(self.login_screen)
        self.login.grid(row=1, column=2, sticky="nsew")
        self.login.configure(text="Login")
        
        self.inserir_login = tk.Entry(self.login_screen)
        self.inserir_login.grid(row=2, column=1, columnspan=3, sticky="nsew")

        self.senha = tk.Label(self.login_screen)
        self.senha.grid(row=3, column=2, sticky="nsew")
        self.senha.configure(text="Senha")
        
        self.inserir_senha = tk.Entry(self.login_screen)
        self.inserir_senha.grid(row=4, column=1, columnspan=3, sticky="nsew")
        self.inserir_senha.configure(show="*")
        
        self.entrar = ttk.Button(self.login_screen)
        self.entrar.grid(row=6, column=2, sticky="nsew")
        self.entrar.configure(text="Entrar")
        self.entrar.configure(command=self.Tentativa_login)
        
        self.login = tk.Label(self.login_screen)
        self.login.grid(row=7, column=1, columnspan=3, sticky="nsew")
        self.login.configure(text="Ainda não possui uma conta?")        
        
        self.criar_novo_usuario = ttk.Button(self.login_screen)
        self.criar_novo_usuario.grid(row=8, column=2, sticky="nsew")
        self.criar_novo_usuario.configure(text="Cadastre-se")
        self.criar_novo_usuario.configure(command=self.novo_usuario)
        
        
         # Tela de novo usuário
        
        self.tela_novo_usuario = tk.Frame(self.window)
        self.tela_novo_usuario.columnconfigure(0, minsize=80)
        self.tela_novo_usuario.columnconfigure(1, minsize=80)
        self.tela_novo_usuario.columnconfigure(2, minsize=80)
        self.tela_novo_usuario.columnconfigure(3, minsize=80)
        self.tela_novo_usuario.columnconfigure(4, minsize=80)
        self.tela_novo_usuario.rowconfigure(0, minsize=60)
        self.tela_novo_usuario.rowconfigure(1, minsize=60)
        self.tela_novo_usuario.rowconfigure(2, minsize=60)
        self.tela_novo_usuario.rowconfigure(3, minsize=60)
        self.tela_novo_usuario.rowconfigure(4, minsize=60)
        self.tela_novo_usuario.rowconfigure(5, minsize=60)
        self.tela_novo_usuario.rowconfigure(6, minsize=60)
        self.tela_novo_usuario.rowconfigure(7, minsize=60)
        self.tela_novo_usuario.rowconfigure(8, minsize=60)
        self.tela_novo_usuario.rowconfigure(9, minsize=60)
                
        self.tela_novo_usuario.grid(row=0, column=0, sticky="nsew")
        
        self.background = tk.Label(self.tela_novo_usuario, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
                
        self.voltar_inicio = ttk.Button(self.tela_novo_usuario)
        self.voltar_inicio.grid(row=0, column=0, sticky="nsew")
        self.voltar_inicio.configure(text="Voltar")
        self.voltar_inicio.configure(command=self.voltar_pagina_inicial)        
        
        self.logo = tk.Label(self.tela_novo_usuario, image= self.window.logo) #LOGO
        self.logo.grid(row=1, column=1, columnspan=3, sticky="nsew") #LOGO
        
        self.nome_usuario = tk.Label(self.tela_novo_usuario)
        self.nome_usuario.grid(row=2, column=2, sticky="nsew")
        self.nome_usuario.configure(text="Insira um usuário:")
        
        self.inserir_nome_usuario = tk.Entry(self.tela_novo_usuario)
        self.inserir_nome_usuario.grid(row=3, column=1, columnspan=3, sticky="nsew")
        
        self.novo_nome_usuario = tk.StringVar(self.inserir_nome_usuario)
        
        self.criar_senha = tk.Label(self.tela_novo_usuario)
        self.criar_senha.grid(row=4, column=2, sticky="nsew")
        self.criar_senha.configure(text="Insira uma senha:")
        
        self.inserir_criar_senha = tk.Entry(self.tela_novo_usuario)
        self.inserir_criar_senha.grid(row=5, column=1, columnspan=3, sticky="nsew")
        self.inserir_criar_senha.configure(show="*")
                
        self.nova_senha = tk.StringVar(self.inserir_criar_senha)
        #self.nova_senha.getpass(self.inserir_criar_senha)
        
        self.condicao_senha = tk.Label(self.tela_novo_usuario)
        self.condicao_senha.grid(row=6, column=1, sticky="nsew")
        self.condicao_senha.configure(text="Mínimo 6 dígitos")
        
        self.salvar_novo_usuario = ttk.Button(self.tela_novo_usuario)
        self.salvar_novo_usuario.grid(row=8, column=2, sticky="nsew")
        self.salvar_novo_usuario.configure(text="Criar")
        self.salvar_novo_usuario.configure(command=self.cadastrar)
        
        
        # Tela de foruns       
              
        self.foruns = tk.Frame(self.window)
        self.foruns.columnconfigure(0, minsize=133)
        self.foruns.columnconfigure(1, minsize=133)
        self.foruns.columnconfigure(2, minsize=133)

        self.foruns.rowconfigure(0, minsize=60)
        self.foruns.rowconfigure(1, minsize=60)
        self.foruns.rowconfigure(2, minsize=60)
        self.foruns.rowconfigure(3, minsize=60)
        self.foruns.rowconfigure(4, minsize=60)
        self.foruns.rowconfigure(5, minsize=60)
        self.foruns.rowconfigure(6, minsize=60)
        self.foruns.rowconfigure(7, minsize=60)
        self.foruns.rowconfigure(8, minsize=60)
        self.foruns.rowconfigure(9, minsize=60)
        self.foruns.rowconfigure(10, minsize=60)
        self.foruns.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.background = tk.Label(self.foruns, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.logo = tk.Label(self.foruns, image= self.window.logo) #LOGO
        self.logo.grid(row=1, column=0, columnspan=3, sticky="nsew") #LOGO
        
        self.voltar_inicio = ttk.Button(self.foruns)
        self.voltar_inicio.grid(row=0, column=0, sticky="nsew")
        self.voltar_inicio.configure(text="Sair")
        self.voltar_inicio.configure(command=self.voltar_pagina_inicial)
    
        self.tema1 = ttk.Button(self.foruns)
        self.tema1.grid(row=3, column=1, sticky="nsew")
        self.tema1.configure(text="Relacionamento")
        self.tema1.configure(command=self.tema1_clicado)
        
        self.tema2 = ttk.Button(self.foruns)
        self.tema2.grid(row=4, column=1, sticky="nsew")
        self.tema2.configure(text="Vida profissional")
        self.tema2.configure(command=self.tema2_clicado)
        
        self.tema3 = ttk.Button(self.foruns)
        self.tema3.grid(row=5, column=1, sticky="nsew")
        self.tema3.configure(text="Amizade")
        self.tema3.configure(command=self.tema3_clicado)
        
        self.tema4 = ttk.Button(self.foruns)
        self.tema4.grid(row=6, column=1, sticky="nsew")
        self.tema4.configure(text="Viagens")
        self.tema4.configure(command=self.tema4_clicado)
        
        self.tema5 = ttk.Button(self.foruns)
        self.tema5.grid(row=7, column=1, sticky="nsew")
        self.tema5.configure(text="Saúde")
        self.tema5.configure(command=self.tema5_clicado)


        # Primeiro forum    
   
        self.janela1 = tk.Frame(self.window)
        self.janela1.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.janela1.columnconfigure(0, minsize=50)
        self.janela1.columnconfigure(1, minsize=50)
        self.janela1.columnconfigure(2, minsize=50)
        self.janela1.columnconfigure(3, minsize=50)
        self.janela1.columnconfigure(4, minsize=50)
        self.janela1.columnconfigure(5, minsize=50)
        self.janela1.columnconfigure(6, minsize=50)
        self.janela1.columnconfigure(7, minsize=50)
        
        self.janela1.rowconfigure(0, minsize=60)
        self.janela1.rowconfigure(1, minsize=60)
        self.janela1.rowconfigure(2, minsize=60)
        self.janela1.rowconfigure(3, minsize=60)
        self.janela1.rowconfigure(4, minsize=60)
        self.janela1.rowconfigure(5, minsize=60)
        self.janela1.rowconfigure(6, minsize=60)
        self.janela1.rowconfigure(7, minsize=60)
        self.janela1.rowconfigure(8, minsize=60)
        self.janela1.rowconfigure(9, minsize=60)
        
        self.background = tk.Label(self.janela1, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = ttk.Button(self.janela1)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar")
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema1 = tk.Label(self.janela1)
        self.titulo_tema1.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema1.configure(text="Relacionamento")
        
        #Página de comentários
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=80)
        self.comentarios.columnconfigure(1, minsize=80)
        self.comentarios.columnconfigure(2, minsize=80)
        self.comentarios.columnconfigure(3, minsize=80)
        self.comentarios.columnconfigure(4, minsize=80)
        self.comentarios.rowconfigure(0, minsize=60)
        self.comentarios.rowconfigure(1, minsize=60)
        self.comentarios.rowconfigure(2, minsize=60)
        self.comentarios.rowconfigure(3, minsize=60)
        self.comentarios.rowconfigure(4, minsize=60)
        self.comentarios.rowconfigure(5, minsize=60)
        self.comentarios.rowconfigure(6, minsize=60)
        self.comentarios.rowconfigure(7, minsize=60)
        self.comentarios.rowconfigure(8, minsize=60)
        self.comentarios.rowconfigure(9, minsize=60)
        self.comentarios.grid(row=0, column=0, sticky="nsew")
        
#        pergunta_responder = tk.Label(self.comentarios)
#        pergunta_responder.grid
        
        #Botão da primeira pergunta
        
        self.primeira_pergunta1 = ttk.Button(self.janela1)
        self.primeira_pergunta1.grid(row=4, column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta1.configure(text="")
        self.primeira_pergunta1.configure(command=self.entrar_pergunta)
        
        
        #Botão da segunda pergunta
        
        self.segunda_pergunta1 = ttk.Button(self.janela1)
        self.segunda_pergunta1.grid(row=5, column=1, columnspan=6, sticky="nsew")
        self.segunda_pergunta1.configure(text="")
        
        #Botão da terceira pergunta
        
        self.terceira_pergunta1 = ttk.Button(self.janela1)
        self.terceira_pergunta1.grid(row=6, column=1, columnspan=6, sticky="nsew")
        self.terceira_pergunta1.configure(text="")
        
        #Botão da quarta pergunta
        
        self.quarta_pergunta1 = ttk.Button(self.janela1)
        self.quarta_pergunta1.grid(row=7, column=1, columnspan=6, sticky="nsew")
        self.quarta_pergunta1.configure(text="")
        
        #Botão da quinta pergunta
        
        self.quinta_pergunta1 = ttk.Button(self.janela1)
        self.quinta_pergunta1.grid(row=8, column=1, columnspan=6, sticky="nsew")
        self.quinta_pergunta1.configure(text="")
        
        #Caixa de texto e pergunta feita        
        
        self.conteudo_texto1 = tk.StringVar(self.janela1)        
        
        self.perg_janela1 = tk.Entry(self.janela1)
        self.perg_janela1.grid(row=2, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_1 = tk.StringVar(self.janela1)
        
        # Botão perguntar

        self.botao_janela1 = ttk.Button(self.janela1)
        self.botao_janela1.grid(row=2, column=6, sticky="nsew")
        self.botao_janela1.configure(text="Perguntar", command=self.perguntar1)
        
        
        # Segundo forum        
        
        self.janela2 = tk.Frame(self.window)
        self.janela2.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.janela2.columnconfigure(0, minsize=50)
        self.janela2.columnconfigure(1, minsize=50)
        self.janela2.columnconfigure(2, minsize=50)
        self.janela2.columnconfigure(3, minsize=50)
        self.janela2.columnconfigure(4, minsize=50)
        self.janela2.columnconfigure(5, minsize=50)
        self.janela2.columnconfigure(6, minsize=50)
        self.janela2.columnconfigure(7, minsize=50)

        self.janela2.rowconfigure(0, minsize=60)
        self.janela2.rowconfigure(1, minsize=60)
        self.janela2.rowconfigure(2, minsize=60)
        self.janela2.rowconfigure(3, minsize=60)
        self.janela2.rowconfigure(4, minsize=60)
        self.janela2.rowconfigure(5, minsize=60)
        self.janela2.rowconfigure(6, minsize=60)
        self.janela2.rowconfigure(7, minsize=60)
        self.janela2.rowconfigure(8, minsize=60)
        self.janela2.rowconfigure(9, minsize=60)
        
        self.background = tk.Label(self.janela2, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = ttk.Button(self.janela2)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar")
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        #Botão da primeira pergunta

        self.primeira_pergunta2 = ttk.Button(self.janela2)
        self.primeira_pergunta2.grid(row=4, column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta2.configure(text="")
        
        #Botão da segunda pergunta
        
        self.segunda_pergunta2 = ttk.Button(self.janela2)
        self.segunda_pergunta2.grid(row=5, column=1, columnspan=6, sticky="nsew")
        self.segunda_pergunta2.configure(text="")
        
        #Botão da terceira pergunta
        
        self.terceira_pergunta2 = ttk.Button(self.janela2)
        self.terceira_pergunta2.grid(row=6, column=1, columnspan=6, sticky="nsew")
        self.terceira_pergunta2.configure(text="")
        
        #Botão da quarta pergunta
        
        self.quarta_pergunta2 = ttk.Button(self.janela2)
        self.quarta_pergunta2.grid(row=7, column=1, columnspan=6, sticky="nsew")
        self.quarta_pergunta2.configure(text="")
        
        #Botão da quinta pergunta
        
        self.quinta_pergunta2 = ttk.Button(self.janela2)
        self.quinta_pergunta2.grid(row=8, column=1, columnspan=6, sticky="nsew")
        self.quinta_pergunta2.configure(text="")
        
        #Caixa de texto e pergunta feita 
        
        self.conteudo_texto2 = tk.StringVar(self.janela2)        
        
        self.perg_janela2 = tk.Entry(self.janela2)
        self.perg_janela2.grid(row=2, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_2 = tk.StringVar(self.janela2)
        
        self.botao_janela2 = ttk.Button(self.janela2)
        self.botao_janela2.grid(row=2, column=6, sticky="nsew")
        self.botao_janela2.configure(text="Perguntar", command=self.perguntar2)
        
        self.titulo_tema2 = tk.Label(self.janela2)
        self.titulo_tema2.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema2.configure(text="Vida profissional")


        # Terceiro forum      
        
        self.janela3 = tk.Frame(self.window)
        self.janela3.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.janela3.columnconfigure(0, minsize=50)
        self.janela3.columnconfigure(1, minsize=50)
        self.janela3.columnconfigure(2, minsize=50)
        self.janela3.columnconfigure(3, minsize=50)
        self.janela3.columnconfigure(4, minsize=50)
        self.janela3.columnconfigure(5, minsize=50)
        self.janela3.columnconfigure(6, minsize=50)
        self.janela3.columnconfigure(7, minsize=50)
        
        self.janela3.rowconfigure(0, minsize=60)
        self.janela3.rowconfigure(1, minsize=60)
        self.janela3.rowconfigure(2, minsize=60)
        self.janela3.rowconfigure(3, minsize=60)
        self.janela3.rowconfigure(4, minsize=60)
        self.janela3.rowconfigure(5, minsize=60)
        self.janela3.rowconfigure(6, minsize=60)
        self.janela3.rowconfigure(7, minsize=60)
        self.janela3.rowconfigure(8, minsize=60)
        self.janela3.rowconfigure(9, minsize=60)
        
        self.background = tk.Label(self.janela3, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = ttk.Button(self.janela3)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar")
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema3 = tk.Label(self.janela3)
        self.titulo_tema3.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema3.configure(text="Amizade")
        
        #Botão da primeira pergunta

        self.primeira_pergunta3 = ttk.Button(self.janela3)
        self.primeira_pergunta3.grid(row=4, column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta3.configure(text="")
        
        #Botão da segunda pergunta
        
        self.segunda_pergunta3 = ttk.Button(self.janela3)
        self.segunda_pergunta3.grid(row=5, column=1, columnspan=6, sticky="nsew")
        self.segunda_pergunta3.configure(text="")
        
        #Botão da terceira pergunta
        
        self.terceira_pergunta3 = ttk.Button(self.janela3)
        self.terceira_pergunta3.grid(row=6, column=1, columnspan=6, sticky="nsew")
        self.terceira_pergunta3.configure(text="")
        
        #Botão da quarta pergunta
        
        self.quarta_pergunta3 = ttk.Button(self.janela3)
        self.quarta_pergunta3.grid(row=7, column=1, columnspan=6, sticky="nsew")
        self.quarta_pergunta3.configure(text="")
        
        #Botão da quinta pergunta
        
        self.quinta_pergunta3 = ttk.Button(self.janela3)
        self.quinta_pergunta3.grid(row=8, column=1, columnspan=6, sticky="nsew")
        self.quinta_pergunta3.configure(text="")
        
        #Caixa de texto e pergunta feita 
        
        self.conteudo_texto3 = tk.StringVar(self.janela3)        
        
        self.perg_janela3 = tk.Entry(self.janela3)
        self.perg_janela3.grid(row=2, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_3 = tk.StringVar(self.janela3)
        
        self.botao_janela3 = ttk.Button(self.janela3)
        self.botao_janela3.grid(row=2, column=6, sticky="nsew")
        self.botao_janela3.configure(text="Perguntar", command=self.perguntar3)
        
        
        # Quarto forum
        
        self.janela4 = tk.Frame(self.window)
        self.janela4.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.janela4.columnconfigure(0, minsize=50)
        self.janela4.columnconfigure(1, minsize=50)
        self.janela4.columnconfigure(2, minsize=50)
        self.janela4.columnconfigure(3, minsize=50)
        self.janela4.columnconfigure(4, minsize=50)
        self.janela4.columnconfigure(5, minsize=50)
        self.janela4.columnconfigure(6, minsize=50)
        self.janela4.columnconfigure(7, minsize=50)

        self.janela4.rowconfigure(0, minsize=60)
        self.janela4.rowconfigure(1, minsize=60)
        self.janela4.rowconfigure(2, minsize=60)
        self.janela4.rowconfigure(3, minsize=60)
        self.janela4.rowconfigure(4, minsize=60)
        self.janela4.rowconfigure(5, minsize=60)
        self.janela4.rowconfigure(6, minsize=60)
        self.janela4.rowconfigure(7, minsize=60)
        self.janela4.rowconfigure(8, minsize=60)
        self.janela4.rowconfigure(9, minsize=60) 
        
        self.background = tk.Label(self.janela4, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = ttk.Button(self.janela4)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar")
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema4 = tk.Label(self.janela4)
        self.titulo_tema4.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema4.configure(text="Viagens")
        
        #Botão da primeira pergunta

        self.primeira_pergunta4 = ttk.Button(self.janela4)
        self.primeira_pergunta4.grid(row=4, column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta4.configure(text="")
        
        #Botão da segunda pergunta
        
        self.segunda_pergunta4 = ttk.Button(self.janela4)
        self.segunda_pergunta4.grid(row=5, column=1, columnspan=6, sticky="nsew")
        self.segunda_pergunta4.configure(text="")
        
        #Botão da terceira pergunta
        
        self.terceira_pergunta4 = ttk.Button(self.janela4)
        self.terceira_pergunta4.grid(row=6, column=1, columnspan=6, sticky="nsew")
        self.terceira_pergunta4.configure(text="")
        
        #Botão da quarta pergunta
        
        self.quarta_pergunta4 = ttk.Button(self.janela4)
        self.quarta_pergunta4.grid(row=7, column=1, columnspan=6, sticky="nsew")
        self.quarta_pergunta4.configure(text="")
        
        #Botão da quinta pergunta
        
        self.quinta_pergunta4 = ttk.Button(self.janela4)
        self.quinta_pergunta4.grid(row=8, column=1, columnspan=6, sticky="nsew")
        self.quinta_pergunta4.configure(text="")
        
        #Caixa de texto e pergunta feita 
        
        self.conteudo_texto4 = tk.StringVar(self.janela4)        
        
        self.perg_janela4 = tk.Entry(self.janela4)
        self.perg_janela4.grid(row=2, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_4 = tk.StringVar(self.janela4)
        
        self.botao_janela4 = ttk.Button(self.janela4)
        self.botao_janela4.grid(row=2, column=6, sticky="nsew")
        self.botao_janela4.configure(text="Perguntar", command=self.perguntar4)
        
        
        # Quinto forum
        
        self.janela5 = tk.Frame(self.window)
        self.janela5.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.janela5.columnconfigure(0, minsize=50)
        self.janela5.columnconfigure(1, minsize=50)
        self.janela5.columnconfigure(2, minsize=50)
        self.janela5.columnconfigure(3, minsize=50)
        self.janela5.columnconfigure(4, minsize=50)
        self.janela5.columnconfigure(5, minsize=50)
        self.janela5.columnconfigure(6, minsize=50)
        self.janela5.columnconfigure(7, minsize=50)

        self.janela5.rowconfigure(0, minsize=60)
        self.janela5.rowconfigure(1, minsize=60)
        self.janela5.rowconfigure(2, minsize=60)
        self.janela5.rowconfigure(3, minsize=60)
        self.janela5.rowconfigure(4, minsize=60)
        self.janela5.rowconfigure(5, minsize=60)
        self.janela5.rowconfigure(6, minsize=60)
        self.janela5.rowconfigure(7, minsize=60)
        self.janela5.rowconfigure(8, minsize=60)
        self.janela5.rowconfigure(9, minsize=60)
        
        self.background = tk.Label(self.janela5, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = ttk.Button(self.janela5)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar")
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema5 = tk.Label(self.janela5)
        self.titulo_tema5.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema5.configure(text="Saúde")
        
        #Botão da primeira pergunta

        self.primeira_pergunta5 = ttk.Button(self.janela5)
        self.primeira_pergunta5.grid(row=4, column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta5.configure(text="")
        
        #Botão da segunda pergunta
        
        self.segunda_pergunta5 = ttk.Button(self.janela5)
        self.segunda_pergunta5.grid(row=5, column=1, columnspan=6, sticky="nsew")
        self.segunda_pergunta5.configure(text="")
        
        #Botão da terceira pergunta
        
        self.terceira_pergunta5 = ttk.Button(self.janela5)
        self.terceira_pergunta5.grid(row=6, column=1, columnspan=6, sticky="nsew")
        self.terceira_pergunta5.configure(text="")
        
        #Botão da quarta pergunta
        
        self.quarta_pergunta5 = ttk.Button(self.janela5)
        self.quarta_pergunta5.grid(row=7, column=1, columnspan=6, sticky="nsew")
        self.quarta_pergunta5.configure(text="")
        
        #Botão da quinta pergunta
        
        self.quinta_pergunta5 = ttk.Button(self.janela5)
        self.quinta_pergunta5.grid(row=8, column=1, columnspan=6, sticky="nsew")
        self.quinta_pergunta5.configure(text="")
        
        #Caixa de texto e pergunta feita 
        
        self.conteudo_texto5 = tk.StringVar(self.janela5)        
        
        self.perg_janela5 = tk.Entry(self.janela5)
        self.perg_janela5.grid(row=2, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_5 = tk.StringVar(self.janela5)
        
        self.conteudo_label5 = tk.StringVar(self.janela5)
                
        
        self.botao_janela5 = ttk.Button(self.janela5)
        self.botao_janela5.grid(row=2, column=6, sticky="nsew")
        self.botao_janela5.configure(text="Perguntar", command=self.perguntar5)
        
        
        self.login_screen.tkraise()
        
        self.numero_perguntas1 = 0
        self.numero_perguntas2 = 0
        self.numero_perguntas3 = 0
        self.numero_perguntas4 = 0
        self.numero_perguntas5 = 0
        
        
    def iniciar(self):
        self.window.mainloop()
        
    def entrar_app(self):
        self.foruns.tkraise()
        
    def novo_usuario(self):
        self.tela_novo_usuario.tkraise()
    
    def cadastrar(self):
        cadastro_usuario = self.inserir_nome_usuario.get()
        cadastro_senha = self.inserir_criar_senha.get()
        
        #dicionario_1 = firebase.get("/Cadastro", "/{0}".format(cadastro_usuario))
        
        #if cadastro_usuario == dicionario_1["usuario"]:
            #self.janela_erro_1 = tkm.showinfo("SOS Now","Usuário já existente. Tente novamente!")
        
        #else:
        firebase.put("/Cadastro/", name = cadastro_usuario, data = {'usuario': cadastro_usuario , 'senha': cadastro_senha})
        self.janela_sucesso = tkm.showinfo("SOS Now", "Cadastro realizado com sucesso!")
        self.limpa_cadastro()
        
    def limpa_cadastro(self):
        if self.janela_sucesso == "ok":
            self.voltar_pagina_inicial()
        
    def Tentativa_login(self):
        Usuario = self.inserir_login.get()
        senha = self.inserir_senha.get()
        
        dicionario_2 = firebase.get("/Cadastro", "/{0}".format(Usuario))
                
        if Usuario == dicionario_2["usuario"] and senha == dicionario_2["senha"]:
            self.entrar_app()
        
        else:
            self.janela_erro_2 = tkm.showinfo("SOS Now","Usuário e/ou senha inválidos. Tente novamente!")
        
        
    def tema1_clicado(self):
        self.janela1.tkraise()
        
    def tema2_clicado(self):
        self.janela2.tkraise()
        
    def tema3_clicado(self):
        self.janela3.tkraise()
        
    def tema4_clicado(self):
        self.janela4.tkraise()
        
    def tema5_clicado(self):
        self.janela5.tkraise()
        
    def perguntar1(self):

        if self.numero_perguntas1 == 0:
            self.primeira_pergunta1.configure(text=self.perg_janela1.get())
            self.numero_perguntas1 += 1
            
        elif self.numero_perguntas1 == 1:
            self.segunda_pergunta1.configure(text=self.perg_janela1.get())
            self.numero_perguntas1 += 1
            
        elif self.numero_perguntas1 == 2:
            self.terceira_pergunta1.configure(text=self.perg_janela1.get())
            self.numero_perguntas1 += 1
            
        elif self.numero_perguntas1 == 3:
            self.quarta_pergunta1.configure(text=self.perg_janela1.get())
            self.numero_perguntas1 += 1
            
        elif self.numero_perguntas1 == 4:
            self.quinta_pergunta1.configure(text=self.perg_janela1.get())
            self.numero_perguntas1 +=1
        
        
    def perguntar2(self):
        
        if self.numero_perguntas2 == 0:
            self.primeira_pergunta2.configure(text=self.perg_janela2.get())
            self.numero_perguntas2 += 1
            
        elif self.numero_perguntas2 == 1:
            self.segunda_pergunta2.configure(text=self.perg_janela2.get())
            self.numero_perguntas2 += 1
            
        elif self.numero_perguntas2 == 2:
            self.terceira_pergunta2.configure(text=self.perg_janela2.get())
            self.numero_perguntas2 += 1
            
        elif self.numero_perguntas2 == 3:
            self.quarta_pergunta2.configure(text=self.perg_janela2.get())
            self.numero_perguntas2 += 1
            
        elif self.numero_perguntas2 == 4:
            self.quinta_pergunta2.configure(text=self.perg_janela2.get())
            self.numero_perguntas2 +=1
        
    def perguntar3(self):
        
        if self.numero_perguntas3 == 0:
            self.primeira_pergunta3.configure(text=self.perg_janela3.get())
            self.numero_perguntas3 += 1
            
        elif self.numero_perguntas3 == 1:
            self.segunda_pergunta3.configure(text=self.perg_janela3.get())
            self.numero_perguntas3 += 1
            
        elif self.numero_perguntas3 == 2:
            self.terceira_pergunta3.configure(text=self.perg_janela3.get())
            self.numero_perguntas3 += 1
            
        elif self.numero_perguntas3 == 3:
            self.quarta_pergunta3.configure(text=self.perg_janela3.get())
            self.numero_perguntas3 += 1
            
        elif self.numero_perguntas3 == 4:
            self.quinta_pergunta3.configure(text=self.perg_janela3.get())
            self.numero_perguntas3 +=1
    
    def perguntar4(self):
        
        if self.numero_perguntas4 == 0:
            self.primeira_pergunta4.configure(text=self.perg_janela4.get())
            self.numero_perguntas4 += 1
            
        elif self.numero_perguntas4 == 1:
            self.segunda_pergunta4.configure(text=self.perg_janela4.get())
            self.numero_perguntas4 += 1
            
        elif self.numero_perguntas4 == 2:
            self.terceira_pergunta4.configure(text=self.perg_janela4.get())
            self.numero_perguntas4 += 1
            
        elif self.numero_perguntas4 == 3:
            self.quarta_pergunta4.configure(text=self.perg_janela4.get())
            self.numero_perguntas4 += 1
            
        elif self.numero_perguntas4 == 4:
            self.quinta_pergunta4.configure(text=self.perg_janela4.get())
            self.numero_perguntas4 +=1
            
    def perguntar5(self):
        
        if self.numero_perguntas5 == 0:
            self.primeira_pergunta5.configure(text=self.perg_janela5.get())
            self.numero_perguntas5 += 1
            
        elif self.numero_perguntas5 == 1:
            self.segunda_pergunta5.configure(text=self.perg_janela5.get())
            self.numero_perguntas5 += 1
            
        elif self.numero_perguntas5 == 2:
            self.terceira_pergunta5.configure(text=self.perg_janela5.get())
            self.numero_perguntas5 += 1
            
        elif self.numero_perguntas5 == 3:
            self.quarta_pergunta5.configure(text=self.perg_janela5.get())
            self.numero_perguntas5 += 1
            
        elif self.numero_perguntas5 == 4:
            self.quinta_pergunta5.configure(text=self.perg_janela5.get())
            self.numero_perguntas5 +=1
            
    def entrar_pergunta(self):
        self.comentarios.tkraise()
        
    def voltar_pagina_inicial(self):
        self.login_screen.tkraise()
        
    def voltar_aos_foruns(self):
        self.foruns.tkraise()

app = InterfaceApp()
app.iniciar()