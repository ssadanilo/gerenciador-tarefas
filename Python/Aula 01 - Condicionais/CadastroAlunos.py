alunos = dict()

while True:

    print("===" *3, "Menu", "===" *3)
    print("Digite a opção desejada:")
    print("[1] para adicionar um aluno")
    print("[2] para atualizar um aluno")
    print("[3] para visualizar todos os alunos")
    print("[4] para remover um aluno")
    print("[5] para encerrar")

    opcao = input("Digite abaixo a opção escolhida: ")

    if opcao == "1":
        matricula = int(input("Digite a matricula do aluno: "))
        alunos[matricula] = input("Nome: ")

    elif opcao == "2":
        for i in alunos.items():
              print(i)
              numero_matricula = int(input("Digite o número da matrícula do aluno a ser atualizado: "))
              alunos[matricula] = input("Nome: ")

    elif opcao == "3":
         for i in alunos.items():
            print(i)

    elif opcao == "4":
      for i in alunos.items():
         print(i)

      numero_matricula = int(input("Digite o número da matrícula do aluno a ser removido: "))
      del alunos[numero_matricula]

    elif opcao == "5":
      print("Programa encerrado")
      break

 