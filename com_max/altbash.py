from abc import ABC, abstractmethod

class criptografia(ABC):
    @abstractmethod
    def criptografar(self,texto):
      pass

    @abstractmethod
    def descriptografar(self,texto):
      pass

class atbash:
  def __init__(self,texto):
    self.texto = texto

  def criptografar(self):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoC = alfabeto[::-1]
    texto = self.texto
    textoseguro = ""
    for letra in texto:
      if letra in alfabeto:
        localizacao = alfabeto.index(letra)
        textoseguro += alfabetoC[localizacao]
      else:
        textoseguro += letra
    return textoseguro

cifra = atbash('ifrn')
print(cifra.criptografar())
