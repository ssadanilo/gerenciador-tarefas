# turno = input("Que turno você estuda? \n M-Matutino, \n V-Vespertino, \n N-Noturno \n Digite a opção: ").upper()
# match turno:
#     case "M":
#         print("Bom dia!")
#     case "V":
#         print("Boa tarde!")
#     case "N":
#         print("Boa noite!")


# # Digite seu nome 5 vezes

# nome = input("Digite seu nome: ")
# for i in range(5):
#     print(nome)

#Contagem regressiva

# for i in range(6,0,-1):
#     print(i)


# for i in range(0,21,2):
#     print(i)

# for i in range(20,0,-2):
#     print(i)

# for i in range(0,20+1,2):
# #     print(i)

# for i in range(1,20,2):
#     print(i)


# Calcule a soma dos numeos de 1 ate 100

# numeros = list(range(1, 101))
# soma = sum(numeros)
# print(soma)

# soma = 0
# for i in range(1,101):
#     soma = soma+ i
# print(soma)

# palavra = "amor"

# for letra in palavra:
#     print(letra)

# Programa qe imprima a palavra ao contrario

# palavra = input("Digite uma palavra: ")

# for letra in palavra[::-1]:
#     print(letra)

# palavra = input("Digite uma palavra: ").upper()

# palavra2 = palavra[::-1]

# if palavra == palavra2:
#     print("É um palindromo")
# else:
#     print("Não é um palindromo")

# palavra = input("Digite uma palavra: ").upper()

# invertida = ""
# invertida = invertida.join(reversed(palavra))
# if invertida == palavra:
#     print("Palindromo")
# else:
#     print("Não é palindromo")

# for i in range(1,101,1):
#     print(i)

# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.


soma = 0
quantidade_de_numeros = 0

# Loop para ler números até que 0 seja digitado
while True:
    numero = int(input("Digite um número (digite 0 para encerrar): "))
    
    if numero == 0:
        break  # Sai do loop quando 0 é digitado
    
    soma += numero
    quantidade_de_numeros += 1

# Verifica se foram digitados números antes de calcular a média
if quantidade_de_numeros > 0:
    media = soma / quantidade_de_numeros
else:
    media = 0

# Exibe os resultados
print(f"\nQuantidade de números digitados: {quantidade_de_numeros}")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")







