#FUNDAMENTAL:
#El manejadro debe tener acceso al gestor de puntos y a las distintas interfaces gui
#Se necesitan dos listas una en el manejador y otra en el gui(se elminara y generara constantemente),se pueden sobrecargar los operadores para comparar los elementos.
import random
from inicio import inicio
from Gestor import gestor

from jugador import Jugador
from gestorJugadores import gestorJugadores


class manejador():
    __nombre:str
    __puntos:int
    __gesto:gestor
    __jueg:object
    __inicio=inicio
    __gesP=gestorJugadores
    
    def __init__(self,nom) -> None:
        from juego import juego  
        self.__nombre=''
        self.__puntos=0
        self.__gesto=gestor()
        self.__gesP=gestorJugadores()
        
        self.__nombre=nom
        un=juego(self)
        self.__jueg=un
    def ejecutar(self):
        self.__jueg.mainloop()

    def comprobar(self,lista):
        b=self.__gesto.comprobar(lista)
        return b

    def getLista(self):
        return self.__gesto.getListad()

    def juego(self):
        self.__puntos=self.__jueg.Darpuntos()
    def cargar(self):
        unjugador=Jugador(Jugador=self.__nombre,Puntaje=self.__puntos)
        self.__gesP.agregar(unjugador)
    def setPuntos(self,p):
        self.__puntos=p
    def getPuntos(self):
        return self.__puntos
    def getnombre(self):
        self.__nombre=self.__inicio.darNombre()
        print(self.__nombre)
 
    def cerrar(self):
        unpuntaje=unpuntaje(self.__nombre,self.__puntos)
        self.__jueg.destroy()
    def iniciar(self):
        self.__gesto.iniciar()
        
    #def over(self):
    #    self.__jueg.destroy()
        


    """""
    def iniciar(self):
        self.__juego=juego()
        print(type(self.__juego.gestorPuntos))
        input("")
        #self.__juego.brillar()
        #self.__juego.after(200,self.brillar())
        #self.__juego.brillar()
        #self.__juego.gestorPuntos.comprobar(self.__juego.lista)
    """""


    def ver(self,k):
        self.__jueg=k
        self.__jueg.brillar(self.__gesto.getListad())

    def datP(self):
        return self.__inicio.puntos()




   




