def calcular_total(itens):
    total = 0
    for quantidade, valor in itens:
        total += quantidade * valor
    return total

itens = []
for i in range(2):
    _, quantidade, valor = input().split()
    itens.append((int(quantidade), float(valor)))

total = calcular_total(itens)

print(f"VALOR A PAGAR: R$ {total:.2f}")
