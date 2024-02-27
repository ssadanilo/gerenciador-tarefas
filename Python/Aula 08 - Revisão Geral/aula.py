
# def saudacao (nome, *args, mensagem = "Olá", **kwargs):
#     saudacao_completa = f" {mensagem}, {nome}"
#     if args:
#         saudacao_completa += f" {', '.join(args)}"
#         if kwargs:
#             saudacao_completa += f"({', '.join(f'{k}={v}' for k, v in kwargs.items())})"
#             return saudacao_completa

# resultado = saudacao("Alice", "Bob", "Carol", mensagem = "Oi", idade = 30, cidade = "Nova York")
# print(resultado)
                     
#================================================================================================

# DADA UMA LISTA DE NÚMEROS, CRIE UMA NOVA LISTA CONTENDO APENAS OS NUMEROS PARES

# import random as rd

# lista = [rd.randint(1,100) for v in range(1000)]
# for v in lista:
#     if (v%2) == 0:
#         print(v, end = '-')
    
#================================================================================================

# CRIE UM CONJUNTO COM NOMES DE CORES. IMPLEMENTE UMA FUNÇÃO QUE NRETORNA AS CORES QUE TEM MAIS DE QUATRO LETRAS

# conjuntoCores = {"Azul", "Vermelho", "Verde", "Branco", "Rosa"}

# def maior4(conjunto):
#     listaRetorno = []
#     for cor in list(conjunto):
#         if len(cor)>4:
#             listaRetorno.append(cor)
#     return listaRetorno

# print(maior4(conjuntoCores))

#================================================================================================

# CRIE UMA FUNÇÃO QUE RECEBA UMA LISTA DE STRINGS E RETORNE UMA NOVA LISTA CONTENDO APENAS AS STRINGS PALÍNDROMOS

# def palindromo(texto):
#     return (True if texto.lower() == texto.lower()[::-1] else False)

#================================================================================================

# print(palindromo("Ana"))

#================================================================================================

# print("Infinity School"[::-1])
# print("Infinity School"[0:9])

#================================================================================================

endereco = "Rua do Camping, 910, casa 07"
temNumero = [c.isdigit() for c in endereco]
if any(temNumero):
    print("Não digite o número no ENDEREÇO")
if all(temNumero):
    print("Todos os caracteres são números")
else:
    print("Nem todos os caracteres são números")