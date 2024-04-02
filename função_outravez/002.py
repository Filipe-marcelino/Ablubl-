def calculadora(x,y):
    soma = x+y
    subtração = x-y
    multiplicação = x*y
    divisão = x/y
    return soma,subtração,multiplicação,divisão

while True:
    num1 = float(input('Digite o primeiro número (0 para parar): '))
    if num1 == 0:
        break
    num2 = float(input('Digite o segundo número: '))
    resultado = calculadora(num1,num2)
    print(f'A soma de {num1} e {num2} é {resultado[0]}')
    print(f'A subtração de {num1} e {num2} é {resultado[1]}')
    print(f'A multiplicação de {num1} e {num2} é {resultado[2]}')
    print(f'A divisão de {num1} e {num2} é {resultado[3]}')