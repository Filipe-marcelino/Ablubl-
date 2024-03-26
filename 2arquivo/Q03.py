

while True:
    nome = input('indique um amigo ou pae para parar: ')
    if nome == 'pare':
        break
    arquivo = open('amigos.txt','a')
    arquivo.write(f'{nome}\n')
    arquivo.close