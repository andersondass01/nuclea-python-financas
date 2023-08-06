from carteira import carteira_analise
from repository.banco_de_dados import BancoDeDados
from utils.valida_cpf import valida_cpf
from utils.valida_data import valida_data_compra
from utils.valida_ticker import valida_ticker


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
            'ticket': valida_ticker()+".SA",
            'valor_compra': input("Valor da compra: "),
            'quantidade_compra': input("Quantidade da compra: "),
            'data_compra': valida_data_compra()
        }
        self.banco_de_dados.insert_ordem(self.atributos)

    def consultar_ordem(self):
        self.cpf = valida_cpf()
        self.cliente = {
            'cpf': self.cpf
        }
        carteira_analise(self.banco_de_dados.select_tickets(self.cliente))

