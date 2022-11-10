""" Importando a Classe """
from car import Carro

""" Criando instâncias da Classe  """
carro1 = Carro(nome="Corola", marca="Toyota", cor="Branco",
               modelo="2022", placa="QWE-1234")
carro2 = Carro(nome="Prisma", marca="Chevrolet",
               cor="Azul", modelo="2023", placa="THZ-7182")

""" Imprimindo as informações dos carros """
print("Informações dos carros:\n")
print(carro1.informations())
print(carro2.informations())
