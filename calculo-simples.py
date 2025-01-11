dado = "12 1 5.30 \n 16 2 5.10"

lista_produtos = dado.split("\n")

valor_total = 0

for produto in lista_produtos:
    produto = produto.strip()
    produto = produto.split(" ")
    codigo = produto[0]
    quantidade = int(produto[1])
    valor = float(produto[2])
    valor_total = valor_total + (valor * quantidade)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')