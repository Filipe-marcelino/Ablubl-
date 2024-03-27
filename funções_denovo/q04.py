def parouimpar(num):
    if num % 2 == 0:
        mensagem = 'par'
    else:
        mensagem = 'ímpar'
    print(mensagem)

for numero in range(1,11):
    parouimpar(numero)