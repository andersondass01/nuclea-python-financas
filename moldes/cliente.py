from repository.banco_de_dados import BancoDeDados
from utils.funcoes_auxiliares import formata_texto
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg
from utils.CEP import valida_cep
from utils.valida_data import valida_data_nascimento


class Cliente:

    def __init__(self):
        self.cliente = None
        self.banco_de_dados = BancoDeDados()
        self.cpf = None

    def cadastrar_cliente(self):
        self.cliente = {
            'nome': formata_texto(input("Nome: ")),
            'cpf': valida_cpf(),
            'rg': valida_rg(),
            'data_nascimento': valida_data_nascimento(),
            'cep': valida_cep(),
            'numero_residencia': input("Número casa: ")
        }
        self.banco_de_dados.insert(self.cliente)

    def consultar_cliente(self):
        self.cpf = valida_cpf()
        self.cliente = {
            'cpf': self.cpf
        }
        self.banco_de_dados.select(self.cliente)

    def alterar_cliente(self):
        self.cpf = valida_cpf()
        self.cliente = {
            'cpf': self.cpf,
            'nome': formata_texto(input("Nome: ")),
            'rg': valida_rg(),
            'data_nascimento': valida_data_nascimento(),
            'cep': valida_cep(),
            'numero_residencia': input("Número casa: ")
        }
        self.banco_de_dados.update(self.cliente)

    def delete_cliente(self):
        self.cpf = valida_cpf()
        self.cliente = {
            'cpf': self.cpf
        }
        print(self.cliente)
        self.banco_de_dados.delete(self.cliente)

