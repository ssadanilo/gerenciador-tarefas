# PROGRAMA QUE ESCREVE BOAS VINDAS

# 10

# PROGRAMA QUE PEDE UM NOME E MOSTRA UMA MENSAGEM PROGRAMADA

# nome_criminoso = input('Digite seu nome: ')
# print(f'A Policia vai dar uma batida em uma casa cheia de drogas, e a casa é de {nome_criminoso}.')

# PROGRAMA QUE PEDE DOIS NÚMEROS DÁ A SOMA

# primeiro_numero = int(input('Digite um número: '))
# segundo_numero = int(input('Digite outro número: '))

# soma_total = primeiro_numero + segundo_numero
# print(f'A soma dos dois números é {soma_total}')

# PROGRAMA QUE PEDE 4 NOTAS E MOSTRA A MÉDIA

while True:
    nome_aluno = input('Digite o nome do aluno[para sair digite 0]: ')
    if nome_aluno == 0:
        break
    
    else: 
        nota_01 = int(input('Digite a primeira nota: '))
        nota_02 = int(input('Digite a segunda nota: '))
        nota_03 = int(input('Digite a terceira nota: '))
        nota_04 = int(input('Digite a quarta nota: '))

        media_notas = (nota_01 + nota_02 + nota_03 + nota_04) / 4

        if media_notas == 10:
            print('Parabéns! Você bota para f@@@')
        elif media_notas > 10 or media_notas < 0:
            print('Nota inválida')
        elif media_notas >= 7:
            print('Passou de ano')
        elif media_notas < 7 and media_notas > 5:
            print('Está na recuperação')
        elif media_notas <= 5:
            print('Perdeu de ano seu infeliz')




