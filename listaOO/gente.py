class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudar(self):
        print(f'Oi, eu sou {self.nome} e tenho {self.idade} anos')

    def envelhecer(self,anos):
        self.idade += anos

pessoa1 = Pessoa('Ciro',43)
pessoa2 = Pessoa('Mickeias',96)
pessoa3 = Pessoa('Ricaom',204)

for p in [pessoa1,pessoa2, pessoa3]:
    #print(f'{p.nome} tem {p.idade} anos')
    p.saudar()

pessoa1.envelhecer(5)
pessoa1.saudar()