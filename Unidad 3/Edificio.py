import numpy as np
from Departamento import departamento
class edificio():
    __id:int
    __nombre:str
    __cantP:int
    __cantD:int
    __direccion:str
    __nombreEmp:str
    __dep=[]
    def __init__(self,id,nombre,direc,nombreEmp,CP,CD) -> None:
        self.__id=int(id)
        self.__cantP=int(CP)
        self.__nombre=nombre
        self.__cantD=int(CD)
        self.__nombreEmp=nombreEmp
        self.__direccion=direc
        self.__dep=[]
    def __str__(self) -> str:
        return("ID:{:5}  Nombre:{:10}  Direccion:{:10}  Nombre empresa:{:10}  Cantidad Pisos:{:5}  Cantidad Dep:{:10}\nDepartamentos:\n".format(self.__id,self.__nombre,self.__direccion,self.__nombreEmp,self.__cantP,self.__cantD))
    
    def getID(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getCantP(self):
        return self.__cantP
    def getCantD(self):
        return self.__cantD
    def getNombreEmp(self):
        return self.__nombreEmp
    def getDireccion(self):
        return self.__direccion
    def getDimension(self):
        return self.__dimensiones
    
    def cargar(self,id,prop,piso,Ndep,CD,CB,sup):
        undp=departamento(id,prop,piso,Ndep,CD,CB,sup)
        self.__dep.append(undp)

    def mostraredifios(self):
        long=len(self.__dep)
        for i in range(long):
            print(self.__dep[i])
    def mostrarprop(self):
        long=len(self.__dep)
        for i in range( long):
            print(self.__dep[i].getprop())
    def suptotal(self):
        long =len(self.__dep)
        acum=0
        for i in range(long):
            acum+=self.__dep[i].getsup()
        return acum