import requests

def busca_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    print(response.json())

if __name__ == "__main__":
    busca_cep(86082147)
