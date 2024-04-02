def consultaCecilia():
    arquivo = open('cecília.txt','r',encoding='utf-8')
    dados = arquivo.readlines()
    arquivo.close()
    matricula = dados[0].replace('\n','')
    global nome
    nome = dados[1].replace('\n','')
    email = dados[2]
    return matricula,nome,email

consulta = consultaCecilia()
print(f'matrícula: {consulta[0]}')
print(f'nome completo: {consulta[1]}')
print(f'email: {consulta[2]}')

print(nome)