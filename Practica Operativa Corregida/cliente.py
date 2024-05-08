class cliente():
    __nombre:str
    __apellido:str
    __Dni:int
    __Ntarjeta:int
    __saldoAnt:int
    def __init__(self,nombre,apellido,DNI,numero,saldo):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__Dni=int(DNI)
        self.__Ntarjeta=int(numero)
        self.__saldoAnt=float(saldo)
    def getDNI(self):
        return self.__Dni
    def getN(self):
        return self.__Ntarjeta
    def getNombreYApellido(self):
        return self.__apellido+self.__nombre
    def putsaldo(self,Act):
        self.__saldoAnt+=Act
    def getsaldo(self):
        return self.__saldoAnt
    def __str__(self) -> str:
        return ("Nombre:{:10}Apellido:{:10}DNI:{:10}numero:{:10}saldo:{:10}".format(self.__nombre,self.__apellido,self.__Dni,self.__Ntarjeta,self.__saldoAnt))
