# Importando módulo Geral
from geral import (tarefas)

# Função para limpar tela. Essa função só funciona no Windows
def limpar_tela():
    import os
    os.system("cls") # Clear Screen

# Função para adicionar nova tarefa
def adicionar_tarefa():
    nome = input('Nome da tarefa: ')
    descricao = input('Descreva a tarefa: ')
    prioridade = input('''
 __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __          
|                                                  |
|        A prioridade da tarefa é:                 |
|        Alta                                      |
|        Média                                     |
|        Baixa                                     |
|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __| 
-> ''').lower().strip()
    categoria = input('''
 __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __          
|                                                  |
|        A categoria da tarefa é:                  |
|        Fácil                                     |
|        Intermediária                             |
|        Difícil                                   |
|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __| 
-> ''').lower().strip()
    tarefas.append({'nome': nome, 'descrição': descricao, 'prioridade': prioridade, 'categoria': categoria})
    print('Tarefa adicionada com sucesso')

# Função para listar as tarefas adicionadas
def listar_tarefa():
    if not tarefas: 
        print('Não há tarefa cadastrada')
    else:
        for i, tarefa in enumerate(tarefas):
            print(f'Tarefa: {i + 1}')
            print(f'Nome: {tarefa["nome"]}')
            print(f'Descrição: {tarefa["descrição"]}')
            print(f'Prioridade: {tarefa["prioridade"]}')
            print(f'Categoria: {tarefa["categoria"]}')

# Função para marcar tarefa como concluída
def concluir_tarefa():
    listar_tarefa()
    i = int(input('Digite o número da tarefa concluída: ')) - 1
    if 0 <= i < len(tarefas):
        del tarefas[i]
        print('Tarefa concluída')
    else:
        print('Número de tarefa incorreto')

# Função para exibir tarefas por prioridade
def prioridade_tarefa():
    prioridade = input('''
 __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __          
|                                                  |
|        Digite a prioridade desejada:             |
|        Alta                                      |
|        Média                                     |
|        Baixa                                     |
|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __| 
-> ''').lower().strip()
    filtrar_prioridade = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    if filtrar_prioridade:
        print(f'Tarefas com prioridade: {prioridade}')
        for tarefa in filtrar_prioridade:
            print(tarefa['nome'])
    else:
        print('Prioridade não encontrada')

# Função para exibir tarefas por categoria
def categoria_tarefa():
    categoria = input('''
 __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __          
|                                                  |
|        Digite a categoria desejada:              |
|        Fácil                                     |
|        Intermediária                             |
|        Difícil                                   |
|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __| 
-> ''').lower().strip()
    filtrar_categoria = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    if filtrar_categoria:
        print(f'Tarefa na categoria: {categoria}')
        for tarefa in filtrar_categoria:
            print(tarefa['nome'])
    else:
        print('Categoria não encontrada') 

# Função para sair do programa
def sair():
    resposta = input('Deseja sair (sim/não)')
    return resposta.lower() == 'sim' or resposta.lower() == 's'
    
        

      

