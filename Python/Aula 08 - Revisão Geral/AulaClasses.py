# ============================================================================

# class Animal:
#     def fazer_som(self):
#         pass

# class Cachorro(Animal):
#     def fazer_som(self):
#         return "Au au!"
    
# class Gato(Animal):
#     def fazer_som(self):
#              return "Miau!"

# # Uso de herança0        
# dog = Cachorro()
# cat = Gato()

# print(dog.fazer_som())
# print(cat.fazer_som())

# ==============================================================================

# class Carro:
#     def __init__(self,marca:str,modelo:str,ano:int,cor:str,) -> None:
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.cor = cor

# print("Digite os atributos do automóvel: ")
# marca = input("Qual a marca? ")
# modelo = input("Qual o modelo? ")
# ano = int(input("Qual o ano? "))
# cor = input("Qual a cor? ")

# carro = Carro(marca,modelo,ano,cor)

# print(carro.__dict__)

# ================================================================================

# carro1 = Carro(marca = "bmw",modelo = "i3",ano = 2020,cor = "preta")
# carro2 = Carro(marca = "volvo",modelo = "i3",ano = 2023,cor = "azul")

# print(f"O carro 1 da marca {carro1.marca} e modelo {carro1.modelo}")

# =======================================================================================

# class Veiculo:
#     def __init__(self,marca:str,modelo:str,ano:str,cor:str,) -> None:
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.cor = cor

# class terrestre(Veiculo):
#     def __init__(self,marca:str,modelo:str,ano:str,cor:str,rodas:str,) -> None:
#         super().__int__(seff,modelo,ano,cor)
#         self.rodas = rodas

# class aquatico(Veiculo):
#     def __init__(self,marca:str,modelo:str,ano:str,cor:str,pes:str,) -> None:
#         super().__int__(seff,modelo,ano,cor)
#         self.pes = pes

# print("Digite os atributos do automóvel: ")
# marca = input("Qual a marca? ")
# modelo = input("Qual o modelo? ")
# ano = int(input("Qual o ano? "))
# cor = input("Qual a cor? ")
# rodas = input("Quantas rodas? ")
# pes = input("Quantos pés? ")

# carro = Veiculo(marca,modelo,ano,cor,rodas,pes,)

# print(carro.__dict__)

# CRIE UM RPG

