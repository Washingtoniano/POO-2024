from nodo import nodo
from zope.interface import implementer
from Personal import personal
from interfaz import Interface
@implementer(Interface)
class lista():
    __actual:nodo
    __comienzo:nodo
    __indice:int
    __tope:int
    def __init__(self) -> None:
        self.__actual=None
        self.__comienzo=None
        self.__indice=0
        self.__tope=0

    def AgregarElemento(self,dato):
        unnodo=nodo(dato)
        unnodo.setSiguiente(self.__comienzo)
        self.__comienzo=unnodo
        self.__actual=unnodo
        self.__tope+=1


    def __next__(self):
        if self.__tope==self.__indice:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            self.__indice+=1
            return dato
    def __iter__(self):
        return self
    
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            Personal=[personal.tojson() for personal in self]
        )
        return d
    
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.getDato().mostrar()
            aux=aux.getSiguiente()