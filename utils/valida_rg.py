import re

def valida_rg(rg):
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]{1}$'

    return bool(re.match(padrao_rg, rg))

rg = "00.000.000-X"

print(valida_rg(rg))

