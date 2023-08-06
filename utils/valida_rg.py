import re

def valida_rg():
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]{1}$'

    while True:
        rg = input("RG: ")
        resultado_validacao = re.match(padrao_rg, rg)

        if (resultado_validacao):
            return rg
        else:
            print("RG inválido. Tente novamente: ")
