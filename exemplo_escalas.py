import tkinter as tk

class Tela:
    def mostrar(self, valor):
        lbl = tk.Label(self.janela, text=self.v.get())
        lbl.pack()

    def __init__(self, master): #customizar a janela
        self.janela = master
        self.janela.title('Exemplo Escalas')
        self.janela.geometry('400x400')
        self.v = tk.StringVar()
        self.v.set(100)
        spb_mes = tk.Spinbox(self.janela, from_=1, to=12,
                             wrap=True)
        spb_mes.pack()
        scl_volume = tk.Scale(self.janela, from_=0, to=100,
                              orient=tk.VERTICAL,
                              variable=self.v,
                              command=self.mostrar)
        scl_volume.pack()


app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()