def retornar_menu_principal():
    retornar_menu_principal = input("Deseja retornar ao menu principal? (sim/não): ")
    if retornar_menu_principal == "sim":
        retorna_menu = True
    elif retornar_menu_principal == "não":
        retorna_menu = False
    return retorna_menu

def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado
