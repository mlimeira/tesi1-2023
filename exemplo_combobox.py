import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

lista = ['Domingo','Segunda', 'Terça', 'Quarta']
cbx = ttk.Combobox(janela, values=lista, state='readonly')
#cbx.set('Segunda')
cbx.current(2)
cbx.pack()

janela.mainloop()