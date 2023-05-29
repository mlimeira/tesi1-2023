import tkinter as tk

class Tela:

    def logar(self):
        lbl_mostrar = tk.Label(self.janela, text='Clicou')
        lbl_mostrar.pack()

    def __init__(self, master):
        self.janela = master
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')
        lbl_usuario = tk.Label(self.janela, text='Usuário:')
        lbl_usuario.pack()
        ent_usuario = tk.Entry(self.janela, width=30)
        ent_usuario.pack()
        lbl_senha = tk.Label(self.janela, text='Senha:')
        lbl_senha.pack()
        ent_senha = tk.Entry(self.janela, width=30, show='*')
        ent_senha.pack()
        btn_logar = tk.Button(self.janela, text='Entrar',
                              command=self.logar)
        btn_logar.pack()
        btn_fechar = tk.Button(self.janela, text='Fechar',
                               command=self.janela.destroy)
        btn_fechar.pack()

master = tk.Tk()
app = Tela(master)
master.mainloop()