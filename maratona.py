arquivo = ("3\n"
           "1 1\n"
           "2 1\n"
           "2 3\n"
           "2\n"
           "2 16\n"
           "4 20\n")

def converter_arquivo_para_dict(arquivo):
    dict_treinos = {}
    count = 0

    dados = arquivo.splitlines()

    for linha in dados:
        linha = linha.strip()
        linha = linha.split(" ")
        if len(linha) < 2:
            count += 1
            dict_treinos[count] = {
                "qnt_treino": linha[0],
                "dados": {}
            }

    count = 0
    x = 0

    for linha in dados:
        linha = linha.strip()
        linha = linha.split(" ")
        if len(linha) < 2:
            count += 1
            x = 1
        if len(linha) > 1:
            dict_treinos[count]["dados"][x] = {
                "tempo": linha[0],
                "distancia": linha[1],
            }
            x += 1

    return dict_treinos

def calcular_velocidade_media(distancia, tempo):
    return distancia / tempo




dict_treinos = converter_arquivo_para_dict(arquivo)

record = 1
count_treinos = 1

print(record)
for treino in dict_treinos:
    dados = dict_treinos[treino]["dados"]
    qnt = dict_treinos[treino]["qnt_treino"]
    for dado in dados:
        if int(qnt) > count_treinos:
            count_treinos += 1
        else:
            count_treinos = 1
        velocidade_media = calcular_velocidade_media(float(dados[dado]["distancia"]),float(dados[dado]["tempo"]))
        if velocidade_media > record:
            record = velocidade_media
            print(dado)


