from modulos.geral import (linhas, )
from modulos.funcoes import (incluir, excluir, limpaTela, alterar, listagemGeral)

def menuPrincipal(): 
    print('-' * linhas)
    print("  C A D A S T R O   D E   P R O D U T O S")
    print('-' * linhas)
    print("1 - Incluir produtos")
    print("2 - Alterar produtos")
    print("3 - Excluir produtos")
    print('.' * linhas)
    print("4 - Relatórios")
    print('.' * linhas)
    print("S - Sair")
    print('=' * linhas)
    opcao = input("Opção: ").upper().strip()
    print('=' * linhas)
    limpaTela()
    match(opcao):
        case '1':
            incluir()
        case '2':
            alterar()
        case '3':
            excluir()
        case '4':
            listagemGeral()
        case 'S':
            exit()
    limpaTela()



