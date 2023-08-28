import tkinter as tk

import ttkbootstrap
from ttkbootstrap import ttk
from tkinter import messagebox
import conexao as bd
from ttkbootstrap.constants import *

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title('Lista de Contas')
        self.janela.place_window_center()   #Função para centralizar tela do ttkbootstrap
        colunas = ('id', 'numero', 'saldo', 'nome')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, height=5, show='headings', bootstyle=DARK)
        self.tvw.grid()
        #Cabeçalho
        self.tvw.heading('id', text='ID')
        self.tvw.heading('numero', text='Número')
        self.tvw.heading('saldo', text='Saldo')
        self.tvw.heading('nome', text='Titular')
        #Colunas
        self.tvw.column('id', minwidth=30, width=30)
        self.tvw.column('numero', minwidth=100, width=100)
        self.tvw.column('saldo', minwidth=100, width=100)
        self.tvw.column('nome', minwidth=200, width=200)
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

    #Função para atualizar o treeview das contas
    def atualizar_treeview(self):
        items = self.tvw.get_children() #limpa o componente treeview antes de preencher com o conteúdo do BD
        for i in items:
            self.tvw.delete(i)
        sql_listar_contas = 'SELECT c.id, c.numero, c.saldo, cli.nome FROM conta c, cliente cli WHERE c.id_cliente=cli.id;'
        dados = bd.listar(sql_listar_contas)
        for linha in dados:
            self.tvw.insert('', tk.END, values=linha)
    #Função para excluir uma conta
    def excluir(self):
        tupla = self.tvw.selection() #Tupla que armazena o item selecionado no treeview
        if len(tupla) != 1:
            messagebox.showwarning('Aviso', 'Selecione somente um item')
        else:
            id = self.tvw.item(tupla, 'values')[0]
            nome = self.tvw.item(tupla, 'values')[1]
            f'SELECT nome FROM conta WHERE id={id};'
            confirma = messagebox.askyesno('Aviso', f'Confirma a exclusão conta: {nome}?')
            if confirma:
                bd.remover(f'DELETE FROM conta WHERE id={id}')
                for item in tupla:
                    self.tvw.delete(item)

    #Função com uma janela TopLevel para cadastrar as informações de uma conta
    def cadastrar(self):
        self.top_cadastrar = ttkbootstrap.Toplevel()
        self.top_cadastrar.title('Cadastro de Contas')
        self.top_cadastrar.position_center() #Função para centralizar toplevel do ttkbootstrap
        self.top_cadastrar.grab_set()
        lbl_numero = tk.Label(self.top_cadastrar, text='Número:')
        lbl_numero.grid(row=0, column=0, pady=2, stick='w')
        lbl_nome = tk.Label(self.top_cadastrar, text='Nome:')
        lbl_nome.grid(row=1, column=0, pady=2, stick='w')
        self.ent_num_conta = tk.Entry(self.top_cadastrar, width=28)
        self.ent_num_conta.grid(row=0, column=1, pady=2, columnspan=2)
        self.ent_nome_cliente = tk.Entry(self.top_cadastrar, state='readonly', width=28)
        self.ent_nome_cliente.grid(row=1, column=1, pady=2, columnspan=2)
        self.btn_pesquisar = tk.Button(self.top_cadastrar, text='Pesquisar Cliente', command=self.pesquisar)
        self.btn_pesquisar.grid(row=2, column=1)
        self.btn_confirmar = tk.Button(self.top_cadastrar,
                                  text='Confirmar',
                                  command=self.confirmar_cadastro, state='disabled')
        self.btn_confirmar.grid(row=2, column=0, padx=5, pady=5)
        btn_cancelar = tk.Button(self.top_cadastrar, text='Cancelar', command=self.cancelar_cadastro)
        btn_cancelar.grid(row=2, column=2, padx=5, pady=5)

    def cancelar_cadastro(self):
        self.top_cadastrar.destroy()

    #Função com janela para pesquisar clientes (semelhante a de listagem) com um botão de pesquisar e ourto para selecionar
    def pesquisar(self):
        self.top_pesquisar_cliente = ttkbootstrap.Toplevel()
        self.top_pesquisar_cliente.grab_set()
        self.top_pesquisar_cliente.title('Pesquisar Clientes')
        self.top_pesquisar_cliente.position_center()
        colunas = ('id', 'nome', 'cpf', 'email')
        self.tvw_pesquisar = ttk.Treeview(self.top_pesquisar_cliente, columns=colunas, height=5, show='headings', bootstyle=DARK)
        self.tvw_pesquisar.grid()
        # Cabeçalho
        self.tvw_pesquisar.heading('id', text='ID')
        self.tvw_pesquisar.heading('nome', text='Nome')
        self.tvw_pesquisar.heading('cpf', text='CPF')
        self.tvw_pesquisar.heading('email', text='E-mail')
        # Colunas
        self.tvw_pesquisar.column('id', minwidth=30, width=30)
        self.tvw_pesquisar.column('nome', minwidth=200, width=200)
        self.tvw_pesquisar.column('cpf', minwidth=100, width=100)
        self.tvw_pesquisar.column('email', minwidth=300, width=300)
        # Linhas
        #self.atualizar_treeview()
        # Barra de rolagem
        scb = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.tvw.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.tvw.config(yscrollcommand=scb.set)
        # Botões
        frm_botoes = tk.Frame(self.top_pesquisar_cliente)
        frm_botoes.grid(row=1, column=0)
        lbl_nome = ttk.Label(frm_botoes, text='Nome:')
        lbl_nome.grid(row=0, column=0)
        self.ent_nome = ttk.Entry(frm_botoes)
        self.ent_nome.grid(row=0, column=1)
        btn_pesquisar = ttk.Button(frm_botoes, text='Pesquisar',
                                   command=self.pesquisar_cliente)
        btn_pesquisar.grid(row=0, column=2, padx=5, pady=5)
        btn_selecionar = ttk.Button(frm_botoes,
                                 text='Selecionar',
                                 command=self.selecionar)
        btn_selecionar.grid(row=0, column=3, padx=5, pady=5)
        btn_cancelar = ttk.Button(frm_botoes,
                                    text='Cancelar',
                                    command=self.cancelar_pesquisa)
        btn_cancelar.grid(row=0, column=4, padx=5, pady=5)

    def cancelar_pesquisa(self):
        self.top_pesquisar_cliente.destroy()

    # Função para selecionar um cliente, guardar nome + id nos campos de entrada e destruir a TopLevel
    def selecionar(self):
        cliente = self.tvw_pesquisar.selection()
        if len(cliente) != 1:
            messagebox.showwarning('Aviso', 'Selecione um item', parent=self.top_pesquisar_cliente)
        else:
            nome_cliente = self.tvw_pesquisar.item(cliente, 'values')[1]
            self.id_cliente = self.tvw_pesquisar.item(cliente, 'values')[0]
            self.ent_nome_cliente.config(state='normal')
            self.ent_nome_cliente.insert('end', nome_cliente)
            self.ent_nome_cliente.config(state='readonly')
            self.btn_confirmar.config(state='normal')
            self.top_pesquisar_cliente.destroy()

    # Função para limpar o treeview, usar o nome digitado para buscar no BD o cliente com o operador like "%{nome}%" e preencher o treeview
    def pesquisar_cliente(self):
        dados = self.tvw_pesquisar.get_children()
        for i in dados:
            self.tvw_pesquisar.delete(i)
        nome = self.ent_nome.get()
        sql_pesquisar = f'SELECT * FROM cliente WHERE nome like "%{nome}%";'
        clientes = bd.listar(sql_pesquisar)
        for c in clientes:
            self.tvw_pesquisar.insert('', 'end', values=c)

    # Função para inserir os dados da conta no BD, atualizar o treeview e destruir a TopLevel
    def confirmar_cadastro(self):
        numero = self.ent_num_conta.get()
        nome = self.ent_nome_cliente.get()
        if numero == '' or nome == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.top_cadastrar)
        else:
            sql = f'INSERT INTO conta VALUES(NULL, {numero}, 0, {self.id_cliente});'
            bd.inserir(sql)
            messagebox.showinfo('Aviso', 'Conta cadastrada com sucesso!')
            self.atualizar_treeview()
            self.top_cadastrar.destroy()

app = ttkbootstrap.Window(themename='litera')
Tela(app)
app.mainloop()