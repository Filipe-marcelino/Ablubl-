arquivo = open('pastel.txt','r')

lista = arquivo.readlines()

print(lista)

listaformatada = []
for item in lista:
    listaformatada.append((item.replace('\n','')))

print(listaformatada)

