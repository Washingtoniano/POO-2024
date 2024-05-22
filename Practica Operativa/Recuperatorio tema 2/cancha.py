class cancha():
    __tipoPiso:str
    __id:int
    __importe:float
    def __init__(self,id,piso,importe) -> None:
        self.__id=id
        self.__importe=float(importe)
        self.__tipoPiso=piso
    def getPiso(self):
        return self.__tipoPiso
    def getId(self):
        return self.__id
    def getImporte(self):
        return self.__importe
    def __str__(self) -> str:
        return ("ID:{:10}Piso:{:10}Importe:{:10}".format(self.__id,self.__tipoPiso,self.__importe))