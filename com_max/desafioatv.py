class Elevador:
    def __init__(self,tandares: int,capacidade: int):
        self.andar = 0
        self.tandares = tandares
        self.capacidade = capacidade
        self.carga = 0

    def entrar(self):
        if self.carga >= self.capacidade:
            print('O elevador está cheio, aguarde um momento')
        else:
            self.carga = self.carga + 1
            print(f'Há {self.carga} pessoas no elevador')
            

    def sair(self):
        if self.carga != 0:
            self.carga = self.carga - 1
            print(f'Há {self.carga} pessoas no elevador')
        else:
            print('Elevador vazio')

    def subir(self):
        if self.andar != self.tandares:
            self.andar = self.andar + 1
            print(f'O elevador está no {self.andar} andar')
        else:
            print('Já estamos no último andar')

    def descer(self):
        if self.andar != 0:
            self.andar = self.andar - 1
            print(f'O elevador está no {self.andar} andar')
        else:
            print('Não desce mais')    

    def morte(self):
        peso = self.carga*60
        velocidade = peso * (self.andar*6)
        if velocidade >= 6000:
            print('Há risco de morte')
        else:
            print('Não há risco de morte')

midway = Elevador(6,6)
midway.subir()
midway.entrar()
midway.entrar()
midway.subir()
midway.entrar()
midway.subir()
midway.sair()
midway.descer()
midway.entrar()
midway.morte()


