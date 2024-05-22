class alquiler():
    __persona:str
    __id:str
    __Hora:int
    __minutos:int
    __duracion:int
    def __init__(self,cliente,cancha,hora,minutos,duracion) -> None:
        self.__duracion=int(duracion)
        self.__persona=cliente
        self.__id=cancha
        self.__Hora=int(hora)
        self.__minutos=int(minutos)
    def getMinutos(self):
        return int(self.__minutos)
    def getHora(self):
        return int(self.__Hora)
    def getId(self):
        return self.__id
    def getPersona(self):
        return self.__persona
    def getDuracion(self):
        return self.__duracion
    def __gt__(self,other):
        s=int(self.__Hora)+(self.__minutos/60)
        o=other.getHora()+(other.getMinutos()/60)
        return s>o
    '''def __lt__(self,other):
        s=self.__duracion/60
        o=other.getDuracion()/60
        return s<o
        '''
    def __str__(self) -> str:
        return ("Cliente:{:10}Cancha:{:10}Hora:{:10}Minutos:{:10}duracion:{:10}".format(self.__persona,self.__id,self.__Hora,self.__minutos,self.__duracion))