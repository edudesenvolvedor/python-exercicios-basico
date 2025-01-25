import string

arquivo = input()

alfabeto = list(string.ascii_uppercase)

arquivo = arquivo.upper()

print(alfabeto.index(arquivo) + 1)

