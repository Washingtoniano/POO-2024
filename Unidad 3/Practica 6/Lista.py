from nodo import nodo
from objectoencoder import ObjectEncoder
class lista():
    __comienzo:nodo
    __indice:int
    __tope:int
    __actual:nodo
    def __init__(self) -> None:
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def __iter__(self):
        return self
    def agregar(self,dato):
        Nodo=nodo(dato)
        Nodo.setSiguiente(self.__comienzo)
        self.__comienzo=Nodo
        self.__actual=Nodo
        self.__tope+=1

    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.mostrar()
            aux=aux.getSiguiente()
   
    def tojason(self):
        listado=[]
        d=dict(
            __class__=self.__class__.__name__,
            Calefactores=[calefactor.tojason()for calefactor in self]
        )
        return d