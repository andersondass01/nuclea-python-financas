import psycopg2
import os


def retornar_parametro_conexao_banco_de_dados():
    parametros_conexao = {
        "user": os.getenv('user'),
        "password": os.getenv('password'),
        "host": os.getenv('host'),
        "port": os.getenv('port'),
        "database": os.getenv('database')
    }
    return parametros_conexao


def conexao_postgres():
    connection = psycopg2.connect(**retornar_parametro_conexao_banco_de_dados())
    cursor = connection.cursor()
    return cursor, connection


def seleciona_cliente_banco_de_dados():
    print("Buscando clientes no banco de dados...")
    select_query = "SELECT * FROM cliente"
    cursor, connection = conexao_postgres()
    cursor.execute(select_query)
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    return clientes


def insert_cliente_banco_de_dados(nome, cpf, rg, data_nascimento, cep, logradouro, complemento, bairro, cidade, estado,numero_casa):
    print("Inserindo clientes no banco de dados...")
    insert_query = """INSERT INTO public.cliente( nome, cpf, rg, data_nascimento, cep, lougradouro, complemento, bairro, cidade, estado, numero_residencia)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cursor, connection = conexao_postgres()
    values = (nome, cpf, rg, data_nascimento, cep, logradouro, complemento, bairro, cidade, estado, numero_casa)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print("Cliente inserido com sucesso!")
    return


print("Execução banco de dados")
seleciona_cliente_banco_de_dados()
insert_cliente_banco_de_dados("Vanessa", "10178117099", "10.507.087-7", "1996-08-15", "08111340", "Rua André", "Casa",
                              "Jardim", "Londrina", "PR", "105")
seleciona_cliente_banco_de_dados()