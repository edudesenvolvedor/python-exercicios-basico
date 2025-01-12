arquivo = ("20\n"
           "15 6")

dados = arquivo.splitlines()
expediente = dados[0]
tempos_producao = dados[1]

tempo_total_producao = 0
for tempo in tempos_producao.split(" "):
    tempo_total_producao += float(tempo)

if tempo_total_producao > float(expediente):
    print("Deixa para amanha!")
else:
    print("Farei hoje!")