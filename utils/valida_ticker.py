import re

def valida_ticker():
    padrao_ticker = r'^[A-Z]{4}\d{1}$'

    while True:
        ticker = input("TICKER: ").upper()
        resultado_validacao = re.match(padrao_ticker, ticker)

        if (resultado_validacao):
            return ticker
        else:
            print("TICKER inválido. Tente novamente: ")
