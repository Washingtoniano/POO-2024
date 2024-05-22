class cabaña():
    __numero:int
    __CantHab:int
    __CantCG:int
    __CantCC:int
    __importe:float
    def __init__(self,numero,CH,CG,CC,impo) -> None:
        self.__CantCC=int(CC)
        self.__CantCG=int(CG)
        self.__CantHab=int(CH)
        self.__importe=float(impo)
        self.__numero=int(numero)
    

    def getCC(self):
        return self.__CantCC
    def getCG(self):
        return self.__CantCG
    def getCH(self):
        return self.__CantHab
    def getImporte(self):
        return self.__importe
    def getNumero(self):
        return self.__numero
    def __str__(self) -> str:
        return("Numero:{} CantHab:{} Camas grandes:{} Camas Chicas:{} Importe:{}".format(self.__numero,self.__CantHab,self.__CantCG,self.__CantCC,self.__importe))
    def __ge__(self,other):
        capacidad=self.__CantCG*2+self.__CantCC
        return capacidad>=other
