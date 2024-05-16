from Empleado import empleado
from PCapacitacion import Pcapacitacion
class matricula():
    __fecha:str
    __empleados:empleado
    __programas:Pcapacitacion
    def __init__(self,fecha,empleado,PC) -> None:
        self.__fecha=fecha
        self.__empleados=empleado
        self.__programas=PC

    def getPC(self):
        return self.__programas
    def getEmp(self):
        return self.__empleados
    def getFecha(self):
        return self.__fecha
    
    def __str__(self):
        return ("Fecha{} Empleado{} Programa de capacitacion{}".format(self.__fecha,self.__empleados,self.__programas))