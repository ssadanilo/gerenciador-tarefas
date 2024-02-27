# palavra = 'bahia'

# for letra in palavra:
#     print(letra)

#===================================================

# alfabeto = 'abcdefghijlmnopqrstuvxwyz'

# for letra in alfabeto:
#     print(letra)

#=====================================================

# Faça um programa para imprimir os números de 1 a 10. Utilize a função 
# range() para criar a coleção de números.


# for numero in range(0,10):
#     print(numero)

#==================================================

# Faça um programa para imprimir os números pares de 1 a 20. Utilize a 
# função range() para criar a coleção de números

# for numeros in range(0,20,2):
#     print(numeros)

#=======================================================

# Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a 
# função range() para criar a coleção de números

# for numero in range(1,19,2):
#     print(numero)

#=======================================================

# Faça um programa para calcular a soma dos números de 1 a 100. Utilize a 
# função range() para criar a coleção de números

# soma = 0

# for numero in range(1,101):
#     soma += numero

# print(soma)

#=======================================================

# Faça um programa para calcular a média de uma lista de números

# soma = 0

# for numero in range(1,13):
#     soma += numero

# print(soma / 13)

#=======================================================

# Faça um programa para verificar se um número é primo. Utilize a 
# condicional IF dentro do laço FOR

# n = int(input("Verificar numeros primos ate: "))
# mult=0

# for count in range(2,n):
#     if (n % count == 0):
#         print("Múltiplo de",count)
#         mult += 1

# if(mult==0):
#     print("É primo")
# else:
#     print("Tem",mult," múltiplos acima de 2 e abaixo de",n)

#========================================================

# 7. Faça um programa para Imprimir os caracteres de uma string 
# separadamente.

# string = input('Digite uma string: ')

# for letra in string:
#     print(letra)

#========================================================

# Faça um programa para contar quantas vogais existem em uma palavra. 
# Utilize a condicional IF dentro do laço FOR

# def contar_vogais(palavra):
#     num_vogais = 0

#     for letra in palavra:
#         if letra.lower() in 'aeiou':
#             num_vogais += 1

#     return num_vogais

# palavra = input("Digite uma palavra: ")

# resultado = contar_vogais(palavra)
# print(f"O número de vogais na palavra '{palavra}' é: {resultado}")

# Faça um programa para contar quantas consoantes existem em uma 
# palavra. Utilize a condicional IF dentro do laço FOR.


# CADASTRO DE CLIENTES

# lista = []

# while True:
#     nome = input('Digite um novo nome (ou "sair" para finalizar): ').lower()
#     lista.append(nome)

#     if nome.lower() == 'sair':
#         break

# lista.remove('sair')
# print(lista)
# print('CADASTRO FINALIZADO COM SUCESSO')
    
        

