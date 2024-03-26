def arq2dic():
    arquivo = open('turma1m.csv','r',encoding='utf-8')
    alunos = arquivo.readlines()
    arquivo.close()
    dicionário = {}
    for aluno in alunos:
        matrícula = aluno.split(';')[0]
        nome = aluno.split(';')[1].replace('\n','')
        dicionário[matrícula] = nome
    return dicionário

meudicionário = arq2dic()
for matrícula,nome in meudicionário.items():
    print(f'[Matrícula: {matrícula}] [nome: {nome}]')