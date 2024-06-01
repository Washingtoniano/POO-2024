import abc
from pathlib import Path
import json
from abc import ABC
class calefactor(ABC):
    __marca:str
    __modelo:str
    __pais:str
    __precio:float
    __FPago:str
    __CCuotas:int
    __promocion:str
    def __init__(self,marca,modelo,pais,precio,FPago,CCuotas,Promocion) -> None:
        self.__marca=marca
        self.__modelo=modelo
        
        self.__CCuotas=int(CCuotas)
        self.__FPago=FPago
        self.__pais=pais
        self.__precio=float(precio)
        self.__promocion=Promocion
    
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
    
    def __lt__(self,other):
        b=False
        if self!=None and other !=None:
            b= self.__precio<other.getPrecio()
        return b

    def mostrarF(self):
        print ("Marca:{} Modelo:{} Pais: {} Precio: {} Forma de Pago:{} Cant.Cuotas:{} Promocion:{}".format(self.__marca,self.__modelo,self.__pais,self.__precio,self.__FPago,self.__CCuotas,self.__promocion))