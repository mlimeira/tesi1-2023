import tkinter as tk
from tkinter import ttk as ttk

janela = tk.Tk()
tema = tk.StringVar()
def alterar_tema(event):
    print(tema.get())
    ts.theme_use(tema.get())

btn = ttk.Button(janela, text='Botão temático')
btn.pack()
lbl = ttk.Label(janela, text='Tema')
lbl.pack()
ts = ttk.Style()
temas = ts.theme_names()
cbx = ttk.Combobox(janela, textvariable=tema, values=temas)
cbx.pack()
cbx.bind('<<ComboboxSelected>>', alterar_tema)

janela.mainloop()