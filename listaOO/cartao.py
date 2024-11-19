class cartao:
    def __init__(self,proprietario: str, id: int, limite: float, compras: list[dict] = []):
        self.proprietario = proprietario
        self.id = id
        self.limite = limite
        self.compras = compras

    def limite_disponivel(self):
        disponivel = self.limite
        for c in self.compras:
            disponivel -= c.['Valor']
        return disponivel
    
    def comprar(self, compra: dict):
        if self.limite_disponivel() >= compra['Valor']:
            self.compras += [compra]
            self.limite -= compra['Valor']


cartao1 = cartao('Bruno',123, 2000 [{}])