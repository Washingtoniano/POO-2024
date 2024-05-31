from Calefactor import calefactor
class calefactorG(calefactor):
    __matricula:str
    __calorias:int
    def __init__(self, marca, modelo, pais, precio, FPago, CCuotas, Promocion,Matricula,calorias) -> None:
        super().__init__(marca, modelo, pais, precio, FPago, CCuotas, Promocion)
        self.__calorias=int(calorias)
        self.__matricula=Matricula
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
        print (super().mostrar())
        print (("Calorias: {} Matricula:{} ".format(self.__calorias,self.__matricula)))
    
    def tojason (self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                pais=super().getPais(),
                FPago=super().getFPagos(),
                CCuotas=super().getCCuotas(),
                Promocion=super().getPromocion(),
                Matricula=self.getMatricula(),
                calorias=self.getCalorias(),


            )
        )
        return d
