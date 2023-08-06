import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def carteira_analise(lista):
    try:
        star_date = "2020-01-01"
        end_date = "2023-01-01"
       # lista = ['ABCB4.SA', 'AGRO3.SA', 'BBAS3.SA']

        df = pd.DataFrame()

        for i in lista:
            cotacao = yf.download(i, start=star_date, end=end_date)
            df[i] = cotacao['Adj Close']

        df.plot(figsize=(15,10))

        plt.xlabel('Anos')
        plt.ylabel('Valor Ticket')
        plt.title('Cotação de Ações')
        plt.legend()

        plt.show()
    except Exception as e:
        print("...Erro ao obter dados")
        print(e)



