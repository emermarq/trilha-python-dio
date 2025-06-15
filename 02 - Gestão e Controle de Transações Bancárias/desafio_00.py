import tkinter as tk
from tkinter import messagebox

# Funções de exemplo para os comandos dos menus
def novo_arquivo():
    print("Novo arquivo criado")

def abrir_arquivo():
    print("Arquivo aberto")

def sair():
    janela.quit()

def copiar():
    print("Copiar")

def colar():
    print("Colar")

def sobre():
    messagebox.showinfo("Sobre", "Exemplo de menu com Tkinter")

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Menu com Tkinter")
janela.geometry("400x300")

# Criar a barra de menu
barra_menu = tk.Menu(janela)

# Menu "Arquivo"
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Menu "Editar"
menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Copiar", command=copiar)
menu_editar.add_command(label="Colar", command=colar)
barra_menu.add_cascade(label="Editar", menu=menu_editar)

# Menu "Ajuda"
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

# Associar a barra de menu à janela
janela.config(menu=barra_menu)

# Rodar o loop principal
janela.mainloop()