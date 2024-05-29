from Calefactor import calefactor
class calefactorE(calefactor):
    __potenciaMax:int
    def __init__(self, marca, modelo, pais, precio, FPago, CCuotas, promocion,PMAX) -> None:
        super().__init__(marca, modelo, pais, precio, FPago, CCuotas, promocion)
        self.__potenciaMax=PMAX
    def getPM(self):
        return self.__potenciaMax
    
    def Calcular(self):
        precio=super().getPrecio()
        if self.__potenciaMax> 1000:
            precio+=precio*1/100
        if self.__CCuotas>1:
            precio+=precio*30/100

        return precio
    
    def mostrar(self):
        print((super().mostrar()))
        print(("Potencia max{}".format(self.__potenciaMax)))
        
    def tojason (self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo,
                pais=super().getPais,
                FPago=super().getFPagos(),
                CCuotas=super().getCCuotas(),
                PMAX=self.getPM(),
                
            )
        )
        return d
