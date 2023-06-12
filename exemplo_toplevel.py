import tkinter as tk

def abrir_janela():
    toplevel = tk.Toplevel()
    toplevel.title('Nova Janela')

janela = tk.Tk()
btn = tk.Button(janela, text='Nova Janela',
                command=abrir_janela)
btn.pack()
janela.mainloop()