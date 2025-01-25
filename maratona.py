def obter_entrada():
    N = int(input())  # Número de entradas
    velocidades = []

    for i in range(N):
        T, D = map(int, input().strip().split())
        velocidades.append((T, D))

    return N, velocidades

def calcular_maxima_velocidade(velocidades):
    Vmax = 0
    for i, (T, D) in enumerate(velocidades, start=1):
        V = D / T
        if V > Vmax:
            Vmax = V
            print(i)

def main():
    while True:
        try:
            N, velocidades = obter_entrada()
            calcular_maxima_velocidade(velocidades)
        except EOFError:
            break

main()
