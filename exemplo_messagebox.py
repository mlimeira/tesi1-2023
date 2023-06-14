import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

def aviso():
    messagebox.showinfo('Aviso', 'Você clicou no Botão')

def erro():
    messagebox.showerror('Erro', 'Torcer pelo Vasco')

def pergunta():
    resposta = messagebox.askquestion('Pergunta', 'Confirma a atualização?')
    if resposta == True:
        messagebox.showinfo('Ok', 'Ok')
    else:
        messagebox.showwarning('Voltar', 'Voltar')


btn_1 = tk.Button(janela, text='Aviso', command=aviso)
btn_1.pack()
btn_2 = tk.Button(janela, text='Erro', command=erro)
btn_2.pack()
btn_3 = tk.Button(janela, text='Pergunta', command=pergunta)
btn_3.pack()


janela.mainloop()