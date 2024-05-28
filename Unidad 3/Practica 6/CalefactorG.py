from Calefactor import calefactor
class calefactorG(calefactor):
    __matricula:str
    __calorias:int
    def __init__(self, marca, modelo, pais, precio, FPago, CCuotas, promocion,matricula,calorias) -> None:
        super().__init__(marca, modelo, pais, precio, FPago, CCuotas, promocion)
        self.__calorias=calorias
        self.__matricula=matricula
    def getMatricula(self):
        return self.__matricula
    def getCalorias(self):
        return self.__calorias
    
    def Calcular(self):
        precio=super().getPrecio()
        if self.__calorias>3000:
            precio+=precio*1/100
        if self.__CCuotas>1:
            precio+=precio*40/100

        return precio
    
    def mostrar(self):
    
     return (super().mostrar()("Calorias: {} Matricula:{} ".format(self.__calorias,self.__matricula)))
    
    def tojason (self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.__marca,
                modelo=self.__modelo,
                pais=self.__pais,
                FPago=self.__FPago,
                CCuotas=self.__CCuotas,
                Promocion=self.__matricula,
                calorias=self.__calorias


            )
        )
        return d
