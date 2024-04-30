#Los  clientes  solicitan  crear  Cuenta,  para  lo  que  la  aplicación  les  solicita:  Apellido,  nombre,  DNI, 
#teléfono, saldo, CVU, porcentaje anual por rendimiento (es el mismo para todas las cuentas).
class cuenta():
    __apellido:str
    __nombre:str
    __DNI:int
    __telefono:int
    __saldo:float
    __CVU:str
    __Porcentaje:float
    def __init__(self,apellido,nombre,DNI,telefono,saldo,CVU,porcentaje=0.18):
        self.__apellido=apellido
        self.__nombre=nombre
        self.__DNI=DNI
        self.__telefono=telefono
        self.__saldo=saldo
        self.__CVU=CVU
        self.__Porcentaje=porcentaje
    def __str__(self) :
        return("apellido:{}  Nombre:{}  DNI:{}  Telefono:{}  Saldo:{}  CVU:{}  Porcentaje:{}%".format(self.__apellido,self.__nombre,self.__DNI,self.__telefono,self.__saldo,self.__Portcentaje))

    @classmethod
    def setporcentaje(self,P):
        self.__Porcentaje=P
    @classmethod
    def getporcentaje(self):
        return self.__Porcentaje