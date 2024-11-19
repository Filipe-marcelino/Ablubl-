from datetime import date

class animal:
    def __init__(self,nome: str,ano: int,castrado: bool,vacinas: list[str] = []):
        self.nome = nome
        self.ano = ano
        self.idade = date.today().year - ano
        self.castrado = castrado
        self.vacinas = vacinas

    def vacinar(self, vacina):
        self.vacinas += [vacina]


ani1 = animal('Ícaro',2007,False)
print(ani1.nome, ani1.idade, ani1.castrado, ani1.ano, ani1.vacinas)
ani1.vacinar('poliomelite')
print(ani1.vacinas)