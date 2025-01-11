arquivo = "3\n8 0 7"

qnt_pessoas = int(arquivo.split("\n")[0].strip())
lista_pessoas = arquivo.split("\n")[1].strip().split(" ")

menor_valor = min(lista_pessoas)

index_menor_valor = lista_pessoas.index(menor_valor) + 1

print(index_menor_valor)
