import datetime as date
class puntaje:
    __dificultad:str
    __puntos:float
    __fecha:str
    __hora:str
    def __init__(self,**kwards) -> None:
        self.__dificultad=None
        self.__puntos=float(kwards['Puntaje'])
        self.__fecha=date.date.today()
        self.__hora=str(date.time.hour)+':'+str(date.time.minute)+':'+str(date.datetime.second)

    def getPuntos(self):
        return self.__puntos

    def getDificultad(self):
        return self.__dificultad
    def getFecha(self):
        return self.__fecha
    def getHora(self):
        return self.__hora
    

    def tojason(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Modo=self.getDificultad(),
                Fecha=self.getFecha(),
                Hora=self.getHora(),
                Puntaje=self.getPuntos(),

            )
        )
        return d