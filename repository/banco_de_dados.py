import psycopg2
import os

class BancoDeDados:
    def __init__(self):
        self.connection = psycopg2.connect(**self.retornar_parametro_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente):
        print("Inserindo cliente no banco de dados...")
        try:
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

            print("...Cliente inserido com sucesso no banco de dados")

        except Exception as e:
            print("Erro ao inserir cliente no banco de dados")
            print(e)

    def update(self, cliente):
        try:
            print("Atualizando cliente no banco de dados...")
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
        except Exception as e:
            print("Erro ao atualizar cliente no banco de dados")
            print(e)

    def delete(self, cliente):
        try:
            print("Deletando cliente no banco de dados...")
            delete_query = "DELETE FROM public.cliente WHERE cpf ='" + cliente['cpf'] + "';"

            values = (
                cliente['cpf']
            )
            self.cursor.execute(delete_query, values)
            self.connection.commit()
            print(f"...Cliente {cliente['cpf']} deletado com sucesso no banco de dados")
        except Exception as e:
            print("Erro ao deletar cliente no banco de dados")
            print(e)

    def select(self, cliente):
        print("Buscando clientes no banco de dados...")
        try:
            select_query = "SELECT * FROM cliente where cpf ='" + cliente['cpf'] + "';"
            self.cursor.execute(select_query)
            clientes = self.cursor.fetchall()
            for cliente in clientes:
                print(cliente)
            if len(clientes) == 0:
                print("Cliente não encontrado no banco de dados")
            return clientes
        except Exception as e:
            print("Erro ao buscar cliente no banco de dados")
            print(e)

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
        print("Inserindo ordem de compra no banco de dados...")
        try:
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
            print("...Ordem de compra inserida com sucesso no banco de dados")
        except Exception as e:
            print("Erro ao inserir ordem de compra no banco de dados")
            print(e)


    def select_tickers(self, cliente):
        print("Buscando ações do cliente no banco de dados...")
        try:
            select_query = "SELECT ordem.ticket FROM cliente, ordem where cliente.id = ordem.cliente_id AND cliente.cpf='" + cliente['cpf'] + "';"
            self.cursor.execute(select_query)
            tickers = self.cursor.fetchall()

            return tickers
        except Exception as e:
            print("Erro ao buscar ações do cliente no banco de dados")
            print(e)