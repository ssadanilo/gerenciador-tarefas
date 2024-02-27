from classCarros import (Carros, Motocicletas)
'''
# Estanciar objetos
chevette = Carros('GM', '1980', 180)
opala = Carros('GM', '1984', 180, 'Vermelha')
maverick = Carros('Ford', '1976', 220, 'Azul')

print('Chevette ligado?', chevette.ligado) # False
chevette.ligarDesligar()
print('Chevette Ligado?', chevette.ligado) # True
for a in range(19):
  chevette.acelerar()
  print('Velocidade Chevette =', chevette.veloAtual)

for k,v in (chevette.__dict__).items():
  print(k,v)
'''
cg150 = Motocicletas(ano='2020', marca='Honda', maxima=160, cor='Vermelha')
print(cg150.veloAtual) # 0
cg150.ligarDesligar()
cg150.acelerar()
print(cg150.veloAtual) # 10