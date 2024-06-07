import random
class gestor():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]

    def agregar(self,dato):
        self.__lista.append(dato)
    def iniciar(self):
        numero=self.random()
        self.agregar(numero)
    def random(self):
        return random.randint(1,4)
    def getListad(self):
        return self.__lista
    
    def comprobar(self,otro):
        b=0
        for i in range (len(self.__lista)):
            if self.__lista[i]==otro:
                b=1
        return b
    """""
    def __eq__(self, other) -> bool:
        n=False

        for i in range(len(self.__lista)):
            if self.__lista[i]==other(i):
                n=True

        return n
    """""
    