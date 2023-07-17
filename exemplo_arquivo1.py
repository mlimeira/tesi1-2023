import tkinter as tk
from tkinter import filedialog as fd, messagebox

janela = tk.Tk()

def abrir(evento):
    tipos = (('Todos', '*.*'),('Python', '*.py'), ('Imagem', '*.jpg'))
    nome = fd.askopenfilename(filetypes=tipos)
    messagebox.showinfo('Info', nome)

btn = tk.Button(janela, text='Abrir')
btn.pack()
btn.bind('<Button-1>', abrir)

janela.mainloop()