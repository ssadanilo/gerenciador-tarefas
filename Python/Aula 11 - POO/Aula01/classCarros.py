class Veiculos():
  pass

class Carros(Veiculos):
  # Método especial (Construtor)
  # DUNDER (Double Underline)
  def __init__(self, marca, ano, maxima, cor='Branca'):
    self.marca = marca
    self.modelo = ano
    self.cor = cor 
    self.velMax = maxima
    self.veloAtual = 0
    self.ligado = False

  def acelerar(self):
    if self.ligado:
      if (self.veloAtual + 10) <= self.velMax:
        self.veloAtual += 10
      else:
        self.veloAtual = self.veloAtual

  def frear(self):
    if (self.veloAtual - 10) >= 0:
      self.veloAtual -= 10
    else:
      self.veloAtual = 0

  def ligarDesligar(self):
    if self.veloAtual == 0:
      self.ligado = not self.ligado
    else:
      if not self.ligado:
        self.ligado = True

class Triciclos:
  pass

# Mãe -> Filho
        # Super Classe -> Sub Classe
class Motocicletas(Carros, Triciclos):
  def __ini__(self, marca, ano, maxima, cor='Branca', descansoLateral = True):
      Carros().__init__(marca, ano, maxima, cor)
      Triciclos().__init__()

      self.descansoLateral = descansoLateral
