import unittest
from unittest.mock import patch

from faker import Faker

from main import main
from repository.banco_de_dados import BancoDeDados
from utils.valida_cpf import gera_cpf


class TestStringMethods(unittest.TestCase):
    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ["1", "1", nome, cpf, "12.345.678-x", "12/12/2012", "86082147", "casa", "100", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
        }

        consulta = BancoDeDados()
        clientes = consulta.select(cliente_esperado)

        cliente_esperado = consulta.select(cliente_esperado)

        self.assertEquals(cliente_esperado, clientes)

