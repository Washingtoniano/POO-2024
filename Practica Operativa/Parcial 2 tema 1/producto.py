import abc
from abc import ABC
class producto(ABC):
    __nombre:str
    __fechaE:str
    __fechaV:str
    __temp:float
    __pais:str
    __lote:str
    __costo:float
    def __init__(self,nombre,FE,FV,Temp,pais,lote,costo) -> None:
        self.__costo=float(costo) 
        self.__fechaE=FE 
        self.__fechaV=FV 
        self.__lote=lote
        self.__nombre=nombre 
        self.__pais=pais
        self.__temp=Temp

    def getTemp(self):
        return self.__temp
    def getPais(self):
        return self.__pais
    def getFV(self):
        return self.__fechaV
    def getFE(self):
        return self.__fechaE
    def getLote(self):
        return self.__lote
    def getCosto(self):
        return self.__costo
    def getNombre(self):
        return self.__nombre
    
  
    def calculatTotal(self):
        return self.__costo+self.calcular()
    
    def mostrarFormato(self):
        print("\nNombre:{}  FE:{}  FV:{} Temp:{} Pais:{} Lote:{} Costo:{}".format(self.__nombre,self.__fechaE,self.__fechaV,self.__temp,self.__pais,self.__lote,self.calculatTotal()))
    
    @abc.abstractmethod
    def calcular():
        pass