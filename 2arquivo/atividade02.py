pares = open('pares.txt','a')
ímpares = open('impares.txt','a')
for numero in range(1,1001):
    print(numero)
    if numero%2 == 0:
        pares.write(str(numero))
    else:
        ímpares.write(str(numero))
pares.close
ímpares.close