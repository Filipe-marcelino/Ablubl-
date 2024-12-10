import turtle
import time

class formas:
    def __init__(self, nome: str, cor: str, px: float, py: float):
        self.nome = nome
        self.cor = cor
        self.px = px
        self.py = py
    
    def rabiscar(self, t: turtle.Turtle):
        t = turtle.Turtle()
        t.up()
        t.setx(self.px)
        t.sety(self.py)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
    
    def rabiscar(self):
        raise Exception('Método abstrato.')


class quadrilatero(formas):
    def __init__(self, largura, altura, cor, px, py):
        super().__init__('Quadrilatero', cor, px, py)
        self.largura = largura
        self.altura = altura
    
    def rabiscar(self, t: turtle.Turtle):
        
    
