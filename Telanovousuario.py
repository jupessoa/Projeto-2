# -*- coding: utf-8 -*-
"""
Created on Wed May 11 07:44:04 2016

@author: Vitória
"""

import tkinter as tk
#from firebase import firebase

#firebase = firebase.FirebaseApplication("https://sosfinal.firebase.com")

class InterfaceApp:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("400x600+150+50")
        self.window.title("App")
        self.window.rowconfigure(0, minsize=600)
        self.window.columnconfigure(0, minsize=400)

        # Tela de login.
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
        
        self.logo = tk.Label(self.login_screen)
        self.logo.grid(row=1, column=1, columnspan=3, sticky="nsew")
        self.logo.configure(text="LOGO")
        
        self.login = tk.Label(self.login_screen)
        self.login.grid(row=2, column=2, sticky="nsew")
        self.login.configure(text="Login")
        
        self.inserir_login = tk.Entry(self.login_screen)
        self.inserir_login.grid(row=3, column=1, columnspan=3, sticky="nsew")

        self.senha = tk.Label(self.login_screen)
        self.senha.grid(row=5, column=2, sticky="nsew")
        self.senha.configure(text="Senha")
        
        self.inserir_senha = tk.Entry(self.login_screen)
        self.inserir_senha.grid(row=6, column=1, columnspan=3, sticky="nsew")
        
        self.entrar = tk.Button(self.login_screen)
        self.entrar.grid(row=8, column=2, sticky="nsew")
        self.entrar.configure(text="Entrar")
        self.entrar.configure(command=self.entrar_app)
        
        self.criar_novo_usuario = tk.Button(self.login_screen)
        self.criar_novo_usuario.grid(row=9, column=4, sticky="nsew")
        self.criar_novo_usuario.configure(text="Criar novo usuário")
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
        
        self.logo = tk.Label(self.tela_novo_usuario)
        self.logo.grid(row=1, column=1, columnspan=3, sticky="nsew")
        self.logo.configure(text="SOS NOW")
        
        self.nome_usuario = tk.Label(self.tela_novo_usuario)
        self.nome_usuario.grid(row=2, column=2, sticky="nsew")
        self.nome_usuario.configure(text="Insira um nome para o seu usuário:")
        
        self.inserir_nome_usuario = tk.Entry(self.tela_novo_usuario)
        self.inserir_nome_usuario.grid(row=3, column=1, columnspan=3, sticky="nsew")

        self.criar_senha = tk.Label(self.tela_novo_usuario)
        self.criar_senha.grid(row=5, column=2, sticky="nsew")
        self.criar_senha.configure(text="Insira uma senha:")
        
        self.inserir_criar_senha = tk.Entry(self.tela_novo_usuario)
        self.inserir_criar_senha.grid(row=6, column=1, columnspan=3, sticky="nsew")
        
        self.salvar_novo_usuario = tk.Button(self.tela_novo_usuario)
        self.salvar_novo_usuario.grid(row=8, column=2, sticky="nsew")
        self.salvar_novo_usuario.configure(text="Criar")
        self.salvar_novo_usuario.configure(command=self.tela_login)
        
        # Tela de forums.        
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
        self.foruns.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
        self.tema1 = tk.Button(self.foruns)
        self.tema1.grid(row=1, column=1, sticky="nsew")
        self.tema1.configure(text="Relacionamento")
        self.tema1.configure(command=self.tema1_clicado)
        
        self.tema2 = tk.Button(self.foruns)
        self.tema2.grid(row=3, column=1, sticky="nsew")
        self.tema2.configure(text="Vida profissional")
        self.tema2.configure(command=self.tema2_clicado)
        
        self.tema3 = tk.Button(self.foruns)
        self.tema3.grid(row=5, column=1, sticky="nsew")
        self.tema3.configure(text="Amizade")
        self.tema3.configure(command=self.tema3_clicado)
        
        self.tema4 = tk.Button(self.foruns)
        self.tema4.grid(row=7, column=1, sticky="nsew")
        self.tema4.configure(text="Viagens")
        self.tema4.configure(command=self.tema4_clicado)

        # Tela primeiro forum.        
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
        
        self.titulo_tema1 = tk.Label(self.janela1)
        self.titulo_tema1.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema1.configure(text="Relacionamento")
        
        self.perg_janela1 = tk.Entry(self.janela1)
        self.perg_janela1.grid(row=2, column=1, columnspan=5, sticky="nsew")
        
        
        self.botao_janela1 = tk.Button(self.janela1)
        self.botao_janela1.grid(row=2, column=6, sticky="nsew")
        self.botao_janela1.configure(text="Perguntar")
        
        
        # Tela segundo forum.        
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
        
        
        self.titulo_tema2 = tk.Label(self.janela2)
        self.titulo_tema2.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema2.configure(text="Vida profissional")
        
        # Tela terceiro forum.        
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
        
        self.titulo_tema3 = tk.Label(self.janela3)
        self.titulo_tema3.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema3.configure(text="Amizade")
        
        # Tela quarto forum.        
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
        
        self.titulo_tema4 = tk.Label(self.janela4)
        self.titulo_tema4.grid(row=0, column=3, columnspan=2, sticky="nsew")
        self.titulo_tema4.configure(text="Viagens")
        
        self.login_screen.tkraise()
        
    def iniciar(self):
        self.window.mainloop()
         
    def novo_usuario(self):
        self.tela_novo_usuario.tkraise()
    
    def tela_login(self):
        self.login_screen.tkraise()
        
    def entrar_app(self):
        self.foruns.tkraise()
        
    def tema1_clicado(self):
        self.janela1.tkraise()
        
    def tema2_clicado(self):
        self.janela2.tkraise()
        
    def tema3_clicado(self):
        self.janela3.tkraise()
        
    def tema4_clicado(self):
        self.janela4.tkraise()
        


app = InterfaceApp()
app.iniciar()