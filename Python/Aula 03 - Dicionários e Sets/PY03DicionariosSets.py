# dicionario = {
#     "Modulo":"Phyton",
#     "Instituicao":"infinity School",
# }

# print(dicionario)

# lista = [] # Lista vazia
# lista2 = list() # Construtor de lista que ninguém usa
# tupla1 = tuple()
# tupla2 = (None,)

# dic = dict() # Construtor de dicionário que ninguém usa
# dic1 = {} # Dicionário vazio
# dic2 = {n:n**2 for n in range(11)}
# print(dic2)

# Criando um Dicionário com o Construtor da classe Dict
# dic3 = dict(
#     Hum = "Vinicius",
#     Dois = "Ana Clara",
#     Tres = "Maria Júlia",
#     )

# print(dic3)

# chave = input("Digite a Chave: ").strip()
# valor = input("Digite o Valor: ").strip()

# Inserir dados no dicionário
# dic3[chave] = valor
# print(dic3)

# dic4 = {
#     1: "Vinicius",
#     2: "Ana",
#     1: "Maria"
# }

# print(dic4)
# print(len(dic4)) # Saber o tamanho do dicionário #2

# Cópia do dicionário
# dic5 = dic4.copy()
# dic5[1] = "João"
# print("Dicionário 4: ",dic4)
# print("Dicionário 5: ",dic5)

# Exclusão de dados
# del dic4[2]
# print(dic4)
# backup = dic4.pop(1)
# print(backup) # Maria

# Inserir/ Alterar Valor:
# dic4[3] = "Juliana"
# print(dic4)

# dic4.clear()
# print(dic4)

# dic6 = ["Hum","Dois"]
# print(dict.fromkeys(dic6,0))

# dic7 = {}.fromkeys(range(1,41), True)
# print(dic7)
# dic7[33] = False

# print(dic7)
# print(dic7.items())

# input("...")
# print(list(dic7.values()))

# input("...")
# print(list(dic7.keys()))

# for chave, valor in dic7.items():
#     print(f"{chave} - {valor}")


# SET # Imprimindo vária vezes ele sai de fomra aleatória
# conj = {"Phyton", "Infinity", 77} 
# print(conj)

# a = set({1,2,3,4,5})
# b = set({9,8,7,6,5})
# c = set({"S","A","Z"})
# print("Interseção: ", a.intersection(b))
# print("União: ", a.union(b))

# Usando o SET para diminuir nomes repetidos em uma lista 
lista = ["a","b","c","d","b","e","b"]
lista2 = set(lista)
print(lista)
print(lista2)
lista2.remove("z")
print(lista2)

