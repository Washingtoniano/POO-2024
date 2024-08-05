from Equipos import equipos
class EquipoP(equipos):
    __tipo:str
    __peso:int
    def __init__(self, **kwards) -> None:
        super().__init__(**kwards)
        self.__tipo=kwards["tipo"]
        self.__peso=int(kwards["peso"])
    def getPeso(self):
        return self.__peso
    def getTipo(self):
        return self.__tipo
    def calcular(self):
        monto=0
        if self.__peso >10:
            monto=self.getTraifa()*20/100
        return monto
    def mostrar(self):
        super().mostrar()
        print("Tipo: {} Peso: {}".format(self.__tipo,self.__peso))