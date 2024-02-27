class Cachorro():
  def fazerSom(self):
    return 'Au Au!'

class Gato():
  def fazerSom(self):
    return 'Miau!'
  
class Petista():
    def fazerSom(self):
      return 'Pruuu!'

def fazerAnimalFalar(Cachorro):
  return Cachorro.fazerSom()

def fazerAnimalFalar(Gato):
  return Gato.fazerSom()

def fazerAnimalFalar(Petista):
  return Petista.fazerSom()

print(Cachorro.fazerSom(Cachorro))
print(Gato.fazerSom(Gato))
print(Petista.fazerSom(Petista))