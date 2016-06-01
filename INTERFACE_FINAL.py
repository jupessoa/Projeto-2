# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:12:29 2016

@author: Vitória
"""

from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tkm
#from firebase import firebase

#firebase = firebase.FirebaseApplication("https://sosfinal.firebaseio.com")

class InterfaceApp:
    def __init__(self):
        
        
        self.window = tk.Tk()
        self.window.geometry("400x600+150+50")
        self.window.title("SOS Now")
        self.window.rowconfigure(0, minsize=600)
        self.window.columnconfigure(0, minsize=400)
        self.window.wm_iconbitmap('iconee.ico')
        self.window.background = tk.PhotoImage(file="2222.png")
        self.window.logo = tk.PhotoImage(file="logo4.png")
        self.window.resizable(False,False)
        
        
        # Tela de login
        
        self.login_screen = tk.Frame(self.window)
        self.login_screen.columnconfigure(0, minsize=80)
        self.login_screen.columnconfigure(1, minsize=80)
        self.login_screen.columnconfigure(2, minsize=80)
        self.login_screen.columnconfigure(3, minsize=80)
        self.login_screen.columnconfigure(4, minsize=80)
        self.login_screen.rowconfigure(0, minsize=45)
        self.login_screen.rowconfigure(1, minsize=45)
        self.login_screen.rowconfigure(2, minsize=45)
        self.login_screen.rowconfigure(3, minsize=45)
        self.login_screen.rowconfigure(4, minsize=45)
        self.login_screen.rowconfigure(5, minsize=45)
        self.login_screen.rowconfigure(6, minsize=45)
        self.login_screen.rowconfigure(7, minsize=45)
        self.login_screen.rowconfigure(8, minsize=45)
        self.login_screen.rowconfigure(9, minsize=45)
        self.login_screen.rowconfigure(10, minsize=45)
        self.login_screen.rowconfigure(11, minsize=45)
        self.login_screen.rowconfigure(12, minsize=45)
                
        self.login_screen.grid(row=0, column=0, sticky="nsew")
        
        self.background = tk.Label(self.login_screen, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.logo = tk.Label(self.login_screen, image= self.window.logo) #LOGO
        self.logo.grid(row=1, column=1, columnspan=3, sticky="nsew") #LOGO
        
        self.login = tk.Label(self.login_screen)
        self.login.grid(row=3, column=2, sticky="nsew")
        self.login.configure(text="Login", font =('AR ESSENCE', '16', 'bold') , fg = 'black')
        
        self.inserir_login = tk.Entry(self.login_screen)
        self.inserir_login.grid(row=4, column=1, columnspan=3, sticky="nsew")

        self.senha = tk.Label(self.login_screen)
        self.senha.grid(row=5, column=2, sticky="nsew")
        self.senha.configure(text="Senha", font =('AR ESSENCE', '16', 'bold') , fg = 'black')
        
        self.inserir_senha = tk.Entry(self.login_screen)
        self.inserir_senha.grid(row=6, column=1, columnspan=3, sticky="nsew")
        self.inserir_senha.configure(show="*")
        
        self.entrar = tk.Button(self.login_screen)
        self.entrar.grid(row=8, column=2, sticky="nsew")
        self.entrar.configure(text="Entrar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.entrar.configure(command=self.Tentativa_login)
        
        self.login = tk.Label(self.login_screen)
        self.login.grid(row=10, column=1, columnspan=3, sticky="nsew")
        self.login.configure(text="Ainda não possui uma conta?", font =('AR ESSENCE', '12', 'bold') , fg = 'black')        
        
        self.criar_novo_usuario = tk.Button(self.login_screen)
        self.criar_novo_usuario.grid(row=11, column=2, sticky="nsew")
        self.criar_novo_usuario.configure(text="Cadastre-se", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.criar_novo_usuario.configure(command=self.novo_usuario)
        
        
         # Tela de novo usuário
        
        self.tela_novo_usuario = tk.Frame(self.window)
        self.tela_novo_usuario.columnconfigure(0, minsize=80)
        self.tela_novo_usuario.columnconfigure(1, minsize=80)
        self.tela_novo_usuario.columnconfigure(2, minsize=80)
        self.tela_novo_usuario.columnconfigure(3, minsize=80)
        self.tela_novo_usuario.columnconfigure(4, minsize=80)
        self.tela_novo_usuario.rowconfigure(0, minsize=45)
        self.tela_novo_usuario.rowconfigure(1, minsize=45)
        self.tela_novo_usuario.rowconfigure(2, minsize=45)
        self.tela_novo_usuario.rowconfigure(3, minsize=45)
        self.tela_novo_usuario.rowconfigure(4, minsize=45)
        self.tela_novo_usuario.rowconfigure(5, minsize=45)
        self.tela_novo_usuario.rowconfigure(6, minsize=45)
        self.tela_novo_usuario.rowconfigure(7, minsize=45)
        self.tela_novo_usuario.rowconfigure(8, minsize=45)
        self.tela_novo_usuario.rowconfigure(9, minsize=45)
        self.tela_novo_usuario.rowconfigure(10, minsize=45)
        self.tela_novo_usuario.rowconfigure(11, minsize=45)
        self.tela_novo_usuario.rowconfigure(12, minsize=45)
                
        self.tela_novo_usuario.grid(row=0, column=0, sticky="nsew")
        
        self.background = tk.Label(self.tela_novo_usuario, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
                
        self.voltar_inicio = tk.Button(self.tela_novo_usuario)
        self.voltar_inicio.grid(row=0, column=0, sticky="nsew")
        #self.voltar_inicio.configure(image = self.window.voltar)
        self.voltar_inicio.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_inicio.configure(command=self.voltar_pagina_inicial)        
        
        self.logo = tk.Label(self.tela_novo_usuario, image= self.window.logo) #LOGO
        self.logo.grid(row=2, column=1, columnspan=3, sticky="nsew") #LOGO
        
        self.nome_usuario = tk.Label(self.tela_novo_usuario)
        self.nome_usuario.grid(row=4, column=2, sticky="nsew")
        self.nome_usuario.configure(text="Insira um usuário:", font =('AR ESSENCE', '12') , fg = 'black')
        
        self.inserir_nome_usuario = tk.Entry(self.tela_novo_usuario)
        self.inserir_nome_usuario.grid(row=5, column=1, columnspan=3, sticky="nsew")
        
        self.novo_nome_usuario = tk.StringVar(self.inserir_nome_usuario)
        
        self.criar_senha = tk.Label(self.tela_novo_usuario)
        self.criar_senha.grid(row=6, column=2, sticky="nsew")
        self.criar_senha.configure(text="Insira uma senha:", font =('AR ESSENCE', '12') , fg = 'black')
        
        self.inserir_criar_senha = tk.Entry(self.tela_novo_usuario)
        self.inserir_criar_senha.grid(row=7, column=1, columnspan=3, sticky="nsew")
        self.inserir_criar_senha.configure(show="*")
                
        self.nova_senha = tk.StringVar(self.inserir_criar_senha)
                
        self.condicao_senha = tk.Label(self.tela_novo_usuario)
        self.condicao_senha.grid(row=8, column=1, sticky="nsew")
        self.condicao_senha.configure(text="Mínimo 6 dígitos", font =('Arial', '7', 'bold') , fg = 'black')
        
        self.salvar_novo_usuario = tk.Button(self.tela_novo_usuario)
        self.salvar_novo_usuario.grid(row=10, column=2, sticky="nsew")
        self.salvar_novo_usuario.configure(text="Criar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.salvar_novo_usuario.configure(command=self.cadastrar)
        
        
        # Tela de foruns       
              
        self.foruns = tk.Frame(self.window)
        self.foruns.columnconfigure(0, minsize=80)
        self.foruns.columnconfigure(1, minsize=80)
        self.foruns.columnconfigure(2, minsize=80)
        self.foruns.columnconfigure(3, minsize=80)
        self.foruns.columnconfigure(4, minsize=80)

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
        self.logo.grid(row=1, column=1, columnspan=3, sticky="nsew") #LOGO
        
        self.voltar_inicio = tk.Button(self.foruns)
        self.voltar_inicio.grid(row=0, column=0, sticky="nsew")
        self.voltar_inicio.configure(text="Sair", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_inicio.configure(command=self.voltar_pagina_inicial)
    
        self.tema1 = tk.Button(self.foruns)
        self.tema1.grid(row=3, column=1, columnspan=3, sticky="nsew")
        self.tema1.configure(text="Relacionamento", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.tema1.configure(command=self.tema1_clicado)
        
        self.tema2 = tk.Button(self.foruns)
        self.tema2.grid(row=4, column=1, columnspan=3, sticky="nsew")
        self.tema2.configure(text="Trabalho", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.tema2.configure(command=self.tema2_clicado)
        
        self.tema3 = tk.Button(self.foruns)
        self.tema3.grid(row=5, column=1, columnspan=3, sticky="nsew")
        self.tema3.configure(text="Amizade", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.tema3.configure(command=self.tema3_clicado)
        
        self.tema4 = tk.Button(self.foruns)
        self.tema4.grid(row=6, column=1, columnspan=3, sticky="nsew")
        self.tema4.configure(text="Viagens", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.tema4.configure(command=self.tema4_clicado)
        
        self.tema5 = tk.Button(self.foruns)
        self.tema5.grid(row=7, column=1, columnspan=3, sticky="nsew")
        self.tema5.configure(text="Saúde", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.tema5.configure(command=self.tema5_clicado)
        
        self.tema6 = tk.Button(self.foruns)
        self.tema6.grid(row=8, column=1, columnspan=3, sticky="nsew")
        self.tema6.configure(text="Família", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.tema6.configure(command=self.tema6_clicado)

        
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
        self.janela1.rowconfigure(0, minsize=45)
        self.janela1.rowconfigure(1, minsize=45)
        self.janela1.rowconfigure(2, minsize=45)
        self.janela1.rowconfigure(3, minsize=45)
        self.janela1.rowconfigure(4, minsize=45)
        self.janela1.rowconfigure(5, minsize=45)
        self.janela1.rowconfigure(6, minsize=45)
        self.janela1.rowconfigure(7, minsize=45)
        self.janela1.rowconfigure(8, minsize=45)
        self.janela1.rowconfigure(9, minsize=45)
        self.janela1.rowconfigure(10, minsize=45)
        self.janela1.rowconfigure(11, minsize=45)
        
        self.background = tk.Label(self.janela1, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = tk.Button(self.janela1)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema1 = tk.Label(self.janela1)
        self.titulo_tema1.grid(row=2, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema1.configure(text="Relacionamento")
        
        # Perguntar        
        
        self.conteudo_texto1 = tk.StringVar(self.janela1)        
        
        self.perg_janela1 = tk.Entry(self.janela1)
        self.perg_janela1.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_1 = tk.StringVar(self.janela1)
        
        self.botao_janela1 = tk.Button(self.janela1)
        self.botao_janela1.grid(row=4, column=6, sticky="nsew")
        self.botao_janela1.configure(text="Perguntar", command=self.perguntar_forum1, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        
       
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
        self.janela2.rowconfigure(0, minsize=45)
        self.janela2.rowconfigure(1, minsize=45)
        self.janela2.rowconfigure(2, minsize=45)
        self.janela2.rowconfigure(3, minsize=45)
        self.janela2.rowconfigure(4, minsize=45)
        self.janela2.rowconfigure(5, minsize=45)
        self.janela2.rowconfigure(6, minsize=45)
        self.janela2.rowconfigure(7, minsize=45)
        self.janela2.rowconfigure(8, minsize=45)
        self.janela2.rowconfigure(9, minsize=45)
        self.janela2.rowconfigure(10, minsize=45)
        self.janela2.rowconfigure(11, minsize=45)
        
        self.background = tk.Label(self.janela2, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = tk.Button(self.janela2)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema2 = tk.Label(self.janela2)
        self.titulo_tema2.grid(row=2, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema2.configure(text="Trabalho")
        
        # Perguntar 
        
        self.conteudo_texto2 = tk.StringVar(self.janela2)        
        
        self.perg_janela2 = tk.Entry(self.janela2)
        self.perg_janela2.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_2 = tk.StringVar(self.janela2)
        
        self.botao_janela2 = tk.Button(self.janela2)
        self.botao_janela2.grid(row=4, column=6, sticky="nsew")
        self.botao_janela2.configure(text="Perguntar", command=self.perguntar_forum2, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        
              
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
        self.janela3.rowconfigure(0, minsize=45)
        self.janela3.rowconfigure(1, minsize=45)
        self.janela3.rowconfigure(2, minsize=45)
        self.janela3.rowconfigure(3, minsize=45)
        self.janela3.rowconfigure(4, minsize=45)
        self.janela3.rowconfigure(5, minsize=45)
        self.janela3.rowconfigure(6, minsize=45)
        self.janela3.rowconfigure(7, minsize=45)
        self.janela3.rowconfigure(8, minsize=45)
        self.janela3.rowconfigure(9, minsize=45)
        self.janela3.rowconfigure(10, minsize=45)
        self.janela3.rowconfigure(11, minsize=45)
        
        self.background = tk.Label(self.janela3, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = tk.Button(self.janela3)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema3 = tk.Label(self.janela3)
        self.titulo_tema3.grid(row=2, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema3.configure(text="Amizade")
        
         # Perguntar 
        
        self.conteudo_texto3 = tk.StringVar(self.janela3)        
        
        self.perg_janela3 = tk.Entry(self.janela3)
        self.perg_janela3.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_3 = tk.StringVar(self.janela3)
        
        self.botao_janela3 = tk.Button(self.janela3)
        self.botao_janela3.grid(row=4, column=6, sticky="nsew")
        self.botao_janela3.configure(text="Perguntar", command=self.perguntar_forum3, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        
        
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
        self.janela4.rowconfigure(0, minsize=45)
        self.janela4.rowconfigure(1, minsize=45)
        self.janela4.rowconfigure(2, minsize=45)
        self.janela4.rowconfigure(3, minsize=45)
        self.janela4.rowconfigure(4, minsize=45)
        self.janela4.rowconfigure(5, minsize=45)
        self.janela4.rowconfigure(6, minsize=45)
        self.janela4.rowconfigure(7, minsize=45)
        self.janela4.rowconfigure(8, minsize=45)
        self.janela4.rowconfigure(9, minsize=45)
        self.janela4.rowconfigure(10, minsize=45)
        self.janela4.rowconfigure(11, minsize=45) 
        
        self.background = tk.Label(self.janela4, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = tk.Button(self.janela4)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema4 = tk.Label(self.janela4)
        self.titulo_tema4.grid(row=2, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema4.configure(text="Viagens")
        
        # Perguntar 
        
        self.conteudo_texto4 = tk.StringVar(self.janela4)        
        
        self.perg_janela4 = tk.Entry(self.janela4)
        self.perg_janela4.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_4 = tk.StringVar(self.janela4)
        
        self.botao_janela4 = tk.Button(self.janela4)
        self.botao_janela4.grid(row=4, column=6, sticky="nsew")
        self.botao_janela4.configure(text="Perguntar", command=self.perguntar_forum4, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        
        
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
        self.janela5.rowconfigure(0, minsize=45)
        self.janela5.rowconfigure(1, minsize=45)
        self.janela5.rowconfigure(2, minsize=45)
        self.janela5.rowconfigure(3, minsize=45)
        self.janela5.rowconfigure(4, minsize=45)
        self.janela5.rowconfigure(5, minsize=45)
        self.janela5.rowconfigure(6, minsize=45)
        self.janela5.rowconfigure(7, minsize=45)
        self.janela5.rowconfigure(8, minsize=45)
        self.janela5.rowconfigure(9, minsize=45)
        self.janela5.rowconfigure(10, minsize=45)
        self.janela5.rowconfigure(11, minsize=45)
        
        self.background = tk.Label(self.janela5, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = tk.Button(self.janela5)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema5 = tk.Label(self.janela5)
        self.titulo_tema5.grid(row=2, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema5.configure(text="Saúde")
        
        # Perguntar 
        
        self.conteudo_texto5 = tk.StringVar(self.janela5)        
        
        self.perg_janela5 = tk.Entry(self.janela5)
        self.perg_janela5.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_5 = tk.StringVar(self.janela5)
        
        self.conteudo_label5 = tk.StringVar(self.janela5)
                
        self.botao_janela5 = tk.Button(self.janela5)
        self.botao_janela5.grid(row=4, column=6, sticky="nsew")
        self.botao_janela5.configure(text="Perguntar", command=self.perguntar_forum5, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        
        
        # Sexto forum
        
        self.janela6 = tk.Frame(self.window)
        self.janela6.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.janela6.columnconfigure(0, minsize=50)
        self.janela6.columnconfigure(1, minsize=50)
        self.janela6.columnconfigure(2, minsize=50)
        self.janela6.columnconfigure(3, minsize=50)
        self.janela6.columnconfigure(4, minsize=50)
        self.janela6.columnconfigure(5, minsize=50)
        self.janela6.columnconfigure(6, minsize=50)
        self.janela6.columnconfigure(7, minsize=50)
        self.janela6.rowconfigure(0, minsize=45)
        self.janela6.rowconfigure(1, minsize=45)
        self.janela6.rowconfigure(2, minsize=45)
        self.janela6.rowconfigure(3, minsize=45)
        self.janela6.rowconfigure(4, minsize=45)
        self.janela6.rowconfigure(5, minsize=45)
        self.janela6.rowconfigure(6, minsize=45)
        self.janela6.rowconfigure(7, minsize=45)
        self.janela6.rowconfigure(8, minsize=45)
        self.janela6.rowconfigure(9, minsize=45)
        self.janela6.rowconfigure(10, minsize=45)
        self.janela6.rowconfigure(11, minsize=45)
        
        self.background = tk.Label(self.janela6, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
        
        self.voltar_foruns = tk.Button(self.janela6)
        self.voltar_foruns.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_foruns.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_foruns.configure(command=self.voltar_aos_foruns)
        
        self.titulo_tema6 = tk.Label(self.janela6)
        self.titulo_tema6.grid(row=2, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema6.configure(text="Família")
        
        # Perguntar 
        
        self.conteudo_texto6 = tk.StringVar(self.janela6)        
        
        self.perg_janela6 = tk.Entry(self.janela6)
        self.perg_janela6.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_6 = tk.StringVar(self.janela6)
        
        self.conteudo_label6 = tk.StringVar(self.janela6)
                
        self.botao_janela6 = tk.Button(self.janela6)
        self.botao_janela6.grid(row=4, column=6, sticky="nsew")
        self.botao_janela6.configure(text="Perguntar", command=self.perguntar_forum6)
        
        
        # Números    
        
        self.login_screen.tkraise()
        
        self.numero_perguntas_1 = 6
        self.numero_perguntas_2 = 6
        self.numero_perguntas_3 = 6
        self.numero_perguntas_4 = 6
        self.numero_perguntas_5 = 6
        self.numero_perguntas_6 = 6
        
        self.numero_respostas1 = 6
        self.numero_respostas2 = 6
        self.numero_respostas3 = 6
        self.numero_respostas4 = 6
        self.numero_respostas5 = 6
        self.numero_respostas6 = 6
        
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        self.x5 = 0
        self.x6 = 0
       
       
    def iniciar(self):
        self.window.mainloop()
        
    def entrar_app(self):
        self.foruns.tkraise()
                    
    def novo_usuario(self):
        self.tela_novo_usuario.tkraise()
    
    def cadastrar(self):
        cadastro_usuario = self.inserir_nome_usuario.get()
        cadastro_senha = self.inserir_criar_senha.get()
        
        dicionario_1 = firebase.get("/Cadastro", "/{0}".format(cadastro_usuario))
        
        if dicionario_1 != None:
            self.janela_erro_1 = tkm.showinfo("SOS Now","Usuário já existente. Tente novamente!")
            if self.janela_erro_1 == "ok" or self.janela_erro_1 == "enter":
                self.novo_usuario()
            
        elif len(cadastro_senha) < 6:
            self.janela_erro_2 = tkm.showinfo("SOS Now","Senha muito curta. Tente novamente!")
            if self.janela_erro_2 == "ok" or self.janela_erro_2 == "enter":
                self.novo_usuario()
        
        else: 
            firebase.put("/Cadastro/", name = cadastro_usuario, data = {'usuario': cadastro_usuario , 'senha': cadastro_senha})
            self.janela_sucesso = tkm.showinfo("SOS Now", "Cadastro realizado com sucesso!")
            self.depois_cadastro()
        
                
    def depois_cadastro(self):
        if self.janela_sucesso == "ok" or self.janela_sucesso == "enter":
            self.voltar_pagina_inicial()
        
        
    def Tentativa_login(self):
        Usuario = self.inserir_login.get()
        senha = self.inserir_senha.get()
        
        dicionario_2 = firebase.get("/Cadastro", "/{0}".format(Usuario))
                
        if dicionario_2 != None:
            if senha == dicionario_2["senha"]:
                self.entrar_app()
                return
                
        self.janela_erro_3 = tkm.showinfo("SOS Now","Usuário e/ou senha inválidos. Tente novamente!")
        
        if self.janela_erro_3 == "ok" or self.janela_erro_3 == "enter":
                self.voltar_pagina_inicial()
        
        
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
    
    def tema6_clicado(self):
        self.janela6.tkraise()
        
   
    def perguntar_forum1(self):
        self.primeira_pergunta1 = tk.Button(self.janela1)
        self.primeira_pergunta1.grid(row="{0}".format(self.numero_perguntas_1), column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta1.configure(text="")
        self.numero_perguntas_1 += 1
        forum1 = self.perg_janela1.get()
        self.primeira_pergunta1.configure(text=forum1)
        self.primeira_pergunta1.configure(command=self.entrar_pergunta1)
        
        firebase.put("/Foruns/Relacionamento/", name = forum1, data = {})
        
             
    def perguntar_forum2(self):
        self.primeira_pergunta2 = tk.Button(self.janela2)
        self.primeira_pergunta2.grid(row="{0}".format(self.numero_perguntas_2), column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta2.configure(text="")
        self.numero_perguntas_2 += 1
        forum2 = self.perg_janela2.get()
        self.primeira_pergunta2.configure(text=forum2)
        self.primeira_pergunta2.configure(command=self.entrar_pergunta2)
        
        firebase.put("/Foruns/Trabalho/", name = forum2, data = {})
                    
        
    def perguntar_forum3(self):
        self.primeira_pergunta3 = tk.Button(self.janela3)
        self.primeira_pergunta3.grid(row="{0}".format(self.numero_perguntas_3), column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta3.configure(text="")
        self.numero_perguntas_3 += 1
        forum3 = self.perg_janela3.get()
        self.primeira_pergunta3.configure(text=forum3)
        self.primeira_pergunta3.configure(command=self.entrar_pergunta3)
                
        firebase.put("/Foruns/Amizade/", name = forum3, data = {})
                    
    
    def perguntar_forum4(self):
        self.primeira_pergunta4 = tk.Button(self.janela4)
        self.primeira_pergunta4.grid(row="{0}".format(self.numero_perguntas_4), column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta4.configure(text="")
        self.numero_perguntas_4 += 1
        forum4 = self.perg_janela4.get()
        self.primeira_pergunta4.configure(text=forum4)
        self.primeira_pergunta4.configure(command=self.entrar_pergunta4)
        
        firebase.put("/Foruns/Viagens/", name = forum4, data = {})
                    
    
    def perguntar_forum5(self):
        self.primeira_pergunta5 = tk.Button(self.janela5)
        self.primeira_pergunta5.grid(row="{0}".format(self.numero_perguntas_5), column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta5.configure(text="")
        self.numero_perguntas_5 += 1
        forum5 = self.perg_janela5.get()
        self.primeira_pergunta5.configure(text=forum5)
        self.primeira_pergunta5.configure(command=self.entrar_pergunta5)
        
        firebase.put("/Foruns/Saude/", name = forum5, data = {})
        
    
    def perguntar_forum6(self):
        self.primeira_pergunta6 = tk.Button(self.janela6)
        self.primeira_pergunta6.grid(row="{0}".format(self.numero_perguntas_6), column=1, columnspan=6, sticky="nsew")
        self.primeira_pergunta6.configure(text="")
        self.numero_perguntas_6 += 1
        forum6 = self.perg_janela6.get()
        self.primeira_pergunta6.configure(text=forum6)
        self.primeira_pergunta6.configure(command=self.entrar_pergunta6)
        
        firebase.put("/Foruns/Familia/", name = forum6, data = {})
        
    
    def responder1(self):
        self.primeira_resposta = tk.Label(self.comentarios)
        self.primeira_resposta.grid(row="{0}".format(self.numero_respostas1), column=1, columnspan=6, sticky="nsew")
        self.primeira_resposta.configure(text="")
        self.numero_respostas1 += 1
        self.primeira_resposta.configure(text=self.comentario_espaco.get())
        
        forum1 = self.perg_janela1.get()
        resposta1 = self.comentario_espaco.get()
        firebase.put("/Foruns/Relacionamento/", name = "{0}".format(forum1), data = {'{0}'.format(self.x1): resposta1})
        self.x1 += 1
        
    
    def responder2(self):
        self.primeira_resposta = tk.Label(self.comentarios)
        self.primeira_resposta.grid(row="{0}".format(self.numero_respostas2), column=1, columnspan=6, sticky="nsew")
        self.primeira_resposta.configure(text="")
        self.numero_respostas2 += 1
        self.primeira_resposta.configure(text=self.comentario_espaco.get())
        
        forum2 = self.perg_janela2.get()
        resposta2 = self.comentario_espaco.get()
        firebase.put("/Foruns/Trabalho/", name = "{0}".format(forum2), data = {'{0}'.format(self.x2): resposta2})
        self.x2 += 1        
        
    
    def responder3(self):
        self.primeira_resposta = tk.Label(self.comentarios)
        self.primeira_resposta.grid(row="{0}".format(self.numero_respostas3), column=1, columnspan=6, sticky="nsew")
        self.primeira_resposta.configure(text="")
        self.numero_respostas3 += 1
        self.primeira_resposta.configure(text=self.comentario_espaco.get())
        
        forum3 = self.perg_janela3.get()
        resposta3 = self.comentario_espaco.get()
        firebase.put("/Foruns/Amizade/", name = "{0}".format(forum3), data = {'{0}'.format(self.x3): resposta3})
        self.x3 += 1
        
    
    def responder4(self):
        self.primeira_resposta = tk.Label(self.comentarios)
        self.primeira_resposta.grid(row="{0}".format(self.numero_respostas4), column=1, columnspan=6, sticky="nsew")
        self.primeira_resposta.configure(text="")
        self.numero_respostas4 += 1
        self.primeira_resposta.configure(text=self.comentario_espaco.get())
        
        forum4 = self.perg_janela4.get()
        resposta4 = self.comentario_espaco.get()
        firebase.put("/Foruns/Viagens/{0}", name = "{0}".format(forum4), data = {'{0}'.format(self.x4): resposta4})
        self.x4 += 1
        
    
    def responder5(self):
        self.primeira_resposta = tk.Label(self.comentarios)
        self.primeira_resposta.grid(row="{0}".format(self.numero_respostas5), column=1, columnspan=6, sticky="nsew")
        self.primeira_resposta.configure(text="")
        self.numero_respostas5 += 1
        self.primeira_resposta.configure(text=self.comentario_espaco.get())
        
        forum5 = self.perg_janela5.get()
        resposta5 = self.comentario_espaco.get()
        firebase.put("/Foruns/Saude/", name = "{0}".format(forum5), data = {'{0}'.format(self.x5): resposta5})
        self.x5 += 1
        
    
    def responder6(self):
        self.primeira_resposta = tk.Label(self.comentarios)
        self.primeira_resposta.grid(row="{0}".format(self.numero_respostas6), column=1, columnspan=6, sticky="nsew")
        self.primeira_resposta.configure(text="")
        self.numero_respostas6 += 1
        self.primeira_resposta.configure(text=self.comentario_espaco.get())
        
        forum6 = self.perg_janela6.get()
        resposta6 = self.comentario_espaco.get()
        firebase.put("/Foruns/Familia/", name = "{0}".format(forum6), data = {'{0}'.format(self.x6): resposta6})
        self.x6 += 1
        
            
    def entrar_pergunta1(self):
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=50)
        self.comentarios.columnconfigure(1, minsize=50)
        self.comentarios.columnconfigure(2, minsize=50)
        self.comentarios.columnconfigure(3, minsize=50)
        self.comentarios.columnconfigure(4, minsize=50)
        self.comentarios.columnconfigure(5, minsize=50)
        self.comentarios.columnconfigure(6, minsize=50)
        self.comentarios.columnconfigure(7, minsize=50)
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
        
        self.background = tk.Label(self.comentarios, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
             
        self.voltar_perguntas = tk.Button(self.comentarios)
        self.voltar_perguntas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_perguntas.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_perguntas.configure(command=self.voltar_as_perguntas1)
        
        self.titulo_comentarios = tk.Label(self.comentarios)
        self.titulo_comentarios.grid(row=2, column=1, columnspan=6, sticky="nsew")
        forum1 = self.perg_janela1.get()
        self.titulo_comentarios.configure(text=forum1)
        
        # Responder
        
        self.conteudo_comentario1 = tk.StringVar(self.comentarios)        
        
        self.comentario_espaco = tk.Entry(self.comentarios)
        self.comentario_espaco.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_comentario2 = tk.StringVar(self.comentarios)
        
        self.conteudo_label = tk.StringVar(self.comentarios)
                
        self.botao_comentarios = tk.Button(self.comentarios)
        self.botao_comentarios.grid(row=4, column=6, sticky="nsew")
        self.botao_comentarios.configure(text="Responder", command=self.responder1, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')        
        
        self.comentarios.tkraise()
        
        
    def entrar_pergunta2(self):
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=50)
        self.comentarios.columnconfigure(1, minsize=50)
        self.comentarios.columnconfigure(2, minsize=50)
        self.comentarios.columnconfigure(3, minsize=50)
        self.comentarios.columnconfigure(4, minsize=50)
        self.comentarios.columnconfigure(5, minsize=50)
        self.comentarios.columnconfigure(6, minsize=50)
        self.comentarios.columnconfigure(7, minsize=50)
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
        
        self.background = tk.Label(self.comentarios, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
             
        self.voltar_perguntas = tk.Button(self.comentarios)
        self.voltar_perguntas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_perguntas.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_perguntas.configure(command=self.voltar_as_perguntas2)
        
        self.titulo_comentarios = tk.Label(self.comentarios)
        self.titulo_comentarios.grid(row=2, column=1, columnspan=6, sticky="nsew")
        forum2 = self.perg_janela2.get()
        self.titulo_comentarios.configure(text=forum2)
        
        # Responder
        
        self.conteudo_comentario1 = tk.StringVar(self.comentarios)        
        
        self.comentario_espaco = tk.Entry(self.comentarios)
        self.comentario_espaco.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_comentario2 = tk.StringVar(self.comentarios)
        
        self.conteudo_label = tk.StringVar(self.comentarios)
                
        self.botao_comentarios = tk.Button(self.comentarios)
        self.botao_comentarios.grid(row=4, column=6, sticky="nsew")
        self.botao_comentarios.configure(text="Responder", command=self.responder2, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')        
        
        self.comentarios.tkraise()
        
        
    def entrar_pergunta3(self):
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=50)
        self.comentarios.columnconfigure(1, minsize=50)
        self.comentarios.columnconfigure(2, minsize=50)
        self.comentarios.columnconfigure(3, minsize=50)
        self.comentarios.columnconfigure(4, minsize=50)
        self.comentarios.columnconfigure(5, minsize=50)
        self.comentarios.columnconfigure(6, minsize=50)
        self.comentarios.columnconfigure(7, minsize=50)
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
        
        self.background = tk.Label(self.comentarios, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
             
        self.voltar_perguntas = tk.Button(self.comentarios)
        self.voltar_perguntas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_perguntas.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_perguntas.configure(command=self.voltar_as_perguntas3)
        
        self.titulo_comentarios = tk.Label(self.comentarios)
        self.titulo_comentarios.grid(row=2, column=1, columnspan=6, sticky="nsew")
        forum3 = self.perg_janela3.get()
        self.titulo_comentarios.configure(text=forum3)
        
        # Responder
        
        self.conteudo_comentario1 = tk.StringVar(self.comentarios)        
        
        self.comentario_espaco = tk.Entry(self.comentarios)
        self.comentario_espaco.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_comentario2 = tk.StringVar(self.comentarios)
        
        self.conteudo_label = tk.StringVar(self.comentarios)
                
        self.botao_comentarios = tk.Button(self.comentarios)
        self.botao_comentarios.grid(row=4, column=6, sticky="nsew")
        self.botao_comentarios.configure(text="Responder", command=self.responder3, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')        
        
        self.comentarios.tkraise()
        
        
    def entrar_pergunta4(self):
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=50)
        self.comentarios.columnconfigure(1, minsize=50)
        self.comentarios.columnconfigure(2, minsize=50)
        self.comentarios.columnconfigure(3, minsize=50)
        self.comentarios.columnconfigure(4, minsize=50)
        self.comentarios.columnconfigure(5, minsize=50)
        self.comentarios.columnconfigure(6, minsize=50)
        self.comentarios.columnconfigure(7, minsize=50)
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
        
        self.background = tk.Label(self.comentarios, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
             
        self.voltar_perguntas = tk.Button(self.comentarios)
        self.voltar_perguntas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_perguntas.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_perguntas.configure(command=self.voltar_as_perguntas4)
        
        self.titulo_comentarios = tk.Label(self.comentarios)
        self.titulo_comentarios.grid(row=2, column=1, columnspan=6, sticky="nsew")
        forum4 = self.perg_janela4.get()
        self.titulo_comentarios.configure(text=forum4)
        
        # Responder
        
        self.conteudo_comentario1 = tk.StringVar(self.comentarios)        
        
        self.comentario_espaco = tk.Entry(self.comentarios)
        self.comentario_espaco.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_comentario2 = tk.StringVar(self.comentarios)
        
        self.conteudo_label = tk.StringVar(self.comentarios)
                
        self.botao_comentarios = tk.Button(self.comentarios)
        self.botao_comentarios.grid(row=4, column=6, sticky="nsew")
        self.botao_comentarios.configure(text="Responder", command=self.responder4, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')        
        
        self.comentarios.tkraise()
    
    
    def entrar_pergunta5(self):
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=50)
        self.comentarios.columnconfigure(1, minsize=50)
        self.comentarios.columnconfigure(2, minsize=50)
        self.comentarios.columnconfigure(3, minsize=50)
        self.comentarios.columnconfigure(4, minsize=50)
        self.comentarios.columnconfigure(5, minsize=50)
        self.comentarios.columnconfigure(6, minsize=50)
        self.comentarios.columnconfigure(7, minsize=50)
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
        
        self.background = tk.Label(self.comentarios, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
             
        self.voltar_perguntas = tk.Button(self.comentarios)
        self.voltar_perguntas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_perguntas.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_perguntas.configure(command=self.voltar_as_perguntas5)
        
        self.titulo_comentarios = tk.Label(self.comentarios)
        self.titulo_comentarios.grid(row=2, column=1, columnspan=6, sticky="nsew")
        forum5 = self.perg_janela5.get()
        self.titulo_comentarios.configure(text=forum5)
        
        # Responder
        
        self.conteudo_comentario1 = tk.StringVar(self.comentarios)        
        
        self.comentario_espaco = tk.Entry(self.comentarios)
        self.comentario_espaco.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_comentario2 = tk.StringVar(self.comentarios)
        
        self.conteudo_label = tk.StringVar(self.comentarios)
                
        self.botao_comentarios = tk.Button(self.comentarios)
        self.botao_comentarios.grid(row=4, column=6, sticky="nsew")
        self.botao_comentarios.configure(text="Responder", command=self.responder5, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')        
        
        self.comentarios.tkraise()
    
    
    def entrar_pergunta6(self):
        
        self.comentarios = tk.Frame(self.window)
        self.comentarios.columnconfigure(0, minsize=50)
        self.comentarios.columnconfigure(1, minsize=50)
        self.comentarios.columnconfigure(2, minsize=50)
        self.comentarios.columnconfigure(3, minsize=50)
        self.comentarios.columnconfigure(4, minsize=50)
        self.comentarios.columnconfigure(5, minsize=50)
        self.comentarios.columnconfigure(6, minsize=50)
        self.comentarios.columnconfigure(7, minsize=50)
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
        
        self.background = tk.Label(self.comentarios, image=self.window.background) #BACKGROUND
        self.background.grid(row = 0, column = 0) #BACKGROUND
        self.background.place(x=0, y=0, relwidth=1, relheight=1) #BACKGROUND
             
        self.voltar_perguntas = tk.Button(self.comentarios)
        self.voltar_perguntas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.voltar_perguntas.configure(text="Voltar", background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')
        self.voltar_perguntas.configure(command=self.voltar_as_perguntas6)
        
        self.titulo_comentarios = tk.Label(self.comentarios)
        self.titulo_comentarios.grid(row=2, column=1, columnspan=6, sticky="nsew")
        forum6 = self.perg_janela6.get()
        self.titulo_comentarios.configure(text=forum6)
        
        # Responder
        
        self.conteudo_comentario1 = tk.StringVar(self.comentarios)        
        
        self.comentario_espaco = tk.Entry(self.comentarios)
        self.comentario_espaco.grid(row=4, column=1, columnspan=5, sticky="nsew")
        
        self.conteudo_comentario2 = tk.StringVar(self.comentarios)
        
        self.conteudo_label = tk.StringVar(self.comentarios)
                
        self.botao_comentarios = tk.Button(self.comentarios)
        self.botao_comentarios.grid(row=4, column=6, sticky="nsew")
        self.botao_comentarios.configure(text="Responder", command=self.responder6, background = 'navy', borderwidth = 3, font=('AR ESSENCE', '18'), fg='gray92')        
        
        self.comentarios.tkraise()
    
    
    def voltar_pagina_inicial(self):
        self.login_screen.tkraise()
        
    def voltar_aos_foruns(self):
        self.foruns.tkraise()
    
    def voltar_as_perguntas1(self):
        self.janela1.tkraise()
    
    def voltar_as_perguntas2(self):
        self.janela2.tkraise()
        
    def voltar_as_perguntas3(self):
        self.janela3.tkraise()
    
    def voltar_as_perguntas4(self):
        self.janela4.tkraise()
        
    def voltar_as_perguntas5(self):
        self.janela5.tkraise()
    
    def voltar_as_perguntas6(self):
        self.janela6.tkraise()
    
  
app = InterfaceApp()
app.iniciar()