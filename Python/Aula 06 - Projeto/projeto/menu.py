# Importando as funções
from funcoes import (limpar_tela, adicionar_tarefa, listar_tarefa, concluir_tarefa, prioridade_tarefa, categoria_tarefa, sair)

# Criando menu
def menu_opcoes():
    while True:
        print('''
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __          
    |                                                  |
    |        1 - Adicionar Tarefa                      |
    |        2 - Listar Tarefa                         |
    |        3 - Marcar Tarefa como Concluída          |
    |        4 - Exibir Tarefas por Prioridade         |
    |        5 - Exibir Tarefas por Categoria          |
    |        6 - Sair                                  |
    |__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __|                                                     
        ''')
        opcao = input('Digite o número da opção desejada: ')
        limpar_tela()
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefa()
        elif opcao == '3':
            concluir_tarefa()
        elif opcao == '4':
            prioridade_tarefa()
        elif opcao == '5':
            categoria_tarefa()
        elif opcao == '6':
            if sair():
                print('Programa encerrado')
                break
            else:
                print('voltano ao programa')        
        else: 
            print('Opção inválida')

