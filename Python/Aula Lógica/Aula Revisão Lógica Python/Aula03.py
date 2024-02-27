while True:
    numero_errado = input('Digite um número: ').replace(',','.')

    if numero_errado.replace('.','').isdigit():
        numero_corrigido = float(numero_errado)
        print(f'O número infomado é {numero_corrigido}')
        break
    else:
        print('Incorreto! Digite um número')
    
# while True:
#     nome = input('Infomre seu nome: ')
#     idade = int(input('Informe sua idade: '))
#     altura = float(input('Informe sua altura: ').replace(',','.'))
#     cpf = int(input('Informe seu CPF: '))
#     print(f'Bem vindo {nome}, seus dados foram cadastrados com sucesso.\nIdade ={idade}, altura = {altura}, CPF = {cpf}.')
#     break

# while True:
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     soma = num1 + num2
#     print(f'A soma de {num1} e {num2} é {soma}')
#     break

# while True:
#     nota01 = float(input('Digite a primeira nota: ').replace(',','.'))
#     nota02 = float(input('Digite a segunda nota: ').replace(',','.'))
#     nota03 = float(input('Digite a terceira nota: ').replace(',','.'))
#     nota04 = float(input('Digite a quarta nota: ').replace(',','.'))
#     media = (nota01 + nota02 + nota03 + nota04) / 4
#     print(f'A média das notas é {media:.2f}')
#     break

# while True:
#     metro = float(input('Informe um valor em metros: ').replace(',','.'))
#     centimetros = metro * 100
#     print(f'{metro:.2f}m equivale a {centimetros:.2f}cm')

# while True:
#     lado_A = float(input('Informe a metragem do lado A: ').replace(',','.'))
#     lado_B = float(input('Informe a metragem do lado B: ').replace(',','.'))
#     quadrado = (lado_A * lado_B) * 2
#     print(f'O dobro da áera é {quadrado:.2f}')
#     break

# while True:
#     salario_hora = float(input('Qual valor do seu salário/hora?: ').replace(',','.'))
#     horas_trabalho = float(input('Quantas horas voçê trabalho no mês?: ').replace(',','.'))
#     salario_bruto = salario_hora * horas_trabalho
#     imposto_renda11 = (salario_bruto * 11) / 100
#     inss8 = (salario_bruto * 8) / 100
#     sindicato5 = (salario_bruto * 5) / 100
#     salario_liquido = salario_bruto - imposto_renda11 - inss8 - sindicato5
#     desconto_total = imposto_renda11 + inss8 + sindicato5
#     print(f'Seu salário no mês é R${salario_bruto:.2f} reais')
#     print(f'O Imposto de Renda desconta R${imposto_renda11:.2f} reais')
#     print(f'O INSS desconta R${inss8:.2f} reais')
#     print(f'O Sindicato desconta R${sindicato5:.2f} reais')
#     print(f'Os descontos totais foram de R${desconto_total:.2f} reais')
#     print(f'O seu Salário Líquido é de {salario_liquido:.2f} reais')
#     break


# while True:
#     valor = float(input('Digite um valor: ').replace(',','.'))
#     if valor >=0:
#         print('Número positivo')
#     else:
#         print('Número negativo')

# while True:
#     sexo = input('''
#                     Informe o sexo 
#                     digitando:
#                     M - para masculino
#                     F - para feminino
#                     --->''').upper()
#     if sexo == 'F' or sexo == 'M':
#         print('Opção cadastrada com sucesso')
#         break
#     else:
#         print('Sexo inválido')
#         print('Digite uma opção válida')

# nota1 = float(input('Digite a primeira nota ').replace(',','.'))
# nota2 = float(input('Digite a segunda nota ').replace(',','.'))
# media = (nota1 + nota2) / 2
# if media == 10:
#     print('Aprovado com distinção')
# elif media >= 7:
#     print('Aprovado')
# else: 
#     print('Reprovado')
# while True:
#     vodka = float(input('Digite o preço da Vodka ').replace(',','.'))
#     rum = float(input('Digite o preço do Rum ').replace(',','.'))
#     gin = float(input('Digite o preço do Gin ').replace(',','.'))
    
#     if vodka < rum and vodka < gin:
#         print(f'Vodka R${vodka} - Rum R${rum} - Gin R${gin}')
#         print('Compre VODKA, é mais barata')
#     elif rum < vodka and rum < gin:
#         print(f'Vodka R${vodka} - Rum R${rum} - Gin R${gin}')
#         print('Compre RUM, é mais barato')
#     else:
#         print(f'Vodka R${vodka} - Rum R${rum} - Gin R${gin}')
#         print('Compre GIN, é mais barato')

# while True:
#     salario_antes = float(input('Informe o salário ').replace(',',"."))
#     if salario_antes >= 1500:
#         reajuste = ((salario_antes * 5) / 100)
#         salario_novo = salario_antes + reajuste
#         print(f'O salário anterior é de R${salario_antes} reais')
#         print(f'Teve reajuste de 5% que equivale a R${reajuste} reais')
#         print(f'Sendo o novo salário de R${salario_novo}')
#     elif salario_antes > 700 and salario_antes < 1500 :
#         reajuste = ((salario_antes * 10) / 100)
#         salario_novo = salario_antes + reajuste
#         print(f'O salário anterior é de R${salario_antes} reais')
#         print(f'Teve reajuste de 10% que equivale a R${reajuste} reais')
#         print(f'Sendo o novo salário de R${salario_novo}')
#     elif salario_antes > 280 and salario_antes <= 700 :
#         reajuste = ((salario_antes * 15) / 100)
#         salario_novo = salario_antes + reajuste
#         print(f'O salário anterior é de R${salario_antes} reais')
#         print(f'Teve reajuste de 15% que equivale a R${reajuste} reais')
#         print(f'Sendo o novo salário de R${salario_novo}')
#     else:
#         reajuste = ((salario_antes * 20) / 100)
#         salario_novo = salario_antes + reajuste
#         print(f'O salário anterior é de R${salario_antes} reais')
#         print(f'Teve reajuste de 20% que equivale a R${reajuste} reais')
#         print(f'Sendo o novo salário de R${salario_novo}')
        








  






