from puntaje import puntaje
class jugador():
    __nombre:str
    __puntaje:puntaje
    def __init__(self,Jugador,**kwards) -> None:
        self.__nombre=Jugador
        self.__puntaje=puntaje(**kwards)

    def setPuntaje(self,p):
        self.__puntaje=p

    def getNombre(self):
        return self.__nombre
    def getPuntaje(self):
        return self.__puntaje
    

    def tojason(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Jugador=self.getNombre(),
                Fecha=self.getPuntaje().getFecha(),
                Hora=self.getPuntaje().getHora(),
                Puntaje=self.getPuntaje().getPuntos(),

            )
        )
        return d
