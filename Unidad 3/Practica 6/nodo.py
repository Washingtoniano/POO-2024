from Calefactor import calefactor
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
        print(self.__dato.mostrar())