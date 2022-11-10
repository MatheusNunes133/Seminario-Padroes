""" Criando classe """


class Animal():

    """ Construtor da classe """

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    """ Método da classe """

    def comer(self):
        return f"O {self.nome} da cor {self.cor} está comendo"
