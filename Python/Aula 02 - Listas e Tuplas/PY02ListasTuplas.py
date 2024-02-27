
# listaClientes = [
#                     ['Vinicius', 50, 1.78, True, 'Rua A', 26],
#                     ['Ana Clara', 50, 1.78, False, 'Rua B', 171],
#                 ]

# for cliente in listaClientes:
#     print(cliente)
    
# for indice in range(len(listaClientes)):
#     salario = float(input(f'Informe o SALÁRIO de {listaClientes[indice][0].upper()}: '))
#     listaClientes[indice].append(salario)
#     print(indice)
    
# listaSimples = [1,2,3,4]
# print(listaSimples)
# listaSimples.append(5) #insere ao final
# print(listaSimples)
# listaSimples.insert(0,9.9)
# listaSimples.insert(6,6)
# print(listaSimples)
# listaSimples[0] = 9.5 #alteração
# print(listaSimples)
# del listaSimples[-1] #excluindo o ltimo elemento
# print(listaSimples)
# backup = listaSimples.pop() #excluindo o último elemento e retorna uma cópia
# print(listaSimples)
# print(backup)
# print = ([1,2,3,4,5]).pop()


# lista22 = list()

# tupla = tuple()
# print(tupla)
# tupla1 = (1,2,3,4,5)
# print(tupla1)
# tuplaRange = tuple(range(10))
# print(tuplaRange)
# primeiro = tuplaRange[0]
# listaVazia = []
# listaVazia.append(primeiro)
# tuplaRange[9] = 0.001 # erro!


# Dada a tupla de nomes de países: ("Brasil", "Canadá", "Austrália", "Espanha", "Índia"), crie um
# programa que itere sobre a tupla e exiba na tela cada país seguido pelo número de
# caracteres presentes em seu nome.

paises = ["Brasil", "Canadá", "Austrália", "Espanha", "Índia"]

printf'([{nome}-{len(nome)}'for nome in paises')] # usando compreenção de listas
       
for pais in paises:
    print(f'{pais} {len(pais)}')
    
# Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
# preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
# que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.

produtosPreços = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]

soma = 0

for preço in produtosPreços:
    print(f'')