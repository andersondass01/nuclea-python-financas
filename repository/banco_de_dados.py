import psycopg2
import os

from carteira import carteira_analise


class BancoDeDados:
    def __init__(self):
        self.connection = psycopg2.connect(**self.retornar_parametro_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente):
        print("Inserindo cliente no banco de dados")
        insert_query = """INSERT INTO public.cliente( nome, cpf, rg, data_nascimento, cep, lougradouro, complemento, 
        bairro, cidade, estado, numero_residencia)
	    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['cep']['CEP'],
            cliente['cep']['logradouro'],
            cliente['cep']['complemento'],
            cliente['cep']['bairro'],
            cliente['cep']['cidade'],
            cliente['cep']['estado'],
            cliente['numero_residencia']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def update(self, cliente):
        print("Atualizando cliente no banco de dados")
        update_query = """UPDATE public.cliente
        SET nome=%s, rg=%s, data_nascimento=%s, cep=%s, lougradouro=%s, complemento=%s, bairro=%s, cidade=%s, estado=%s, numero_residencia=%s
        WHERE cpf=%s;"""
        values = (
            cliente['nome'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['cep']['CEP'],
            cliente['cep']['logradouro'],
            cliente['cep']['complemento'],
            cliente['cep']['bairro'],
            cliente['cep']['cidade'],
            cliente['cep']['estado'],
            cliente['numero_residencia'],
            cliente['cpf']
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def delete(self, cliente):
        print("Deletando cliente no banco de dados")
        delete_query = "DELETE FROM public.cliente WHERE id=%s;"

        values = (
            cliente['id']
        )
        self.cursor.execute(delete_query, values)
        self.connection.commit()

    def select(self, cliente):
        print("Buscando clientes no banco de dados...")
        select_query = "SELECT * FROM cliente where cpf ='" + cliente['cpf'] + "';"
        self.cursor.execute(select_query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes

    def retornar_parametro_conexao_banco_de_dados(self):
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }

        return parametros_conexao
    def insert_ordem(self, atributos):
        print("Inserindo ordem de compra no banco de dados")
        insert_query = """INSERT INTO public.ordem (nome, ticket, valor_compra, quantidade_compra,
        data_compra, cliente_id)
	    VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (
            atributos['nome'],
            atributos['ticket'],
            atributos['valor_compra'],
            atributos['quantidade_compra'],
            atributos['data_compra'],
            atributos['cliente_id']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select_tickets(self, cliente):
        print("Buscando ações do cliente no banco de dados...")
        select_query = "SELECT ordem.ticket FROM cliente, ordem where cliente.id = ordem.cliente_id AND cliente.cpf='" + cliente['cpf'] + "';"
        self.cursor.execute(select_query)
        tickets = self.cursor.fetchall()
        for ticket in tickets:
            print(ticket)
        carteira_analise(tickets)

        return tickets


# cliente_teste = {}
# banco_de_dados = BancoDeDados()
# cliente = {'cpf': '10178117099'}
# banco_de_dados.select_tickets(cliente)

# cliente_teste = {
#     'nome': input("Nome: "),
#     'cpf': valida_cpf(),
#     'rg': valida_rg(),
#     'data_nascimento': valida_data_nascimento(),
#     'cep': valida_cep(),
#     'numero_residencia': input("Número casa: ")
# }
# print(banco_de_dados.insert(cliente_teste))
