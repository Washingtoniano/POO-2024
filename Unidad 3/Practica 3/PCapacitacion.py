class Pcapacitacion():
    __nombre:str
    __cod:str
    __duracion:int
    def __init__(self,nombre,cod,dura) -> None:
        self.__nombre=nombre
        self.__cod=cod
        self.__duracion=dura
    
    def __str__(self) -> str:
        return ("Nombre:{} Codigo:{} Duracion:{}".format(self.__nombre,self.__cod,self.__duracion))
    def getNombre(self):
        return self.__nombre
    def getCod(self):
        return self.__cod
    def getDura(self):
        return self.__duracion