import tkinter as tk

janela = tk.Tk()
imagem = tk.PhotoImage(file='logo-ufac.png')
imagem2 = imagem.subsample(4, 4) #Redimensiona a imagem
lbl = tk.Label(janela, image=imagem2)
lbl.pack()

janela.mainloop()