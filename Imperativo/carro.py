class Carro:
    def __init__(self, nova_cor):
        self.cor = nova_cor
        self.ligado = False
        self.velocidade = 0
        self.gasolina = 0

    def ligar(self):
        if self.gasolina > 0:
            print('Vruuuum....')
            self.ligado = True
        else:
            print('brrrrtt-')

    def acelerar(self):
        if self.ligado:
            print('brrum bruum bruum bruuuum!')
            self.velocidade += 10

    def abastecer(self, qtd):
        print('gulp gulp gulp')
        if self.gasolina + qtd > 50:
            excedente = (-50 + self.gasolina + qtd)
            qtd = qtd - excedente
            print(f'descartou {excedente}L')
        self.gasolina += qtd

carro1 = Carro('vermelho')

carro2 = Carro('preto')
carro2.gasolina = 20

carro3 = Carro('cinza')
carro3.gasolina = 20
carro3.abastecer(300)
carro3.ligar()
carro3.acelerar()
