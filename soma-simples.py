arquivo = "30 \n 10"

primeiro_valor = int(arquivo.split("\n")[0].strip())
segundo_valor = int(arquivo.split("\n")[1].strip())

print(f'SOMA = {primeiro_valor + segundo_valor}')