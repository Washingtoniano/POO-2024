

class GestorRepartidor():
    __lista:list
    def __init__(self) -> None:
        self.__lista=[]

    def agregar(self,dato):
        self.__lista.append(dato)