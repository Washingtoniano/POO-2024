class moto():
    __patente:str
    __marca:str
    __nombre:str
    __apellido:str
    __kilometraje:float
    def __init__(self,patente,marca,nombre,apellido,kilometraje):
        self.__patente=patente
        self.__marca=marca
        self.__nombre=nombre
        self.__apellido=apellido
        self.__kilometraje=kilometraje

    def __str__(self) :
        return("Patente:{}--Marca:{}--Nombre:{}--Apellido:{}--Kilometraje:{}".format(self.__patente,self.__marca,self.__nombre,self.__apellido,self.__kilometraje))
    def getpatente(self):
        return self.__patente
    def getNombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido