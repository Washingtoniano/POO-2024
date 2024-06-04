from producto import producto
class productoC(producto):
    __nitrogeno:int
    __oxigeno:int
    __carbono:int
    __agua:int
    __metodo:str

    def __init__(self, nombre, FE, FV, Temp, pais, lote, costo,ni,ox,dio,agu,me) -> None:
        super().__init__(nombre, FE, FV, Temp, pais, lote, costo)
        self.__nitrogeno=int(ni)
        self.__agua=int(agu)
        self.__carbono=int(dio)
        self.__oxigeno=int(ox)
        self.__metodo=me

    def getNitrogeno(self):
        return self.__nitrogeno
    def getAgua(self):
        return self.__agua
    def getOxigeno(self):
        return self.__oxigeno
    def getCarbono(self):
        return self.__carbono
    def getMetodo(self):
        return self.__metodo
    def calcular(self):
        preci=super().getCosto()
        if self.__metodo.upper()=='MECANICO':
            preci=preci*15/100
        else:
            preci=preci*15/100
        return preci
    def mostrar(self):
        super().mostrarFormato()
        print("Metrodo de congelacion: {} Pocentaje de:  Nitrogeno:{}%  Oxigeno:{}%  Carbono:{}%  Agua:{}% ".format(self.__metodo,self.__nitrogeno,self.__oxigeno,self.__carbono,self.__agua))