from Paquete import paquete
from Sucursal import sucursal
class repartidor():
    __numero:int
    __nombre:str
    __dni:str
    __paquete:list
    __sucursal:sucursal
    def __init__(self,id,nombre,dni,idsucursal=None) -> None:

        #¿El id es del empleado y el numero es la idd de sucursal?
        self.__dni=dni
        self.__numero=int(id)
        self.__nombre=nombre
        self.__sucursal=idsucursal


    def agregarpquete(self,paq):
        self.__paquete.append(paq)

    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__dni
    def getPaquete(self):
        return self.__paquete
    def getSucursal(self):
        return self.__sucursal
