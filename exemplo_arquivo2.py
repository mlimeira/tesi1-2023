import tkinter as tk
from tkinter import filedialog as fd, messagebox
from tkinter.scrolledtext import ScrolledText

janela = tk.Tk()

def abrir(evento):
    tipos = (('Todos', '*.*'),('Python', '*.py'), ('Imagem', '*.jpg'))
    # nome = fd.askopenfilename(filetypes=tipos)
    # sct.delete(0.0, 'end')
    # with open(nome, 'r') as arquivo:
    #     for linha in arquivo:
    #         sct.insert(tk.END, linha)
    sct.delete(0.0, 'end')
    arquivo = fd.askopenfile(filetypes=tipos)
    for linha in arquivo:
        sct.insert('end', linha)
btn = tk.Button(janela, text='Abrir')
btn.pack()
btn.bind('<Button-1>', abrir)
sct = ScrolledText(janela, width=200, height=10)
sct.pack()

janela.mainloop()