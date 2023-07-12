import tkinter as tk

janela = tk.Tk()
def button_press(e):
    btn.config(text='Clicou')
def button_release(e):
    btn.config(text='Soltou')

btn = tk.Button(janela, text='Clique aqui')
btn.pack()
#btn.bind('<Button-1>', button_press)
btn.bind('<ButtonRelease-1>', button_release)

janela.mainloop()