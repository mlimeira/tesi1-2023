import tkinter as tk

janela = tk.Tk()
#Event bind
def clicou(evento):
    lbl = tk.Label(janela, text='Não pressionou Caps_Lock')
    lbl.pack()

def log(e):
    print(e)

def teste(t):
    print('teste')

btn = tk.Button(janela, text='Clique')
janela.bind('<Any-KeyPress>', clicou)
janela.bind('<Caps_Lock>', log, add='+')
#btn.bind('<a>', teste, add='+')
btn.pack()
janela.mainloop()