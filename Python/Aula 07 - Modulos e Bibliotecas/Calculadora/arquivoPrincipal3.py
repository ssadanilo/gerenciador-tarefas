
from operacoesMatematicas import(somar, subtrair, multiplicar, dividir, potencia, sair)

menu = {
    1: ["Somar", "somar("],
    2: ["Subtrair", "subtrair("],
    3: ["Multiplicar", "multiplicar("],
    4: ["Dividir", "dividir("],
    5: ["Potencia", "potencia("],
    6: ["Sair", "exit()"],
}

while True:
    for item in menu:
        print(f"{item} - {menu[item][0]}")

    opcao = int(input("Escolha uma opção: "))
    valores = ""
    while True:
        valores+= input("Digite um valor")
        valores += ","
        resposta = input("S/N").upper()
        if resposta == "N": break
    valores = valores + ")"
    expressao = menu[opcao][1]+valores
    print(eval(expressao))
