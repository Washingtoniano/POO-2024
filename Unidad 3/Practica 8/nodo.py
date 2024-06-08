from Personal import personal
class nodo():
    __dato:personal
    __sig:object
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__sig=None

    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__sig
    def setSiguiente(self,sig):
        self.__sig=sig
    def __lt__(self,other):
        return self.__dato< other.getDato()
    def setDato(self,dato):
        self.__dato=dato