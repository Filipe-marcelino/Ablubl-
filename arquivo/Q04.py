A = []
linhas = int(input('Insira quantidade de linhas: '))
colunas = int(input('Insira quantidade de colunas: '))

for l in range(0,linhas):
    linha = []
    A.append(linha)
    for c in range(0,colunas):
        elemento = int(input(f'Insira o nome da posição {l}{c}: '))
        linha.append(elemento)        

print(A)
