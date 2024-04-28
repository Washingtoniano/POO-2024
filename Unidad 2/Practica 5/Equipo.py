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
    def getnombre(self):
        return self.__nombre
    def getID(self):
        return self.__Id
    def __str__(self):
        return ("Equipo:{:10} ID:{:5} goles a favor{:5} goles en contra{:5} Diferencia de goles{:5} Puntos{:5}".format(self.__nombre,self.__Id,self.__golesF,self.__golesC,self.__golesDif,self.__puntos))
        #2 espacios, 2 espacio, 3 espacios, 2 espacio
    def getpuntos(self):
        return self.__puntos
    def getdif(self):
        return self.__golesDif
    def getGolF(self):
        return self.__golesF
    def __gt__(self,other):
        b= self.__puntos>other.getpuntos()
        if(self.__puntos==other.getpunts()):
            b=self.__golesDif > other.getdif()
        else:
            b=self.__golesF > other.getGolf()
        return b
    def actualizar(self,puntos,GF,GC):
        self.__puntos+=puntos
        self.__golesC+=GC
        self.__golesF+=GF
        self.__golesDif=self.__golesF-self.__golesC