import abc
from abc import ABC
class equipos(ABC):
    __marca:set
    __modelo:str
    __añoF:str
    __tarifa:float
    __cantDi:int
    __cap:str
    __potencia:str
    __combustible:str
    def __init__(self,**kwards) -> None:
        self.__añoF=kwards["año"]
        self.__cantDi=int(kwards["dias"])
        self.__modelo=kwards["modelo"]
        self.__marca=kwards["marca"]
        self.__tarifa=float(kwards["tarifa"])
        self.__cap=kwards["cap"]
        self.__potencia=kwards["pot"]
        self.__combustible=kwards["com"]
 
    def getTraifa(self):
        return self.__tarifa
    def getAño(self):
        return self.__añoF
    def getDias(self):
        return self.__cantDi
    def getModelo(self):
        return self.__modelo
    def getMarca(self):
        return self.__marca
    def getCapacidad(self):
        return self.__cap
    def getPotencia(self):
        return self.__potencia
    def getCombustible(self):
        return self.__combustible
    def Total(self):
        return self.__tarifa*self.__cantDi+self.calcular()
    
    @abc.abstractmethod
    def calcular():
        pass
    def mostrar(self):
        print("\nMarca: {} Modelo: {} anio: {} Combustible: {} Potencia: {} Capacidad: {} AlquilerDiario: {} Cant.Dias.: {}".format (self.__marca,self.__modelo,self.__añoF,self.__combustible,self.__potencia,self.__cap,self.__tarifa,self.__cantDi))