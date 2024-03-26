registros = {}
aluno = input("insira o nome (PARE para parar): ")
while aluno != "PARE":
    media = (float(input(f"Digite a média de {aluno}: ")))
    registros[aluno] = media
    aluno = input("insira o nome (PARE para parar): ")
print(registros)

print("Os alunos aprovados foram: ")
for aluno,media in registros.items():
    if media >= 60:
        print(aluno)

print("Os alunos reprovados foram: ")
for aluno,media in registros.items():
    if media < 60:
        print(aluno)