Programa para gerenciar tarefas, com funções para adicionar nova tarefa, listar todas as tarefas, marca como concluídas, listar por prioridade e listar por categoria.
Ela já esta preparada para usar no ambiente virtual.

Passos que usei para ativar o ambiente virtual:

No terminal do VSCode digitar:
python -m venv nome_da_pasta

No terminal do VSCode digitar:
.\nome_da_pasta\Scripts\Activate.ps1

Caso dê erro, pesquisar no Windows o Windows PowerShell e digitar:  
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Retorna ao VSCode com: python -m venv nome_da_pasta

Dando certo essas etapas e aparecendo o nome da pasta no terminal, vai ao lado na pasta Lib que foi criada e digita:
pip install pymysql

Ao criar um arquivo para trabalhar, ele vai perguntar embaixo qual interpretador quer usar, use a recomendada do python para o ambiente virtual
