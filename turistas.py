arquivo = ("SALIDA 10\n"
           "SALIDA 12\n"
           "SALIDA 10\n"
           "VUELTA 20\n"
           "ABEND")

dados = arquivo.splitlines()

jeeps = 0
turistas = 0

for linha in dados:
    linha = linha.split(" ")
    status_jeep = linha[0]
    if(status_jeep == "SALIDA"):
        jeeps += 1

    if(status_jeep == "VUELTA"):
        jeeps -= 1

    if len(linha) > 1:
        qnt_turista = linha[1]
        if(status_jeep == "SALIDA"):
            turistas += int(qnt_turista)

        if(status_jeep == "VUELTA"):
            turistas -= int(qnt_turista)


print(turistas)

print(jeeps)

