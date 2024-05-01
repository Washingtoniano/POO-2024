#Las  Transacciones  tienen:  CVU,  numero  de  transacción,  importe,  tipo  de  transacción  (‘D’-Débito, 
#‘C’-Crédito)
class Transaccion():
    __CVU:str
    __Ndetransaccion:int
    __importe:float
    __Tipo:str
    def __init__(self, CVU,N,importe,tipo):
        self.__CVU=CVU
        self.__Ndetransaccion=N
        self.__importe=float(importe)
        self.__Tipo=tipo
    def getCVU(self):
        return self.__CVU
    def getN(self):
        return self.__Ndetransaccion
    def getImporte(self):
        return self.__importe
    def getTipo(self):
        return self.__Tipo
    def __str__(self):
        return("CVU:{}  N° de Transaccion:{}  Importe:{}  Tipo:{}".format(self.__CVU,self.__Ndetransaccion,self.__importe,self.__Tipo))