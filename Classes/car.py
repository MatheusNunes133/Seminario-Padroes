""" Inicio da Classe/Objeto """


class Carro:

    """ Construtor """

    def __init__(self, nome, marca, cor, placa, modelo):
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.placa = placa
        self.modelo = modelo

    """ Método para retornar todas as informações """

    def informations(self):

        return f"Nome: {self.nome}\nMarca: {self.marca}\nCor: {self.cor}\nPlaca: {self.placa}\nModelo: {self.modelo}\n"

    """ Método para recuperar dados individuais  """

    def getNome(self):
        return self.nome

    def getMarca(self):
        return self.marca

    def getCor(self):
        return self.cor

    def getPlaca(self):
        return self.placa

    def getModelo(self):
        return self.modelo

    """ Metodos setters """

    def setNome(self, name):
        self.nome = name

    def setMarca(self, marca):
        self.marca = marca

    def setCor(self, cor):
        self.cor = cor

    def setPlaca(self, placa):
        self.placa = placa

    def setModelo(self, modelo):
        self.modelo = modelo
