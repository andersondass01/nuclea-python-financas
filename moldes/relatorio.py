from relatório import obter_dados_acao
from repository.banco_de_dados import BancoDeDados
from utils.valida_cpf import valida_cpf
from utils.valida_ticker import valida_ticker


class Relatorio:

    def __init__(self):
        self.cliente = None
        self.acao = None
        self.banco_de_dados = BancoDeDados()

    def pesquisar_acao(self):
        self.acao = valida_ticker() + ".SA"
        nome_arquivo = "Relatório " + self.acao + ".txt"
        obter_dados_acao(self.acao, nome_arquivo)

    def relatorio_carteira(self):
        self.cpf = valida_cpf()
        self.cliente = {
            'cpf': self.cpf
        }
        tickets = self.banco_de_dados.select_tickets(self.cliente)
        if len(tickets) == 0:
            print("Cliente não possui ações.")
            return

        for ticket in tickets:
            self.acao = str(ticket).replace("('", "").replace("',)", "")
            nome_arquivo = "Relatório " + self.acao + ' CPF ' + self.cpf + '.txt'
            obter_dados_acao(self.acao, nome_arquivo)
