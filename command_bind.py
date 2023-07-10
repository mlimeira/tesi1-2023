import tkinter as tk

janela = tk.Tk()

def clicou():
    lbl = tk.Label(janela, text='Clicou')
    lbl.pack()

btn = tk.Button(janela, text='Clique',
                command=clicou)
btn.pack()
janela.mainloop()