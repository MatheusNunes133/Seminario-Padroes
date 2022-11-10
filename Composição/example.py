class A:
    def getNumber(self):
        return 5 * 2
class B:
    objeto = A()
    def getNumberFromObject(self):
        return self.objeto.getNumber()
    
OBJ = B()
print(OBJ.getNumberFromObject()) # saída vai ser 10