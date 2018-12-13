class cFichas:
    def __init__(self,x):
        self.__nombre = x
        self.__posX = 0
        self.__posY = 0
        print(x)
    def getNombre(self):
        return self.__nombre
    def setNombre(x):
        self.__nombre = x
    def getPosX():
        return self.__posX
    def setPoxX(x):
        self.__posX = x
    def getPosY():
        return self.__posY
    def setPoxY(y):
        self.__posY = y
    def tiene(self,x):
        aux = self.__nombre
        if (x in self.getNombre()  or x in self.getNombre() ):
            return x
        else:
            return "-"

