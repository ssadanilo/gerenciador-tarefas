from operacoesMatematicas import(somar, subtrair, multiplicar, dividir, potencia, sair)

while True:
    print("CALCULADORA")
    print("Escolha a operação matemática")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potenciar")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            a = float(input("Digite um número"))
            b = float(input("Digite outro número"))
            print(somar(a,b))
        case 2:
            a = float(input("Digite um número"))
            b = float(input("Digite outro número"))
            print(subtrair(a,b))
        case 3:
            a = float(input("Digite um número"))
            b = float(input("Digite outro número"))
            print(multiplicar(a,b))
        case 4:
            a = float(input("Digite um número"))
            b = float(input("Digite outro número"))
            print(dividir(a,b))
        case 5:
            a = float(input("Digite um número"))
            b = float(input("Digite outro número"))
            print(potencia(a,b))
        case 6:
            print(sair())