qnt_pessoas = int(input())
lista_pessoas = input().strip().split(" ")

menor_valor = min(lista_pessoas)

index_menor_valor = lista_pessoas.index(menor_valor) + 1

print(index_menor_valor)
