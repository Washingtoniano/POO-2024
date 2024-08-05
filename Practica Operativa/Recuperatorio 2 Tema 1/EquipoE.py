from Equipos import equipos
class EquipoE(equipos):
    __fuente:str
    def __init__(self, **kwards) -> None:
        super().__init__(**kwards)
        self.__fuente=kwards["fuente"]
    def getFuente(self):
        return self.__fuente
    def calcular(self):
        monto=0
        if self.__fuente.upper()=="BATERIA":
            monto=self.getTraifa()*10/100
        return monto
    def mostrar(self):
        super().mostrar()
        print("Fuente de alimentacion: {}".format(self.__fuente))
