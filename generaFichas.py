from random import randint
import fichas
misfichas=["00","01","02","03","04","05","06","07","08","09",
           "11","12","13","14","15","16","17","18","19",
           "22","23","24","25","26","27","28","29",
           "33","34","35","36","37","38","39",
           "44","45","46","47","48","49",
           "55","56","57","58","59",
           "66","67","68","69",
           "77","78","79",
           "88","89",
           "99"]
class cGenera:
    def __init__(self):
        self.listas = []
        self.fichas55()
    def fichas55(self):
        for i in range(0,55):
            a = randint(0, 55)
            while misfichas[a-1] in self.listas:
                a = randint(0, 55)

            fFicha = fichas.cFichas(misfichas[a-1])
            self.listas.append(fFicha)
        return self.listas
