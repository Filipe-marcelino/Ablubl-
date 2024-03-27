def par():
    print('Número par')

def ímpar():
    print('Número impar')

for numero in range(1,11):
    print(f'O número {numero} é um ',end='')
    if numero % 2 == 0:
        par()
    else:
        ímpar()