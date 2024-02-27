
import random

direita=10
esquerda=1
# meio=(direita+esquerda)//2



print(" Pense em um número de 1 à 10")

palpite=random.randint(1,10)
# palpite=(direita+esquerda)//2

pergunta=""

while pergunta!="igual":
    pergunta=input(f"O numéro que vc pensou é maior menor ou igual a  {palpite}?\n")
    if pergunta == "maior":
        
        esquerda=palpite+1
        # print(direita)
        # print(esquerda)
        palpite=(direita+esquerda)//2
        if direita ==esquerda:
            print(f" O número pensado foi {palpite}")
            pergunta="igual"
        
    elif pergunta == "igual":
        print(f" O número pensado foi {palpite}")
        
    elif pergunta == "menor":

        direita=palpite-1
        # print(direita)
        # print(esquerda)
        palpite=(direita+esquerda)//2
        if direita ==esquerda:
            print(f" O número pensado foi {palpite}")
            pergunta="igual"
    else:
         print("resposta inválida")
    # palpite=(direita+esquerda)//2

