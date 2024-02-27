# Contador
# contador = 0
# while (contador<5):
#     print(contador)
#     contador = contador + 1

# -----------------------------------------------------

# Contagm regressiva
# contador = 5
# while contador > 0:
#     print(contador)
#     contador -=1

# -----------------------------------------------------

# São o memso resultado
# soma+=numero
# soma = soma + numero

# -----------------------------------------------------

# Loop while que imprima os números pares de 2 até 10
# contador = 0
# numero = int(input('Digite um número: '))
# while contador < numero:
#     contador += 1
#     if contador %2 == 0:
#         print(f'É par: {contador}')
#     elif contador %2 != 0:
#         print(f'É ímpar {contador}')

# -----------------------------------------------------

# Adivinhe um número
# numero = 7
# numero_user = 0
# while numero != numero_user:
#     numero_user = int(input(f'Digite um valor entre 1 e 20: '))
#     if numero_user > numero:
#         print ('O número correto é menor que sua tentativa!')
#     elif numero_user < numero:
#         print('O número correto é maior que sua tentativa!')
#     else:
#         print('Acertou!')

# -----------------------------------------------------

# soma = 0
# limite = 20

# while True:
#     numero = int(input('Digite nuúmero: '))
#     soma += numero

#     if soma >= limite:
#         break

# print(f'A soma ultrapassou o limite de {limite}. A Somam final é {soma}')

# -----------------------------------------------------

# Faça um porgrama que solicite numeros, some os pares e imprima a soma
# soma_pares = 0
# limite = 50

# while True:
#     numero = int(input('Digite números até somar 50: '))
#     if numero %2 == 0 and soma_pares < limite:
#         soma_pares += numero
#     if soma_pares >= 50:
#         break
# print(f'Soma dos pares é {soma_pares}') 

# -----------------------------------------------------

# Somando numeros pares
# soma = 0

# for num in range(0,7,2): # inicio, fim, passo
#     soma += num
# print(soma)

# -----------------------------------------------------

# Programa que imprime numeros pares

# for i in range(2,11):
#     if i %2 == 0:
#         print(i)

# -----------------------------------------------------

# Loop para somar numeros de 1 ate 6
# soma = 0

# for i in range(1,5):
#     soma += i
#     print(soma)

# -----------------------------------------------------

# Crie uma programa que solicite 10 números para o usuário.
# O programa deve somar todos os números múltiplos de 6
# digitados. Se a soma for igual ou maior que 30, o programa
# dever parar e mostrar o resultado da soma.

soma = 0

for i in range(10):
    numero = input(f'Tentativa {i+1} digite o número: ')
    if not numero % 6: 
        soma += numero  
    if soma >= 30:
        break

print(f'{soma}')