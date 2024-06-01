from Investigador import investigador
from Docente import docente
class docente_investigador(docente,investigador):
    __categoria:str
    __importeextra:float
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, **kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, **kwards)
        self.__categoria=kwards['categoria']
        self.__importeextra=kwards['extra']

    def getCategoria(self):
        return self.__categoria
    def getImpExtra(self):
        return self.__importeextra