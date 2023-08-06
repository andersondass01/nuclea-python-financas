from datetime import datetime
def valida_data_nascimento():

    while True:
        valida_data_nascimento = input("Data de nascimento: ")

        try:
            data_convertida = datetime.strptime(valida_data_nascimento, "%d/%m/%Y").date()

            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("Data de nascimento maior que a data atual. Tente novamente: ")
        except ValueError as e:
            print(f'Data de nascimento inválida "{e}". Tente novamente: ')

def valida_data_compra():

        while True:
            valida_data_compra = input("Data de compra: ")

            try:
                data_convertida = datetime.strptime(valida_data_compra, "%d/%m/%Y").date()

                data_atual = datetime.now().date()

                if data_convertida < data_atual:
                    return data_convertida.strftime("%d/%m/%Y")
                else:
                    print("Data de compra maior que a data atual. Tente novamente: ")
            except ValueError as e:
                print(f'Data de compra inválida "{e}". Tente novamente: ')