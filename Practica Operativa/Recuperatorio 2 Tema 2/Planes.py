import abc
from abc import ABC
class planes(ABC):
    __Nombre:str
    __cobertura:str
    __duracion:int
    __precio:int
    def __init__(self,**kwards) -> None:
        self.__Nombre=kwards['nombre']
        self.__duracion=int(kwards['dura'])
        self.__cobertura=kwards["cober"]
        self.__precio=float(kwards['precio'])
    def getNombre(self):
        return self.__Nombre
    def getCobertura(self):
        return self.__cobertura
    def getDuracioN(self):
        return self.__duracion
    def getPrecio(self):
        return self.__precio
    
    def Total(self):
        return self.__precio+self.calcular()

    @abc.abstractmethod
    def tipo():
        pass
    @abc.abstractmethod
    def calcular():
        pass
    def mostrar(self):
            print("\nCompañia: {} Cobertura: {} Duracion: {} Precio: {}" .format(self.__Nombre,self.__cobertura,self.__duracion,self.__precio))
    def Mostrar(self):
        tipo=self.tipo()
        print("\nTipo de plan: {} Compañia: {} Cobertura: {} Duracion: {} Precio: {}" .format(tipo,self.__Nombre,self.__cobertura,self.__duracion,self.Total()))