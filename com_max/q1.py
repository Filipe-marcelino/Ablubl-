from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def descricao(self):
        pass

def descrever_forma(forma: FormaGeometrica):
  return forma.area(),forma.perimetro()

class Retangulo:
  def __init__(self, altura, largura):
    self.altura = altura
    self.largura = largura

  def area(self):
    return self.altura*self.largura

  def perimetro(self):
    return 2 * (self.altura + self.largura)

  def descricao(self):
    return f"sou um retangulo de altura {self.altura} e largura {self.largura}"


class circulo:
  def __init__(self,raio):
    self.raio = raio

  def area(self):
    return (2*3.14)*(self.raio**2)


  def perimetro(self):
    return 2*3.14*self.raio

  def descricao(self):
    return f'sou um círculo de raio {self.raio}'

#objeto = Retangulo(5,10)
#a,b = descrever_forma(objeto)
#print(a,b)
#objeto.descricao()
#print(objeto.descricao())

formas = [Retangulo(5,10),circulo(6), Retangulo(13,11),circulo(8)]
for f in formas:
  print(descrever_forma(f),f.descricao())