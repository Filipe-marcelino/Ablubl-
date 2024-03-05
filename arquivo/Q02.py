lista_nome = []
tupla_nome = ()
nome = input("digite um nome: ")
#transforma tupla em lista
lista1 = list(tupla_nome)

for letra in nome:
    lista_nome.append(letra)
    lista1.append(letra)

    print(letra)
print(lista_nome)

#transforma lista em tupla
tupla_nome = tuple(lista1)
print(tupla_nome)

#método alternativo
nome = input("digite um nome: ")

lista2 = list(nome)
print(lista2)