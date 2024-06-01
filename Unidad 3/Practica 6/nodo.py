from Calefactor import calefactor
from CalefactorE import calefactorE
class nodo():
    __dato:calefactor
    __siguiente:object
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__siguiente=None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self,sig):
        self.__siguiente=sig
    def mostrar(self):
        self.__dato.mostrar()

    def __lt__(self,other):
        return self.__dato< other.getDato()
    
