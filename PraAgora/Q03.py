registros = {}
while True:
    telefone = int(input("Digite o telefone ou [0] para parar: "))
    if telefone == 0:
        break
    nome = input((f"[{telefone}] Digite o nome: "))
    cidade = input((f"[{telefone}] Digte a cidade de {nome}: "))
    registros[telefone] = [nome,cidade]

print(registros)

while True:
    telefone = int(input('Telefone a consultar: '))
    if telefone == 0:
        break

    if telefone in registros.keys():
        print(f"O telefone {telefone} pertence a registros{registros[telefone[0]]}")
        print(f"Que mora na cidade: {registros[telefone[1]]}")