import datetime as date
class Jugador:
    __jugador:str
    __dificultad:str
    __puntos:float
    __fecha:str
    __hora:str
    def __init__(self,**kwards) -> None:
        self.__jugador=kwards['Jugador']
        self.__dificultad=None
        self.__puntos=float(kwards['Puntaje'])
        today=date.date.today()
        hora=date.datetime.today()
        self.__fecha=str(today.day)+'/'+str(today.month)+"/"+str(today.year)
        self.__hora=str(hora.hour)+':'+str(hora.minute)+':'+str(hora.second)

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
    
    