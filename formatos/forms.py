import turtle
import time

class formas:
    def __init__(self, nome: str, cor: str, x: float, y: float):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
    
    def rabiscar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        self.desenhar_forma(t)
        t.end_fill()

    
    def desenhar_forma(self):
        raise Exception('Método abstrato.')


class quadrilatero(formas):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Quadrilatero', cor, x, y)
        self.largura = largura
        self.altura = altura
    
    def desenhar_forma(self, t:turtle.Turtle):
        for _ in range(2):
            for tam in [self.altura, self.largura]:
                t.forward(tam)
                t.right(90)

class triangulo(formas):
    def __init__(self, lado, cor, x, y):
        super().__init__('triangulo',cor, x, y)
        self.lado = lado
    
    def desenhar_forma(self, t:turtle.Turtle):
        for _ in range(0,3):
            t.left(120)
            t.forward(self.lado)

class circulo(formas):
    def __init__(self, raio, cor, x, y):
        super().__init__('roda',cor,x,y)
        self.raio = raio
    
    def desenhar_forma(self, t:turtle.Turtle):
        t.left(180)
        t.circle(self.raio)


base = quadrilatero(300,300,'blue',-150,150)
base.rabiscar()

teto = triangulo(300, 'red', 150, 150)
teto.rabiscar()

porta = quadrilatero(70,100, 'brown', 150, -75)
porta.rabiscar()

janela1 = circulo(30,'white',75,75)
janela1.rabiscar()

janela2 = circulo(30,'white',-75,75)
janela2.rabiscar()
