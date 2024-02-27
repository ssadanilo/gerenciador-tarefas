lista = []

while True:
    nome = input('Digite um novo nome (ou sair para finalizar)').lower()
    lista.append(nome)
   
    if nome.lower() == 'sair':
        break
        
lista.remove('sair')
print(lista)
print('CADASTRO FINALIZADO')



# Crie uma lista de cadastro

minha_lista = []

# Definindo a quantidade de elementos que você deseja adicionar
quantidade_elementos = int(input("Quantos elementos você deseja adicionar? "))

# Usando um loop for para inputar dados na lista
for i in range(quantidade_elementos):
    elemento = input(f"Digite o elemento {i + 1}: ")
    minha_lista.append(elemento)

# Exibindo a lista
print(minha_lista)