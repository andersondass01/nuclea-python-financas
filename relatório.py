import yfinance as yf


def obter_dados_acao(ticket, nome_arquivo):

    try:
        acao = yf.download(ticket, progress=False)

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatório da ação: " + ticket + "\n")
            arquivo.write(str(acao.tail()))
            arquivo.close()

        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        print("Erro ao obter dados da ação: " + ticket)
        print(e)


# ticket = input("Informe o ticket da ação: ")
# nome_arquivo = input("Informe o nome do arquivo: ")
# obter_dados_acao(ticket, nome_arquivo)