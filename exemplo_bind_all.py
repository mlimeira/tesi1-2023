import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()

def entrar(e):
    messagebox.showinfo('Info', 'Ok')

ent_nome = tk.Entry(janela)
ent_nome.pack()
ent_senha = tk.Entry(janela)
ent_senha.pack()
btn = tk.Button(janela, text='Entrar')
btn.pack()
btn.bind('<1>', entrar)
janela.bind_all('<Return>', entrar)

janela.mainloop()


