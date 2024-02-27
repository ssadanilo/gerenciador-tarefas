# Crie um app para caixa registradora

preco = 1
total = 0

while preco>0:
    preco = float(input('Digite o preço R$: '))
    total += preco
print(f'Total a pagar R${total} reais')


exit()

# Crie lista de inclusão, alteração e exclusão de dados

x=0
while True:
    print('1 - Inclusão')
    print('2 - Alteração')
    print('3 - Exclusão')
    print('3 - Sair')
    op  = input(': ')
    match (op):
        case '1':
            print('Inclusão de dados')
        case '2':
            print('Alteração de dados')
        case '3':
            print('Exclusão de dados')
        case '4':
            print('Sair')
            break
        
    

exit()

while True:
    print('A melhor escola de Informática: Infinity School')
    break

exit()

# Criar um app que verifica se a palavra digitada é um palíndromo

palavra = input('Digite uma palavra: ').strip().lower()
if palavra == palavra[::-1]:
    print(f'A {palavra} é um Palíndromo')
else:
    print(f'A {palavra} NÃO é um Palíndromo')

exit()

# Criar um app que o usuário informa um texto, e o mesmo é impresso invertido
    
texto = input('Digite um texto: ').strip().upper()
# len() -> Length (tmanho da string) 
for letra in range(len(texto)-1,-1,-1):
    print(texto[letra], end=' ')

exit()

print( 'Infinity School'[::-1])
valor = int(input('Digite um Inteiro: '))

for numero in range(valor + 1):
    print(numero, end = ' ')


exit()

lista = list(range(1,100,2))
print(lista)

exit()

empresa = 'ARARA ANA'
for letras in empresa:
    print(letras)

exit()

lampadaEstaLigada = False
lampadaEstaLigada = not lampadaEstaLigada

exit()

nota = float(input('Informe a NOTA do Estudante: '))
faltas = int(input('Informe a quantidade de faltas: '))
if (nota>=7):
    if (faltas<10):
        print('Aprovado')
        
    if (nota>=7) and (faltas<10):
        print('Aprovado')
        

# TkInter | Simplegui | Qt5

exit()

estadoCivil = input('Informe seu Estado Civil: ').strip().upper()
match (estadoCivil):
    case 'SOLTEIRO':
        print('Estado Civil: Solteiro')
    case 'CASADO':
        print('Estado Civil: Casado')
    case 'VIUVO':
        print('Estado Civil: Casado')
    case _:
        print('Opção Inválida!')

exit()

minhaIdade: int = 22


# contador = 0

# while True:
#     if contador == 10:
#         print(contador)
#         break
    # elif contador == 8:
    #     print(contador)
    #     break
#     else:
#         contador += 1

# for numero in range(5):
#     print(numero)
# else:
#     print("else:", numero)
        
# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
# o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# nota = -1
# while nota < 0 or nota > 10:
#     nota = float(input('Digite a nota do aluno: '))
#     if nota == 10:
#         print('Aluno aprovado com honras')
#     elif nota >= 6:
#         print('Aluno aprovado')
#     else:
#         print('Aluno reprovado')



# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
# informações.

# usuario = input('Digite o nome de usuario: ')
# senha = input('Digite sua senha: ')

# while usuario == senha:
#     print('Erro')
#     senha = input('Digite uma nova senha: ')

# print("Acesso aceito")

# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# nome = input('Digite seu nome: ')
# while len(nome) <= 3:
#     nome = input('Nome inválido. Digite novamente: ')

# idade = int(input('Digite sua idade entre 0 a 150 anos: '))
# while idade < 0 or idade > 150:
#     idade = int(input('Idade inválida. Digite novamente: '))

# salario = int(input('Digite sua salario: '))
# while salario <= 0:
#     salario = int(input('É escravo? Digite um salário digno: '))

# sexo = input('Digite seu sexo: M - masculino ou F - feminino: ').upper()
# while sexo not in 'M F':
#     sexo = input('Sexo não reconhecido. Digite novamente: ').upper()

# estadoCivil = input('Digite seu estadoCivil: S - solteiro, C - casado, V - viúvo ou D - divorciado: ').upper()
# while estadoCivil not in 'SCVD':
#     estadoCivil = input('estadoCivil não reconhecido. Digite novamente: ').upper()

# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
# uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de
# anos necessários para que a população do país A ultrapasse ou iguale a população do
# país B, mantidas as taxas de crescimento.

# populacaoA = 80000
# populacaoB = 200000
# taxaA = 0.03
# taxaB = 0.015
# anos = 0

# while populacaoA <= populacaoB:
#     populacaoA += populacaoA * taxaA
#     populacaoB += populacaoB * taxaB
#     anos += 1
# print(f'Levará {anos} anos para a População A ultrapassar a População B')

# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas
# de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacaoA = floa(input("Digite a população inicial de A: "))
populacaoB = floa(input("Digite a população inicial de A: "))
taxaA = 
taxaB = 
anos = 

while populacaoA <= populacaoB:
     populacaoA += populacaoA * taxaA
     populacaoB += populacaoB * taxaB
     anos += 1
print(f'Levará {anos} anos para a População A ultrapassar a População B')

# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.


# 7. Faça um programa que leia 5 números e informe o maior número.


# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.


# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que
# estão no intervalo compreendido por eles.

