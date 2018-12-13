import singleton

class cJugador:
    def __init__(self,nombre,fichas):
        self.__nombre=nombre
        self.__tantos=0
        self.__maxTantos=singleton.OnlyOne()
        self.fichas = fichas
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self.__nombre=nom
    def getMaxTantos(self):
        return self.__maxTantos.val
    def setMaxTantos(self,x):
        self.__maxTantos.val=x
    def getTantos(self):
        return self.__tantos
    def setTantos(self,x):
        if(self.__tantos+x<self.__maxTantos.val):
            self.__tantos=self.__tantos+x
        else:
            self.__tantos=self.__tantos+x
            print("Ganaste")
