def parouimpar(num):
    if num % 2 == 0:
        mensagem = str(num) + ' É um número par'
    else:
        mensagem = str(num) + ' é um numero ímpar'
    return mensagem


for numero in range(1,11):
    print(parouimpar(numero))