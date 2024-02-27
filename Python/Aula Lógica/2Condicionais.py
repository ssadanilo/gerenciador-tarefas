# idade = int(input('Digite sua idade: '))
# if idade >= 18:
#     print('Você é maior de idade')

# nota = float(input ('Digite sua nota: '))
# if nota>= 7:
#     print('Congratulations')

# if nota<= 6.9:
#     print('Loser')


# idade = int(input('Digite sua idade: '))
# if idade >- 18:
#     print('Você é maior de idade')
# elif idade == 18:
#     print('Você tem exatamente 18 anos')
# else:
#     print('Você é menor de idade')

# nota = float(input('Digite sua nota: '))
# if nota >7:
#     print('Aprovado')
# elif nota ==7:
#     print('Na média')
# else:
#     print('Reprovado')

#programa que peça um valor e mostre se é positivo ou negativo


# n = float(input('Digite um número: '))
# if n>0 :
#     print('Este valor é positivo')
# elif n<0 :
#     print('Este número é negativo')
# else :
#     print('Este valor é neutro')

# #programa que peça um valor e mostre se é positivo ou negativo

# n = int(input("Informe um número:"))

# if n > 0:
#     print(f"O número {n} é positivo")
# elif n == 0:
#     print(f"O número {n} é igual a 0")
# else:
#     print(f"O número {n} é negativo")

# p1 = 'Banana'
# p2 = 'Manga'
# p3 = 'Abacaxi'

# p1 = float(input('Qual o preço da banana'))
# p2 = float(input('Qual o preço da manga'))
# p3 = float(input('Qual o preço da abacaxi'))

# if p1 > p2 and p1 > p3:
#     print('Compre p1')
# elif p2 > p1 and p2 > p3:
#     print('Compre p2')
# else: 
#     print('Compre p3')

# Verifique se uma letra digitada e vogal ou consoante

# letra = str(input('Digite uma letra: '))

# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#     print('Vogal')
# else:
#     print('Consoante')

# pri = float(input('Digite um número: '))
# seg = float(input('Digite um número: '))
# ter = float(input('Digite um número: '))

# if pri > seg and pri > ter:
#     print(pri)
# elif seg > pri and seg > ter:
#     print(seg)
# else:
#     print(ter)

pri = float(input('Digite um número: '))
seg = float(input('Digite um número: '))
ter = float(input('Digite um número: '))

maior = max(pri, seg, ter)
print('O maior número é: maior')