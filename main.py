from moldes.cliente import Cliente
from moldes.ordem import Ordem

print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")


def main():
    validador = True
    while validador:
        print("1 - Cliente")
        print("2 - Cadastrar ordem de compra")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
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
            acao = Ordem()
            acao.cadastrar_ordem()
        elif opcao == "3":
            acao = Ordem()
            acao.consultar_ordem()

        elif opcao == "4":
            pass
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


main()
