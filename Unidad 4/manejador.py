#FUNDAMENTAL:
#El manejadro debe tener acceso al gestor de puntos y a las distintas interfaces gui
#Se necesitan dos listas una en el manejador y otra en el gui(se elminara y generara constantemente),se pueden sobrecargar los operadores para comparar los elementos.
import random
from inicio import inicio
from Gestor import gestor

from jugador import Jugador
from gestorJugadores import gestorJugadores

#Manejador general
class manejador():
    __nombre:str
    __puntos:int
    __gesto:gestor
    __jueg:object
  
    
    def __init__(self,nom) -> None:
        from juego import juego  
        self.__nombre=''
        self.__puntos=0
        self.__gesto=gestor()
        
        self.__nombre=str(nom)
        un=juego(self)
        self.__jueg=un
    def ejecutar(self):
        self.__jueg.mainloop()

    def comprobar(self,lista):
        b=self.__gesto.comprobar(lista)
        return b

    def getLista(self):
        return self.__gesto.getListad()


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








   




