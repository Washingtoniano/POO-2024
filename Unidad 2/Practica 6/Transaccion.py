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
        self.__importe=importe
        self.__Tipo=tipo
    def __str__(self):
        return("CVU:{}  N° de Transaccion:{}  Importe:{}  Tipo:{}".format(self.__CVU,self.__Ndetransaccion,self.__importe,self.__Tipo))