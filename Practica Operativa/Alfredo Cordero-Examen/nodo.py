from paciente import paciente

class nodo():
    __dato:paciente
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