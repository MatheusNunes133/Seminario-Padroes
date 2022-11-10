""" Importando Classe Animal """
from animal import Animal

""" Criando classe Cachorro """
""" OBS: Para herdar uma classe basta colocar o nome dela entre os parênteses da classe """


class Cachorro(Animal):
    """ Criando construtor """

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    """ Criando método latir """

    def latir(self):
        return f"{self.nome}: Au Au Au!!!"
