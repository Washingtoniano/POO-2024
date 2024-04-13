class CajaDeAhorro():
    __ncuenta=str
    __cuil=str
    __apellido=str
    __nombre=str
    __saldo=float
    def __init__(self,ncuenta=None,cuil=None,apellido=None,nombre=None,saldo=0.0):
        self.__ncuenta=ncuenta
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__saldo=saldo
    #def __str__(self):
       # return("Los datos son\n n°de cuenta:{} cuil: {} apellido:{} nombre:{} saldo:{}".format(self.__ncuenta,self.__cuil,self.__apellido,self.__nombre,self.__saldo))
    def mostrar(self):
        print("Los datos son\n n°de cuenta:{} cuil: {} apellido:{} nombre:{} saldo:{}".format(self.__ncuenta,self.__cuil,self.__apellido,self.__nombre,self.__saldo))
    def extraer(self,monto):
        resultado=-1
        if(self.__saldo>=monto):
            self.__saldo=self.__saldo-monto
            resultado=self.__saldo
        return resultado

    def depositar(self,monto):
        valor=-1
        if(monto>0):
            self.__saldo=self.__saldo+monto
            valor=self.__saldo
        return valor
    def comprobar(self, cuil):
        partes=cuil.split('-')
        if
        


        
                
            
