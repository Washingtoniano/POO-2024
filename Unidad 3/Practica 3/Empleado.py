class empleado():
    __NyA:str
    __id:int
    __puesto:str
    def __init__(self,NYA,id,puesto) -> None:
        self.__NyA=NYA
        self.__id=id
        self.__puesto=puesto 
    def getNombre(self):
        return self.__NyA
    def getID(self):
        return self.__id
    def getPuesto(self):
        return self.__puesto
    
    def __str__(self) -> str:
        return ("Empleado:{} ID:{} Puesto:{}".format(self.__NyA,self.__id,self.__puesto))