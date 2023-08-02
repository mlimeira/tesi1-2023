import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#janela = tk.Tk()
janela = ttk.Window(themename='superhero')
frm = ttk.LabelFrame(janela, text='Estilos')
frm.pack()
estilos = janela.style.colors
for e in estilos:
    btn = ttk.Button(frm, text=f'{e}', bootstyle=e)
    btn.pack(side=LEFT, padx=10)

janela.mainloop()