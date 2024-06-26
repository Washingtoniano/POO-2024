import datetime as date
class Jugador:
    __jugador:str
    __dificultad:str
    __puntos:int
    __fecha:str
    __hora:str
    def __init__(self,**kwards) -> None:
        self.__jugador=kwards['Jugador']
        self.__dificultad=None
        self.__puntos=int(kwards['Puntaje'])
        today=date.date.today()
        hora=date.datetime.today()
        if kwards["Fecha"] ==None:
            self.__fecha=str(today.day)+'/'+str(today.month)+"/"+str(today.year)
        else:
            self.__fecha=kwards["Fecha"]
        if kwards["Hora"]==None:
            self.__hora=str(hora.hour)+':'+str(hora.minute)+':'+str(hora.second)
        else:
            self.__hora=kwards["Hora"]

    def getPuntos(self):
        return self.__puntos

    def getDificultad(self):
        return self.__dificultad
    def getFecha(self):
        return self.__fecha
    def getHora(self):
        return self.__hora
    def getNombre(self):
        return self.__jugador
    

    def tojason(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Jugador=self.getNombre(),
                Fecha=self.getFecha(),
                Hora=self.getHora(),
                Puntaje=self.getPuntos()

            )
        )
        return d
    def __gt__(self,other):
        return self.__puntos>other.getPuntos()
    
    