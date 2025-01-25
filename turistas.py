def processar_evento(evento, quantidade, pessoas, jipes):
    if evento == "SALIDA":
        pessoas += quantidade
        jipes += 1
    elif evento == "ENTRADA":
        pessoas -= quantidade
        jipes -= 1
    return pessoas, jipes

def main():
    pessoas, jipes = 0, 0

    while True:
        entrada = input().strip().split(' ')
        
        if entrada[0] == "ABEND":
            break
        
        evento = entrada[0]
        quantidade = int(entrada[1])
        pessoas, jipes = processar_evento(evento, quantidade, pessoas, jipes)

    print(pessoas)
    print(jipes)

main()
