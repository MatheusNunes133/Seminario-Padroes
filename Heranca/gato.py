""" Importando Classe Animal """
from animal import Animal

""" Criando classe Gato """
""" OBS: Para herdar uma classe basta colocar o nome dela entre os parênteses da classe """


class Gato(Animal):

    """ Construtor """

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    """ Método da classe gato """

    def miar(self):
        return f"{self.nome}: Miau Miau Miau!!!"
