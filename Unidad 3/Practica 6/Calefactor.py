import abc
from pathlib import Path
import json
class calefactor():
    __marca:str
    __modelo:str
    __pais:str
    __precio:float
    __FPago:str
    __CCuotas:int
    __promocion:str
    def __init__(self,marca,modelo,pais,precio,FPago,CCuotas,promocion) -> None:
        self.__marca=marca
        self.__modelo=modelo
        
        self.__CCuotas=CCuotas
        self.__FPago=FPago
        self.__pais=pais
        self.__precio=precio
        self.__promocion=promocion
    
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getCCuotas(self):
        return self.__CCuotas
    def getFPagos(self):
        return self.__FPago
    def getPais(self):
        return self.__pais
    def getPrecio(self):
        return self.__precio
    def getPromocion(self):
        return self.__promocion
    
    def CalcularTotal(self):
        return self.Calcular()-self.CalcularP()
    @abc.abstractmethod
    def Calcular():
        pass
    def CalcularP(self):
        precio=0
        if self.__promocion.upper()=="SI":
            precio=((self.getPrecio()*15)/100)
        return precio

    def mostrar(self):
        return ("Marca:{} Modelo:{} Pais: {} Precio: {} Forma de Pago:{} Cant.Cuotas:{} Promocion:{}")