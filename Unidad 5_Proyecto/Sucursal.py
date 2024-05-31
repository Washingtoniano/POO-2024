from Repartidor import repartidor
from Paquete import paquete
from Transporte import transporte
class sucursal():
    __numero:int
    __provincia:str
    __localidad:str
    __direccion:str
    __paquetes:list
    __repartidor:list
    __transporte:transporte
    def __init__(self,numero,provincia,localidad,direccion,trans=None) -> None:
        self.__numero=int(numero)
        self.__provincia=provincia
        self.__localidad=localidad
        self.__direccion=direccion
        self.__paquetes=[]
        self.__paquetes=[]
        self.__transporte=trans
    def agregarPaquete(self,paquete):
        self.__paquetes.append(paquete)

    def agregarRepartidor(self,repartidor):
        self.__repartidor.append(repartidor)

    def getNumero(self):
        return self.__numero
    def getProvincia(self):
        return self.__provincia
    def getLocalidad(self):
        return self.__localidad
    def getDireccion(self):
        return self.__direccion
    


    def getRep(self,i):
        return self.__repartidor[i]
    def getPa(self,i):
        return self.__paquetes[i]
    def getTrans(self,i):
        return self.__transporte

