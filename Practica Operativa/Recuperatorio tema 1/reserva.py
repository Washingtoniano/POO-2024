class reserva():
    __numero:int
    __persona:str
    __cabaña:int
    __fecha:str
    __huespedes:int
    __dias:int
    __seña:float
    
    def __init__(self,num,persona,cabaña,fecha,huespedes,dias,seña) -> None:
        self.__cabaña=int(cabaña)
        self.__dias=int(dias)
        self.__persona=persona
        self.__fecha=fecha
        self.__numero=int(num)
        self.__huespedes =int(huespedes)
        self.__seña =float(seña)
    def getCa(self):
        return self.__cabaña
    def getdias(self):
        return self.__dias
    def getpersona(self):
        return self.__persona
    def getnumero(self):
        return self.__numero
    def getHuespedes(self):
        return self.__huespedes
    def getseña(self):
        return self.__seña
    def getfecha(self):
        return self.__fecha
    def __str__(self) -> str:
        return ("Numero:{}Persona:{}Cabaña:{}Fecha:{}Huespedes:{}Dias:{}Seña:{}".format(self.__numero,self.__persona,self.__cabaña,self.__fecha,self.__huespedes,self.__dias,self.__seña))