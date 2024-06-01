from Personal import personal
class investigador(personal):
    __area:str
    __tipo:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad,**kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__area=kwards['area']
        self.__tipo=kwards['tipo']
    def getTipo(self):
        return self.__tipo
    def getArea(self):
        return self.__area