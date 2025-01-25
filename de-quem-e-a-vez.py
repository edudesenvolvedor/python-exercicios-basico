def determinar_vencedor(rodada):

    resultado = 'IMPAR' if (rodada['N'] + rodada['M']) % 2 else 'PAR'
    return rodada['jogador1'] if rodada['jogada1'] == resultado else rodada['jogador2']

QT = int(input())

rodadas = []

for i in range(QT):
    jogador1, jogada1, jogador2, jogada2 = input().strip().split(' ')
    N, M = map(int, input().strip().split(' '))
    rodadas.append({
        'jogador1': jogador1,
        'jogada1': jogada1,
        'jogador2': jogador2,
        'jogada2': jogada2,
        'N': N,
        'M': M
    })

for i, rodada in enumerate(rodadas, start=1):
    vencedor = determinar_vencedor(rodada)
    print(f"{vencedor}")
