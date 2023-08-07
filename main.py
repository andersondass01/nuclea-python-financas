from moldes.cliente import Cliente
from moldes.ordem import Ordem
from moldes.relatorio import Relatorio

print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")


def main():
    validador = True
    while validador:
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Gerar relatórios")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cliente = Cliente()
            print("Bem vindo ao menu de Cliente. Selecione uma das opções abaixo:")
            print("1 - Cadastrar cliente")
            print("2 - Consultar cliente")
            print("3 - Alterar cliente")
            print("4 - Excluir cliente")
            print("5 - Voltar ao menu principal")
            opcao_cliente = input("Digite a opção desejada: ")

            if opcao_cliente == "1":
                cliente.cadastrar_cliente()
            elif opcao_cliente == "2":
                cliente.consultar_cliente()
            elif opcao_cliente == "3":
                cliente.alterar_cliente()
            elif opcao_cliente == "4":
                cliente.delete_cliente()
            else:
                print("Retornando ao menu principal...")

        elif opcao == "2":
            print("Bem vindo ao menu de Ordem. Selecione uma das opções abaixo:")
            print("1 - Cadastrar ordem")
            print("2 - Voltar ao menu principal")
            opcao_ordem = input("Digite a opção desejada: ")
            if opcao_ordem == "1":
                acao = Ordem()
                acao.cadastrar_ordem()
            else:
                print("Retornando ao menu principal...")
        elif opcao == "3":
            print("Bem vindo ao menu de Análise de Carteira. Selecione uma das opções abaixo:")
            print("1 - Consultar carteira por CPF")
            print("2 - Voltar ao menu principal")
            opcao_analise = input("Digite a opção desejada: ")
            if opcao_analise == "1":
                acao = Ordem()
                acao.consultar_ordem()
            else:
                print("Retornando ao menu principal...")

        elif opcao == "4":
            acao = Relatorio()
            print("Bem vindo ao menu de Relatório. Selecione uma das opções abaixo:")
            print("1 - Pesquisar ação por ticket")
            print("2 - Consultar relatório da carteira por CPF")
            print("3 - Voltar ao menu principal")
            opcao_relatorio = input("Digite a opção desejada: ")
            if opcao_relatorio == "1":
                acao.pesquisar_acao()
            elif opcao_relatorio == "2":
                acao.relatorio_carteira()
            else:
                print("Retornando ao menu principal...")
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


main()
