#Los  clientes  solicitan  crear  Cuenta,  para  lo  que  la  aplicación  les  solicita:  Apellido,  nombre,  DNI, 
#teléfono, saldo, CVU, porcentaje anual por rendimiento (es el mismo para todas las cuentas).
class cuenta():
    __apellido:str
    __nombre:str
    __DNI:int
    __telefono:int
    __saldo:float
    __CVU:str
    __Porcentaje=0.18
    def __init__(self,apellido,nombre,DNI,telefono,saldo,CVU):
        self.__apellido=apellido
        self.__nombre=nombre
        self.__DNI=int(DNI)
        self.__telefono=int(telefono)
        self.__saldo=float(saldo)
        self.__CVU=CVU
    def __str__(self) :
        return("apellido:{}  Nombre:{}  DNI:{}  Telefono:{}  Saldo:{}  CVU:{}".format(self.__apellido,self.__nombre,self.__DNI,self.__telefono,round(self.__saldo,2),self.__CVU))

    # def getPorcentaje(self):
    #     return self.__Porcentaje
    def getSaldo(self):
        return self.__saldo
    def getCVU(self):
        return self.__CVU
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__DNI
    def setSaldo(self,S):
        self.__saldo=S
    def getTelefono(self):
        return self.__telefono
    # @classmethod
    # def setporcentaje(cls):
    #     return cls.Porcentaje
    @classmethod
    def getporcentaje(cls):
        return cls.__Porcentaje
    @classmethod
    def verPorcentaje(cls):
        print("Porcentaje {0:5.2f}%".format (cls.getporcentaje()))
    @classmethod
    def setporcentaje(cls,p):
        cls.__Porcentaje=p