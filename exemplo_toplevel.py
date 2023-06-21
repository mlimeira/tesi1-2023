import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.janela.title('Primeira Janela')
        btn = tk.Button(self.janela, text='Nova Janela',
                        command=self.nova_janela)
        btn.pack()

    def nova_janela(self):
        self.toplevel = tk.Toplevel(self.janela)
        self.toplevel.geometry('300x100')
        self.toplevel.title('Top Level Janela')
        #self.janela.withdraw() #Oculta a janela principal
        self.toplevel.grab_set() #Fixar toplevel
        btn = tk.Button(self.toplevel, text='Voltar',
                        command=self.voltar)
        btn2 = tk.Button(self.toplevel, text='Nova Janela',
                        command=self.nova_janela2)
        btn.pack()
        btn2.pack()

    def nova_janela2(self):
        self.toplevel2 = tk.Toplevel(self.toplevel)
        self.toplevel2.geometry('300x100')
        self.toplevel2.title('Top Level Janela')
        #self.janela.withdraw() #Oculta a janela principal
        self.toplevel2.grab_set() #Fixar toplevel
        btn = tk.Button(self.toplevel2, text='Voltar',
                        command=self.voltar2)
        btn.pack()

    def voltar(self):
        self.toplevel.destroy()
        self.janela.deiconify()

    def voltar2(self):
        self.toplevel2.destroy()



app = tk.Tk()
master = Tela(app)
app.mainloop()