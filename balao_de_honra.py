import string

arquivo = "c"

alfabeto = list(string.ascii_uppercase)

arquivo = arquivo.upper()

print(alfabeto.index(arquivo) + 1)

