def par():
    return 'Número Par'

def ímpar():
    return 'Número ímpar'

for numero in range(1,11):
    print(f'{numero} é um ',end='')
    if numero % 2 == 0:
        print(par())
    else:
        print(ímpar())