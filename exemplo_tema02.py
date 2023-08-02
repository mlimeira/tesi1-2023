import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk as ttk

janela = ThemedTk(theme='breeze')

btn = ttk.Button(janela, text='Botão temático')
btn.pack()
lbl = ttk.Label(janela, text='Tema')
lbl.pack()
ent = ttk.Entry(janela)
ent.pack()

janela.mainloop()