from Personal import personal
class docente(personal):   
    __catedra:str
    __cargo:str
    __carrera:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, **kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__carrera=kwards['carrera']
        self.__cargo=kwards['cargo']
        self.__catedra=kwards['catedra']

    def getCatedra(self):
        return self.__catedra
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo