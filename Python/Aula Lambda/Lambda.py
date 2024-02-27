from functools import reduce


def quadrado(valor):
    return valor*valor

# Expressão lambda  (anônima ou inline)
quadrado = lambda valor : valor*valor
print(quadrado(3))

lista_numeros = list(range(1,1000))
print(lista_numeros)

#Filtrar os números pares:
numeros_pares = list(filter(lambda x: x%2==0, lista_numeros))
print(numeros_pares)

def pares(lista):
    listaPares = []
    for item in lista:
        if item%2==0:
            listaPares.append(item)
    return listaPares

# Mapeamento de interáveis (lista, tupla, sets, ...)
lista_cubo = list(map(lambda x: x**3, lista_numeros))
print(lista_cubo)

# Redução para um único valor (escalar)

valor = reduce(lambda x, acumulador = 1 : x * acumulador ,[1,2,3,4,5])
print(valor) 