import random
from inicio import inicio
from aplicacion import Ventana
class manejador():
    __ventana=object
    __lista=[]

    def __init__(self) -> None:
        self.__lista=[]
        self.__ventana=inicio()
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




