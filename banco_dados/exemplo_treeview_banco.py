import tkinter as tk

import ttkbootstrap
from ttkbootstrap import ttk
from tkinter import messagebox
import conexao as bd
from ttkbootstrap.constants import *

class Tela():
    def __init__(self, master):
        self.janela = master
        colunas = ('id', 'nome', 'cpf', 'email')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, height=5, show='headings', bootstyle=DARK)
        self.tvw.grid()
        #Cabeçalho
        self.tvw.heading('id', text='ID')
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='E-mail')
        #Colunas
        self.tvw.column('id', minwidth=30, width=30)
        self.tvw.column('nome', minwidth=200, width=200)
        self.tvw.column('cpf', minwidth=100, width=100)
        self.tvw.column('email', minwidth=300, width=300)
        #Linhas
        self.atualizar_treeview()
        #Barra de rolagem
        scb = ttk.Scrollbar(self.janela, orient=tk.VERTICAL,command=self.tvw.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.tvw.config(yscrollcommand=scb.set)
        #Botões
        frm_botoes = tk.Frame(self.janela)
        frm_botoes.grid(row=1, column=0)
        btn_cadastrar = ttk.Button(frm_botoes, text='Cadastrar',
                                   command=self.cadastrar)
        btn_cadastrar.grid(row=0, column=0, padx=5, pady=5)
        btn_excluir = ttk.Button(frm_botoes,
                                  text='Excluir',
                                  command=self.excluir)
        btn_excluir.grid(row=0, column=1, padx=5, pady=5)
        btn_editar = ttk.Button(frm_botoes, text='Editar',
                               command=self.editar)
        btn_editar.grid(row=0, column=2, padx=5, pady=5)

    def atualizar_treeview(self):
        items = self.tvw.get_children() #limpando o componente treeview antes de preencher com o conteúdo do banco de dados
        for i in items:
            self.tvw.delete(i)
        dados = bd.listar('SELECT id, nome, cpf, email  FROM cliente;')
        for linha in dados:
            self.tvw.insert('', tk.END, values=linha)

    def editar(self):
        item = self.tvw.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            valores = self.tvw.item(item, 'values')
            self.top_editar = tk.Toplevel()
            self.top_editar.grab_set()
            lbl_nome = tk.Label(self.top_editar, text='Nome:')
            lbl_nome.grid(row=0, column=0, pady=2, stick='w')
            lbl_cpf = tk.Label(self.top_editar, text='CPF:')
            lbl_cpf.grid(row=1, column=0, pady=2, stick='w')
            lbl_email = tk.Label(self.top_editar, text='E-mail:')
            lbl_email.grid(row=2, column=0, pady=2, stick='w')
            self.ent_nome = tk.Entry(self.top_editar)
            self.ent_nome.grid(row=0, column=1, pady=2)
            self.ent_nome.insert('end', valores[1])
            self.ent_cpf = tk.Entry(self.top_editar)
            self.ent_cpf.grid(row=1, column=1, pady=2)
            self.ent_cpf.insert('end', valores[2])
            self.ent_email = tk.Entry(self.top_editar)
            self.ent_email.grid(row=2, column=1, pady=2)
            self.ent_email.insert('end', valores[3])
            self.id = valores[0]
            btn_confirmar = tk.Button(self.top_editar,
                                      text='Confirmar',
                                      command=self.confirmar_edicao)
            btn_confirmar.grid(row=3, column=1, padx=5, pady=5)

    def confirmar_edicao(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        selecionado = self.tvw.selection()
        if nome == '' or cpf == '' or email == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.top_cadastrar)
        else:
            #self.tvw.item(selecionado, values=(nome, cpf, email))
            sql = f'''UPDATE cliente SET nome="{nome}", 
            cpf="{cpf}", email="{email}" WHERE id={self.id};'''
            bd.atualizar(sql)
            self.atualizar_treeview()
            self.top_editar.destroy()

    def excluir(self):
        tupla = self.tvw.selection()
        # if len(tupla) == 1:
        #     self.tvw.delete(tupla)
        # elif len(tupla) > 1:
        #     for item in tupla:
        #         self.tvw.delete(item)
        if len(tupla) != 1:
            messagebox.showwarning('Aviso', 'Selecione somente um item')
        else:
            id = self.tvw.item(tupla, 'values')[0]
            nome = self.tvw.item(tupla, 'values')[1]
            f'SELECT nome FROM cliente WHERE id={id};'
            confirma = messagebox.askyesno('Aviso', f'Confirma a exclusão do cliente: {nome}?')
            if confirma:
                bd.remover(f'DELETE FROM cliente WHERE id={id}')
                for item in tupla:
                    self.tvw.delete(item)

    def cadastrar(self):
        self.top_cadastrar = ttkbootstrap.Toplevel()
        self.top_cadastrar.grab_set()
        lbl_nome = tk.Label(self.top_cadastrar, text='Nome:')
        lbl_nome.grid(row=0, column=0, pady=2, stick='w')
        lbl_cpf = tk.Label(self.top_cadastrar, text='CPF:')
        lbl_cpf.grid(row=1, column=0, pady=2, stick='w')
        lbl_email = tk.Label(self.top_cadastrar, text='E-mail:')
        lbl_email.grid(row=2, column=0, pady=2, stick='w')
        self.ent_nome = tk.Entry(self.top_cadastrar)
        self.ent_nome.grid(row=0, column=1, pady=2)
        self.ent_cpf = tk.Entry(self.top_cadastrar)
        self.ent_cpf.grid(row=1, column=1, pady=2)
        self.ent_email = tk.Entry(self.top_cadastrar)
        self.ent_email.grid(row=2, column=1, pady=2)
        btn_confirmar = tk.Button(self.top_cadastrar,
                                  text='Confirmar',
                                  command=self.confirmar_cadastro)
        btn_confirmar.grid(row=3, column=1, padx=5, pady=5)


    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        if nome == '' or cpf == '' or email == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.top_cadastrar)
        else:
            #self.tvw.insert('','end', values=(id, nome, cpf, email))
            sql_inserir = f"INSERT INTO cliente VALUES(NULL, '{nome}','{cpf}','{email}');"
            bd.inserir(sql_inserir)
            messagebox.showinfo('Aviso', 'Registro inserido com sucesso!')
            self.atualizar_treeview()
            self.top_cadastrar.destroy()

app = ttkbootstrap.Window(themename='litera')
Tela(app)
app.mainloop()