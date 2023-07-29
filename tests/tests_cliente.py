import unittest
from unittest.mock import patch

from faker import Faker

from main import main, clientes
from utils.valida_cpf import gera_cpf


class TestStringMethods(unittest.TestCase):
    pass

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ["1", nome, cpf, "12.345.678-x", "12/12/2012", "86082147", "100", "não"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}",
            "rg": "12.345.678-x",
            "data_nascimento": "12/12/2012",
            "endereco": {'CEP': '86082-147', 'Logradouro': 'Rua João Gil Ortega', 'Bairro': 'Parigot de Souza 2',
                         'Cidade': 'Londrina', 'Estado': 'PR'},
            "numero_casa": "100"
        }

        self.assertIn(cliente_esperado, clientes)
