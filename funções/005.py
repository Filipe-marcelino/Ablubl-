def limpanome(nome):
    nomelimpo = nome.replace('\n','')
    return nomelimpo


arquivo = open('nomes.txt','r',encoding='utf-8')
nomes = arquivo.readlines()
arquivo.close()
nomeslimpos = []
for item in nomes:
    nomeslimpos.append(limpanome(item))

print(nomeslimpos)