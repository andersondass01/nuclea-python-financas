from carteira import carteira_analise
from repository.banco_de_dados import BancoDeDados


class Ordem:

    def __init__(self):
        self.cliente = None
        self.atributos = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_ordem(self):
        self.cliente = input("Cliente ID: ")
        self.atributos = {
            'cliente_id': self.cliente,
            'nome': input("Nome Ação: "),
            'ticket': input("Ticket Ação: ")+".SA",
            'valor_compra': input("Valor da compra: "),
            'quantidade_compra': input("Quantidade da compra: "),
            'data_compra': input("Data da compra: ")
        }
        self.banco_de_dados.insert_ordem(self.atributos)

    def consultar_ordem(self):
        self.cpf = input("CPF: ")
        self.cliente = {
            'cpf': self.cpf
        }
        carteira_analise(self.banco_de_dados.select_tickets(self.cliente))

