agenda = {}

for registro in range(0,5):
    nome = input("Insira o nome: ")
    número = int(input(f"Insira o número de telefone de {nome}:"))
    agenda[nome] = número



for registro in agenda.items():
    print(f"O tele fone de {nome} é {número}")
