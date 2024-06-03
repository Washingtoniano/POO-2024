class personal():
    __cuil:str
    __apellido:str
    __nombre:str
    __sueldo:float
    __antiguedad:int

    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,**kwards) -> None:
        self.__cuil=cuil
        self.__antiguedad=int(antiguedad)
        self.__sueldo=float(sueldo)
        self.__apellido=apellido
        self.__nombre=nombre
        
    def getCuil(self):
        return self.__cuil
    
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getAntiguedad(self):
        return self.__antiguedad
    def getSueldo(self):
        return self.__sueldo
    def __del__(self):
        print("Nos vamos a morir")
        del self
    
    def mostrar(self):
        print("Cuil: {} Apellido: {} Nombre: {} Sueldo: {} Antiguedad: {}".format(self.__cuil,self.__apellido,self.__nombre,self.__sueldo,self.__antiguedad))