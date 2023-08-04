import yfinance as yf


def obter_dados_acao(ticket, nome_arquivo):

    try:

        print("Colentando dados da ação: " + ticket)

        acao = yf.download(ticket+'.SA', progress=False)

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatório da ação: " + ticket + "\n")
            arquivo.write(str(acao.tail()))
            arquivo.close()

        print(acao)

    except Exception as e:
        print("Erro ao obter dados da ação: " + ticket)
        print(e)


ticket = input("Informe o ticket da ação: ")
nome_arquivo = input("Informe o nome do arquivo: ")
obter_dados_acao(ticket, nome_arquivo)