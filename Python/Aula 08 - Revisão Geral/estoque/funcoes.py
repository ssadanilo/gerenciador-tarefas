from geral import (banco, )

def gerarCodigo():
    if len(banco) == 0:
        return 1
    else:
        len(banco) + 1

def incluir():
    while True:
        nome = input("Digite o NOME: ").upper().strip()
        preco = float(input("Digite o PREÇO: "))
        qt = int(input("Digite a QUANTIDADE: "))
        categoria = input("Digite a CATEGORIA: ").upper().strip()
        banco[gerarCodigo()] = [nome, preco, qt, categoria]
        escolha = input("Continuar a incluir (S/N)").upper().strip()
        if escolha != 'S': break

def listaGeral():
    print(banco)

def alterar():
    