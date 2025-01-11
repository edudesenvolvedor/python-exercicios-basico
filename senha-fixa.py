arquivo = "2200\n1020\n2022\n2002"

def valida_senha(senha):
    if senha == 2002:
        print("Acesso Permitido")
    else:
        print("Senha Invalida")

lista_senhas = arquivo.splitlines()
for senha in lista_senhas:
    senha = int(senha.strip())
    valida_senha(senha)

