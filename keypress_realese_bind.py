import tkinter as tk

janela = tk.Tk()
#Event bind
def keypress(e):
    lbl.config(text=f'Keypress Símbolo:{e.keysym} char: {e.char}')
def keyrelease(e):
    lbl.config(text='KeyRelease')

lbl = tk.Label(janela, text='Pressione qualquer tecla')
lbl.pack()
janela.bind('<KeyPress>', keypress)
janela.bind('<KeyRelease>', keyrelease, add='+')

janela.mainloop()