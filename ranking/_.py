open('ranking.txt','a',).close()
while True:
    arq = open('ranking.txt',encoding='utf-8')
    linhas = arq.readlines()
    arq.close
    ranking = []
    for i in range(0,len(linhas),2):
        nome = linhas[i][:-1]
        pontuacao = int(linhas[i+1][:-1])
        nome_pontuacao = [pontuacao, nome]
        ranking.append(nome_pontuacao)
    print(sorted(ranking, reverse=True))

    nome = input('Jogador: (digite parar para parar)')
    if nome.lower() == 'parar':
        break
    pontuacao = input('Pontuação: ')
    arq = open('ranking.txt', 'a', encoding='utf-8')
    arq.write(nome + '\n' + pontuacao +'\n')
    arq.close