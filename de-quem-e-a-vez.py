arquivo = ("4\n"
           "Quico PAR Chiquinha IMPAR\n"
           "9 7\n"
           "Dami PAR Marcus IMPAR\n"
           "12 3\n"
           "Dayran PAR Conrado IMPAR\n"
           "3 1000000000\n"
           "Popis PAR Chaves IMPAR\n"
           "2 7")

testes = int(arquivo.split("\n")[0].strip())

partidas = arquivo.split("\n")[1:]

rodadas_jogadas = {}

def validar_nome(nome):
    if not nome.isalpha():
        raise ValueError("O nome contém caracteres invalido")
    if len(nome) > 100:
        raise  ValueError("Limite de caracteres de nome ultrapassado")

    return nome

def rodadas (jogadas, valores):
    jogador1 = jogadas.split(" ")[0].strip()
    escolha1 = jogadas.split(" ")[1].strip()
    valor1 = int(valores.split(" ")[0].strip())
    jogador2 = jogadas.split(" ")[2].strip()
    escolha2 = jogadas.split(" ")[3].strip()
    valor2 = int(valores.split(" ")[1].strip())

    return {
        "jogador_1": {
            "nome": validar_nome(jogador1),
            "escolha": escolha1,
            "valor": valor1,
        },
        "jogador_2":{
            "nome": validar_nome(jogador2),
            "escolha": escolha2,
            "valor": valor2,
        }
    }

count = 0
for i in range(0, len(partidas), 2):
    count += 1
    rodadas_jogadas[count] = rodadas(partidas[i], partidas[i + 1])

def validar_vencedor(rodada):
    soma_total = rodada['jogador_1']['valor'] + rodada['jogador_2']['valor']
    if soma_total % 2:
        if rodada['jogador_1']['escolha'] == 'IMPAR':
            return rodada['jogador_1']
        else:
            return rodada['jogador_2']
    else:
        if rodada['jogador_1']['escolha'] == 'PAR':
            return rodada['jogador_1']
        else:
            return rodada['jogador_2']

for rodada in rodadas_jogadas.values():
    print(validar_vencedor(rodada)['nome'])

