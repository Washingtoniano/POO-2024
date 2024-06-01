from Personal import personal
class apoyo(personal):
    __categoria=str

    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad,**kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__categoria=kwards['categoria']

    def getCategoria(self):
        return self.__categoria