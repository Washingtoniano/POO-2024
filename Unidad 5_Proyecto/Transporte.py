from Paquete import paquete
from Sucursal import sucursal
class transporte():
    __numero:int
    __fechaS:str
    __fechaLL:str
    __sucursal=sucursal
    __paquete=paquete
    def __init__(self,numerotransporte,fechasalida,fechallegada,Paquete=None,Sucursal=None) -> None:
        self.__numero=int(numerotransporte)
        self.__fechaLL=fechallegada
        self.__fechaS=fechasalida
        self.__paquete=Paquete
        self.__sucursal=Sucursal


    def getNumero(self):
        return self.__numero
    def getFechaL(self):
        return self.__fechaLL
    def getFechaS(self):
        return self.__fechaS
    
    def getPaquete(self):
        return self.__paquete
    def getSucursal(self):
        return self.__sucursal
    