import tkinter as tk
from tkinter import filedialog as fd, messagebox
from tkinter.scrolledtext import ScrolledText

janela = tk.Tk()

def abrir(evento):
    tipos = (('Todos', '*.*'),('Python', '*.py'),('Imagem', '*.jpg'))
    sct.delete(0.0, 'end')
    arquivo = fd.askopenfile(filetypes=tipos)
    for linha in arquivo:
        sct.insert('end', linha)

def salvar(evento):
    origem = sct.get(0.0, 'end')
    tipos = (('Texto', '*.txt'), ('Texto', '*.txt'))
    destino = fd.asksaveasfile(filetypes=tipos)
    for linha in origem:
        destino.write(linha)

btn = tk.Button(janela, text='Abrir')
btn.pack()
btn.bind('<Button-1>', abrir)
sct = ScrolledText(janela, width=200, height=10)
sct.pack()
btn2 = tk.Button(janela, text='Salvar')
btn2.pack()
btn2.bind('<Button-1>', salvar)

janela.mainloop()