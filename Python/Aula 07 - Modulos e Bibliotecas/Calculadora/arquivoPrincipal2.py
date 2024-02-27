from operacoesMatematicas import(somar, subtrair, multiplicar, dividir, potencia, sair)

menu = {
    1: ["Somar", "somar()"],
    2: ["Subtrair", "subtrair()"],
    3: ["Multiplicar", "multiplicarr()"],
    4: ["Dividir", "dividirr()"],
    5: ["Potenciar", "potenciar()"],
    6: ["Sair", "sair()"],
}

while True:
    for item in menu:
        print(f"{item} - {menu[item][0]}")

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