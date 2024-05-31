from Repartidor import repartidor
from Transporte import transporte
from Sucursal import sucursal
class paquete():
    __numero:int
    __peso:float
    __NombreD:str
    __DireccionD:str
    __Entregado:bool
    __observacion:str
    __Repartidor:repartidor
    __Transporte:transporte
    __Sucursal:sucursal
    def __init__(self,numeroenvio,peso,nomdestino,DD,entregado,observacio,idsucursal,idtransporte,idrepartidor) -> None:
        self.__DireccionD=DD 
        self.__peso=float(peso)
        self.__Entregado= entregado
        self.__numero=int(numeroenvio)
        self.__observacion=observacio
        self.__NombreD=nomdestino

    

    def getNumero(self):
        return self.__numero
    def getPeso(self):
        return self.__peso
    def getNombreD(self):
        return self.__NombreD
    def getDireccionD(self):
        return self.__DireccionD
    def getEntregado(self):
        return self.__Entregado
    def getObservacion(self):
        return self.__observacion
    def getRepartidor(self):
        return self.__Repartidor

