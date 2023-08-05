from relatório import obter_dados_acao
from repository.banco_de_dados import BancoDeDados


class Relatorio:

    def __init__(self):
        self.cliente = None
        self.acao = None
        self.banco_de_dados = BancoDeDados()

    def pesquisar_acao(self):
        self.acao = input("Informe o Ticket da ação: ")+".SA"
        nome_arquivo = "Relatório "+ self.acao + ".txt"
        obter_dados_acao(self.acao, nome_arquivo)

    def relatorio_carteira(self):
        self.cpf = input("CPF: ")
        self.cliente = {
            'cpf': self.cpf
        }
        tickets = self.banco_de_dados.select_tickets(self.cliente)
        for ticket in tickets:
            self.acao = str(ticket).replace("('", "").replace("',)", "")
            nome_arquivo = "Relatório "+ self.acao +" "+ self.cpf+ ".txt"
            obter_dados_acao(self.acao, nome_arquivo)