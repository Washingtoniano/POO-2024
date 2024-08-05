from Equipos import equipos
class nodo():
    __dato:equipos
    __sig:object
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__sig=None
    def getDato(self):
        return self.__dato
    def setSiguiente(self,sig):
        self.__sig=sig
    def getSiguiente(self):
        return self.__sig
