amigos = ('joão','chico','ana','maria')

#transforma a tupla em lista, possibilitando alteração
listaamigos = list(amigos)

#alteração na lista
listaamigos[1] = 'Francisco'

#converte a lista em tupla agr já alterada
amigos = tuple(listaamigos)
print(amigos)