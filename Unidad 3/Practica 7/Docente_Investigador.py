from Investigador import investigador
from Docente import docente
class docente_investigador(docente,investigador):
    __categoria:str
    __importeextra:float
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, **kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,**kwards)
        self.__categoria=kwards['categoria']
        self.__importeextra=kwards['importeextra']

    def getCategoria(self):
        return self.__categoria
    def getImpExtra(self):
        return self.__importeextra
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldo=super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                carrera=super().getCarrera(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                area=super().getArea(),
                tipo=super().getTipo(),
                categoria=self.getCategoria(),
                importeextra=self.getImpExtra()
            )
        )
        return d
    def mostrar(self):
        super().mostrar()
        print("Categoria: {} ImporteExtra: {}".format(self.__categoria,self.__importeextra))