from moldes.cliente import Cliente
from utils.CEP import valida_cep
from utils.funcoes_auxiliares import *
from utils.valida_cpf import *
from utils.valida_data import *
from utils.valida_rg import *

clientes = []



print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
def main():
    validador = True
    while validador:
        print("1 - Cliente")
        print("2 - Cadastrar ação")
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
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
              cliente.cadastrar_cliente()
            # cliente = {
            #     "nome": input("Nome: "),
            #     "cpf": valida_cpf(),
            #     "rg": valida_rg(),
            #     "data_nascimento": valida_data_nascimento(),
            #     "endereco": valida_cep(),
            #     "numero_casa": input("Número casa: ")
            # }
            # clientes.append(cliente)
            # print(clientes)
            # validador = retornar_menu_principal()

        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


main()
