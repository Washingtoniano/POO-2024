from Personal import personal
class apoyo(personal):
    __categoria=str

    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad,**kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,**kwards)
        self.__categoria=kwards['categoria']

    def calcular(self):
        #Porcentaje por categoría: 10% si la categoría es de 1 a 10, 20 % si la categoría es de 11 a 20,  30% si la categoría es de 21 a 22.
        pass

    def getCategoria(self):
        return self.__categoria
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldo=super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                categoria=self.getCategoria()


            )
        )
        return d
    
    def mostrar(self):
        super().mostrar()
        print("Categoria: {}".format(self.__categoria))