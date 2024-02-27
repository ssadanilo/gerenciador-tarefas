# Polimorfismo
class ContasCorrente:
  def __init__(self, numero, correntista):
      self.numero = numero
      self.correntista = correntista
      self.__saldo = 0
    
  # Decorator ( Disfarce )
  @property
  def movimentar(self): # GEtter
    return f'R$ {self.__saldo}'
  
  @movimentar.setter # Setter
  def movimentar(self,valor):
    if (self.__saldo + valor) >= 0:
      self.__saldo += valor
     
# -----------------------------
     
minhaConta = ContasCorrente('12345-0', 'Vinicius Costa')
print(minhaConta.movimentar) # Getter -> 0

minhaConta.movimentar = 100 # Setter

print(minhaConta.movimentar) # Getter -> 100







exit()

class Motores:
   def funcionar(self):
      return f'Motor ligado!'

objMotor1 = Motores()

class Carros:
  # Método construtor
  def __init__(self, maxima, objMotor1,cor='Branca'):
    # Atributos
    self.cor = cor
    self.veloMax = maxima
    self.motor = objMotor1
    self.__renavan = 123456 # O _ serve para avisar que essa inforção deve ficar protegida
    self.veloAtual = 0

  def frear(self):
     return f'freando...'

class Caminhoes(Carros):
    pass

# Estanciando objeto
objCaminhao = Caminhoes(cor='Vermelha', maxima=190, objMotor1=objMotor1)
objCarro = Carros(maxima=200, objMotor1=objMotor1)
print(objCaminhao.frear())
print(objCarro.motor.funcionar())
print(objCaminhao.motor.funcionar())
print(objCarro._renavan)
