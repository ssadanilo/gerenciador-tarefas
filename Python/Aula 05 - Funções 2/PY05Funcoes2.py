# def quadrado(numero):
#     resultado = numero ** 2
#     return resultado

# resultado = quadrado(5)

# print("O quadrado de 5 é:", resultado)


# def soma(a,b,c):
#     return a+b+c

# a = int(input("Digite o primeira nota: "))
# b = int(input("Digite o segunda nota: "))
# c = int(input("Digite o terceira nota: "))

# resultado = soma(a,b,c)/3
# print("A média das notas é: ", resultado)



# def media(n1,n2,n3) -> float:
    
#     '''
#         Esta função calcula a média aritmética das notas do estudante
#         Entrada: 3 valores float (float)
#         Saída: Valor (escalar) das médias das notas (float)
#     '''
#     listaValores = n1,n2,n3
#     return sum((n1,n2,n3))/len(listaValores)

# #-------------------------------------------
# # App:
# notas = list()
# for indice in range(3):
#     notas.append(float(input(f"Digite a nota da prova {indice+1}: ")))
# listasNotasTexto = [str(nota) for nota in notas]
# a,b,c = notas
# print("Lista como string")
# print(f"Sua média foi {media(a,b,c)} nas notas: {','.join(listasNotasTexto)}")


# def calcular_area_retangulo(a1,a2):
#     return a1*a2

# a1 = int(input("Digite o comprimento do retângulo: "))
# a2 = int(input("Digite a largura do retângulo: "))

# resultado = calcular_area_retangulo(a1,a2)
# print("A área do retângulo é de: ",resultado)

#==========================================================================================

# def somarNumeros(*numeros):
#     listaNumeros = []
#     for valor in numeros:
#         listaNumeros.append(isinstance(valor,float))
#     if not all(listaNumeros):
#         return f"Argumentos NÃO podem ser strings"
#     soma = 0
#     for num in numeros:
#         soma += num
#         # soma = soma + num
#     return soma
    
# # Programa
# var1 = int(input("Digite o primeiro número: "))
# var2 = float(input("Digite o segundo número: "))
# print(f"Soma é {somarNumeros(var1,var2)}")
# print(f"Soma2 é {somarNumeros(var1,var2,100.0)}")
# print(f"Soma3 é {somarNumeros(var1,var2,'100')}")

#==========================================================================================

