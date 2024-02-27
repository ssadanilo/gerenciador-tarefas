from modulos.geral import (banco, )

def limpaTela():
    '''
    ATENÇÃO: Esta função só é funcional no Windows!
    '''
    import os
    os.system("cls") # Clear Screen


def geraCodigo():
    if len(banco) == 0:
        return 1
    else:
        return ( list(banco.keys() )[-1] ) + 1


#class clsSuperString(str):
class SuperString(str):
    def validaCategoria(self):
        if self in "AHPCLBR":
            return self
        else:
            return 'X'

def incluir():
    # Substitui a classe padrão 'str' pela classe customizada 'clsSuperString':
    #__build_class__.str = clsSuperString

    while True:
        nome = input("informe o NOME do Produto: ").strip().capitalize()
        preco = float( input("Informe o PREÇO do Produto: ") )
        qt = int( input("Informe a QUANTIDADE: ") )
        categoria = input(
        """
            A: Alimentos
            H: Higiene
            P: Padaria
            C: Congelados e frios
            L: Limpeza
            B: Bebidas
            R: Papelaria
        """
        ).strip().upper()
        categoria = SuperString( categoria )
        categoria = categoria.validaCategoria()
        ativo = True
        banco[geraCodigo()] = [nome, preco, qt, categoria, ativo]
        continua = input("Continua a Incluir (S/N)? ").strip().upper()
        if continua != 'S': break
        limpaTela()


def excluir():
    codigo = int(input("Digite o CÓDIGO do produto: "))
    if codigo in banco.keys():
        confirma = input(f"Confirma a exclusão do produto: {banco[codigo][0]} (S/N) ?").strip().upper()
        if confirma == "S":
            del banco[codigo]


def alterar():
    
    opcao = input("Digite: [N]ome, [P]reço, [Q]uantidade, [C]ategoria, [A]tivo: ").strip().upper()
    codigo = int( input("Informe o CÓDIGO do produto: ") )
    if codigo in list( banco.keys() ):
        match (opcao):
            case 'N':
                novoNome = input(f"Digite o NOVO Nome do produto {banco[codigo][0]}: ")
                banco[codigo][0] = novoNome
                # imprimindo:
                print(banco)
                input('Pressione qq tecla p/continuar...')
            case 'P':
                novoPreco = float(input(f"Digite o NOVO Preço do produto {banco[codigo][1]}: "))
                banco[codigo][0] = novoPreco
                # imprimindo:
                print(banco)
                input('Pressione qq tecla p/continuar...')
            case 'Q':
                novaQt = int(input(f"Digite a NOVA Quantidade do produto {banco[codigo][2]}: "))
                banco[codigo][0] = novaQt
                # imprimindo:
                print(banco)
                input('Pressione qq tecla p/continuar...')
            case 'C':
                novaCategoria = input(
                    f''' Categoria Atual: {banco[codigo][3]}
                    A: Alimentos
                    H: Higiene
                    P: Padaria
                    C: Congelados e Frios
                    L: Limpeza
                    B: Bebidas
                    R: Papelaria
                '''
                ).stripe().upper()
                novaCategoria = SuperString(novaCategoria)
                novaCategoria = novaCategoria.validaCategoria()
                banco[codigo][4] = not banco[codigo[4]]

            case 'A':
                banco[codigo][4] = not banco[codigo][4]
            case _:
                print("Opção inválida!!!")
            
    else:
        print(f"Código {codigo} inválido!!")
        input('')

def listagemGeral(): 
    for k, v in banco.items():
        if banco[k][4]:
         print(f"Código: {k}, Produto: {v[k][0]} - Preço: {banco[k][1]}")

    input("Pressione ENTER para continuar...")