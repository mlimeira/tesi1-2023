import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

janela = ThemedTk(theme="arc")
temas = janela.pixmap_themes
def altera_tema(t):
   janela.set_theme(t)

mnu_barra = tk.Menu(janela)
mnu_temas = tk.Menu(mnu_barra, tearoff=0)
mnu_barra.add_cascade(label='Temas', menu=mnu_temas)
janela.config(menu=mnu_barra)
for t in temas:
    mnu_temas.add_command(label=t, command=lambda t=t: altera_tema(t))

lbl_user = ttk.Label(janela, text='Usuario:').grid(row=0, column=0)
lbl_pass = ttk.Label(janela, text='Senha:').grid(row=1, column=0)
ent_user = ttk.Entry(janela).grid(row=0, column=1)
ent_pass = ttk.Entry(janela).grid(row=1, column=1)
btn = ttk.Button(janela, text='Entrar').grid(row=2, column=0, columnspan=2)

janela.mainloop()