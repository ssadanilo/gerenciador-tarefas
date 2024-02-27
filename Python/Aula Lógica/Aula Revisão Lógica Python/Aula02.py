lista_compras = []

def cadastrar_compras():
    nome_produto = input('Digite o nome: ')
    preco_produto = float(input('Digite o preço: '))
    qto_produto = int(input('Digite a quantidade: '))
    total_compra = preco_produto * qto_produto
    produtos_adquiridos = {f'Produto: {nome_produto} - Preco: {preco_produto} - Quantidade: {qto_produto} - Total: {total_compra}'}
    lista_compras.append(produtos_adquiridos)
    print(f'{produtos_adquiridos} adicionados com sucesso!')

def ver_compras():
    for produtos_adquiridos in lista_compras:
        print(produtos_adquiridos)
        
    
    total_compra = sum(produtos_adquiridos['total_compra'] for produtos_adquiridos in lista_compras)
    print(f'Total das compras: ', total_compra)

def atualizar_compras():
    nome_produto = input('Digite o nome: ')
    for produtos_adquiridos in lista_compras:
        if produtos_adquiridos['Produtos'] == nome_produto:
            produtos_adquiridos['Produto'] = input('Digite o novo nome: ')
            produtos_adquiridos['Preço'] = input('Digite o novo preço: ')
            produtos_adquiridos['Quantidade'] = input('Digite a nova quantidade: ')
            produtos_adquiridos['Total'] = produtos_adquiridos['Preço'] * produtos_adquiridos['Quantidade']
            return
    
def deletar_compras():
    nome_produto = input('Digite o nome do produto: ')
    for produtos_adquiridos in ver_compras:
        if produtos_adquiridos['Produto'] == nome_produto:
            lista_compras.remove(produtos_adquiridos)
            return

def menu():
    while True:
        print('1 - Adicionar compra')
        print('2 - Ver compras')
        print('3 - Atualizar compra')
        print('4 - Deletar compra')
        
        opcao = int(input('Digite a opção desejada: '))
        
        match opcao:
            
            case 1:
                cadastrar_compras()
                
            case 2:
                ver_compras()
                
            case 3:
                atualizar_compras()
                
            case 4:
                deletar_compras()
            case 5:
                print('Programa encerrado')
                break
            
if __name__ == '__main__':
    menu()