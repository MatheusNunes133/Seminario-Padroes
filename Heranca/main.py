""" Importando Classes """
from gato import Gato
from cachorro import Cachorro

""" Instanciando Classes """
gato = Gato(nome="Alfie", cor="Branco")
cachorro = Cachorro(nome="Spike", cor="Preto")

""" Imprimindo métodos das classes """
print(gato.miar())
print(gato.comer())

print(cachorro.latir())
print(cachorro.comer())
