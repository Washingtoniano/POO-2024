import abc
from abc import ABC
class publicacion(ABC):
    __titulo:str
    __categoria:str
    __precio:float

    def __init__(self,titulo,categoria,precio) -> None:
        self.__categoria=categoria
        self.__precio=precio
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo
    def getCategoria(self):
        return self.__categoria
    def getPrecio(self):
        return self.__precio
    def mostrar(self):
        print("Titulo: {} Categoria: {} Precio Base: {}".format(self.getTitulo(),self.getCategoria(),self.getPrecio()))
    @abc.abstractmethod
    def ImporteTotal():
        pass