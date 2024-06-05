import random
from inicio import inicio
from juego import juego
from inicio import inicio
class manejador():
   
    __inicio=inicio()
    __lista=[]

    def __init__(self) -> None:
        self.__lista=[]
        #self.__ventana=Ventana()
        self.__inicio=inicio()

    def inicio(self):
        self.__inicio.mainloop()
    def agregar(self,dato):
        self.__lista.append(dato)
    def iniciar(self):
        numero=self.random()
        self.agregar(numero)
    def random(self):
        return random.randint(1,4)
    """""
    def jugar(self):
        self.iniciar()
        while
            self.iniciar()
    """""




