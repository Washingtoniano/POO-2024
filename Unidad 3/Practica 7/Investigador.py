from Personal import personal
class investigador(personal):
    __area:str
    __tipo:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad,**kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,**kwards)
        self.__area=kwards['area']
        self.__tipo=kwards['tipo']
    def getTipo(self):
        return self.__tipo
    def getArea(self):
        return self.__area
    
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldo=super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                area=self.getArea(),
                tipo=self.getTipo()


            )
        )
        return d
    def mostrar(self):
        super().mostrar()
        print("Area: {} Tipo: {}".format(self.__area,self.__tipo))