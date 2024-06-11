#FUNDAMENTAL:
#El manejadro debe tener acceso al gestor de puntos y a las distintas interfaces gui
#Se necesitan dos listas una en el manejador y otra en el gui(se elminara y generara constantemente),se pueden sobrecargar los operadores para comparar los elementos.
import random
from inicio import inicio
from Gestor import gestor
from gameover import gameover

from jugador import Jugador
from gestorJugadores import gestorJugadores

#Manejador general
class manejador():
    __nombre:str
    __puntos:int
    __gesto:gestor
    __jueg:object
    
    
    def __init__(self,nom,encoder,juga) -> None:
        from juego import juego  
        self.__nombre=''
        self.__puntos=0
        self.__gesto=gestor()
        self.__encoder=encoder
        self.__jugadores=juga

        self.__nombre=str(nom)
        un=juego(self)
        self.__jueg=un



    def ejecutar(self):
        self.__jueg.mainloop()

    def comprobar(self,lista,ob):
        b=self.__gesto.comprobar(lista,ob)
        if b==0:
            ob.destroy()
            self.guardar()
            ungameover=gameover(self.__puntos)
            ungameover
        else:
            ob.setlista()
  
            ob.brillar()

    def getLista(self):
        return self.__gesto

    def getJugadores(self):
        return self.__jugadores
    def setPuntos(self,p):
        self.__puntos=int(p)

    def getPuntos(self):
        return self.__puntos
    
    def getnombre(self):
            return self.__nombre
    
    def cerrar(self):
        unpuntaje=unpuntaje(self.__nombre,self.__puntos)
        self.__jueg.destroy()
    def iniciar(self):
        self.__gesto.iniciar()
        


    def guardar(self):
        unpunto=Jugador(Jugador=self.getnombre(),Fecha=None,Hora=None,Puntaje=self.getPuntos())
        self.__jugadores.agregar(unpunto)
        d=self.__jugadores.tojson()
        self.__encoder.guardarJSONArchivo(d)





   




