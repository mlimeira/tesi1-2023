import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
caminho_imagem = Image.open('capivara-ufac.jpg')
imagem = caminho_imagem.resize((200,150))
imagem = ImageTk.PhotoImage(imagem)
lbl = tk.Label(janela, image=imagem)
lbl.pack()

janela.mainloop()