class equipo():
    __Id:int
    __nombre:str
    __golesF:int
    __golesC:int
    __golesDif:int
    __puntos:int
    def __init__(self,id,nombre,golF,golC,golD,puntos):
        self.__Id=int(id)
        self.__golesDif=int(golD)
        self.__golesF=int(golF)
        self.__golesC=int(golC)
        self.__puntos=int(puntos)
        self.__nombre=nombre