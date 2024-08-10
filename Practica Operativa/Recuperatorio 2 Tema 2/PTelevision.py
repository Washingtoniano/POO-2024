from Planes import planes
class Television(planes):
    __CN:int
    __CI:int
    def __init__(self, **kwards) -> None:
        super().__init__(**kwards)
        self.__CI=int(kwards['CI'])
        self.__CN=int(kwards['CN'])

    def getCN(self):
        return self.__CN
    def getCI(self):
        return self.__CI
    def calcular(self):
        po=0
        if self.__CI>10:
            po=self.getPrecio()*15/100
        return po
    def tipo(self):
        return "Televisivo"
    def mostrar(self):
        super().mostrar()
        print("Canales Nacionales: {} Canales Internacionales: {}".format (self.__CN,self.__CI))