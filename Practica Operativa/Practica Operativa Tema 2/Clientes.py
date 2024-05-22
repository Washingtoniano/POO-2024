class clientes():
    __nombre:str
    __apellido:str
    __dni:int
    __saldo:float
    __numero:int
    def __init__(self,nombre,apellido,DNI,Num,saldo) -> None:
        self.__apellido=apellido
        self.__nombre=nombre
        self.__dni=int(DNI)
        self.__numero=int(Num)
        self.__saldo=float(saldo)
    def getNum(self):
        return self.__numero
    def getNomb(self):
        return self.__nombre
    def getApelli(self):
        return self.__apellido
    def getSaldo(self):
        return self.__saldo
    def getDNI(self):
        return self.__dni
    def setSaldo(self,acum):
        self.__saldo+=acum
    def __str__(self) -> str:
        return("Nombre:{:5}Apellido:{:5}DNI:{:5}Numero:{:5}Saldo:{:5}".format(self.__nombre,self.__apellido,self.__dni,self.__numero,self.__saldo))