import requests

def busca_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            dados_endereco = data

            endereco = {
                "CEP": data['cep'],
                "Logradouro": data['logradouro'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf']
            }
            return endereco

def valida_cep():
    print("Consulta do CEP - ViaCEP")

    while True:
        cep_input = input("CEP: ")

        if cep_input.isdigit() and len(cep_input) == 8:
            return busca_cep(cep_input)



