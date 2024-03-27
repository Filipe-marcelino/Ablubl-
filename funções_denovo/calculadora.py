def soma():
    print(f'a soma é: {primeironum + segundonum}')
def subtracao():
    print(f'a subtração é: {primeironum - segundonum}')
def multiplicacao():
    print(f'a multiplicação é: {primeironum * segundonum}')
def divisao():
    print(f'a divisão é: {primeironum / segundonum}')
def raizquadrada(primeironum):
    print(f'a raiz quadrada de {primeironum} é {primeironum ** (1/2)}')


while True:
    primeironum = float(input('Insira o primeiro número: '))
    if primeironum == 0:
        break
    segundonum = float(input('Insira o segundo número: '))
    print(soma())
    print(subtracao())
    print(multiplicacao())
    print(divisao())
    print(raizquadrada(primeironum))
