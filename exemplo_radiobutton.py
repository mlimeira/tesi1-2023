import tkinter as tk

class Tela:
    def mostrar(self):
        lbl_mostrar = tk.Label(self.janela, text=self.v.get())
        lbl_mostrar.pack()

    def __init__(self, master): #customizar a janela
        self.janela = master
        self.janela.title('Exemplo RadioButton')
        self.janela.geometry('400x400')
        self.v = tk.StringVar()
        self.v.set('bd1')
        lbl_escolha = tk.Label(self.janela, text='Escolha uma Disciplina:')
        lbl_escolha.pack()
        rbt_lp1 = tk.Radiobutton(self.janela, text='LP1',
                                 value='lp1',
                                 variable=self.v,
                                 selectcolor='grey',
                                 command=self.mostrar)
        rbt_lp1.pack()
        rbt_tesi1 = tk.Radiobutton(self.janela, text='TESI 1',
                                   value='tesi1',
                                   variable=self.v,
                                   selectcolor='grey',
                                   command=self.mostrar)
        rbt_tesi1.pack()
        rbt_bd1 = tk.Radiobutton(self.janela, text='BD 1',
                                 value='bd1',
                                 variable=self.v,
                                 selectcolor='grey',
                                 command=self.mostrar)
        rbt_bd1.pack()

app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()