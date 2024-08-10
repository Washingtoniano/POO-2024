from Planes import planes
class Telefonia(planes):
    __tipo:str
    __min:int
    def __init__(self, **kwards) -> None:
        super().__init__(**kwards)
        self.__tipo=kwards['tipo']
        self.__min=int(kwards['min'])
    def getTipo(self):
        return self.__tipo
    def getMin(self):
        return self.__min
    
    def calcular(self):
        por=0
        if self.__tipo=='locales':
            por=self.getPrecio()*7.5/100
            por=por*(-1)

        else:
            por=self.getPrecio()*20/100
        return por
    def tipo(self):
        return "Telefonico"
    def mostrar(self):
        super().mostrar()
        print("Tipo de llamadas: {} Minutos: {}".format(self.__tipo,self.__min))