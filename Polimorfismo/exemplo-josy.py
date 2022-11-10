class Carro:
    def buzinar(self):
        print("buzinou...")

class Carro2 (Carro):

    def buzinar(self):
        print("buzinou o carro da classe 2")

carro1 = Carro()
carro1.buzinar()

carro2 = Carro2()
carro2.buzinar()