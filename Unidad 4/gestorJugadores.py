from jugador import Jugador
class gestorJugadores():
    __lista=[]

    def __init__(self) -> None:
        self.__lista=[]
    def agregar(self,dato):
        self.__lista.append(dato)

    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            Jugador=[Jugador.tojason() for Jugador in self.__lista]
        )
        return d