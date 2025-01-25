expediente = input()
tempos_producao = input()

tempo_total_producao = 0
for tempo in tempos_producao.split(" "):
    tempo_total_producao += float(tempo)

if tempo_total_producao > float(expediente):
    print("Deixa para amanha!")
else:
    print("Farei hoje!")
