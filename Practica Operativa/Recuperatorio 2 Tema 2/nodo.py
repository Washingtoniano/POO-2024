from Planes import planes
class nodo():
    __dato:planes
    __sig:object
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__sig=None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__sig
    def setSiguiente(self,si):
        self.__sig=si