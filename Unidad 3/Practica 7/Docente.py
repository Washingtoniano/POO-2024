from Personal import personal
class docente(personal):   
    __catedra:str
    __cargo:str
    __carrera:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, **kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,**kwards)
        self.__carrera=kwards['carrera']
        self.__cargo=kwards['cargo']
        self.__catedra=kwards['catedra']

    def calcular(self):
   #Porcentaje por cargo: 10 % si el cargo es simple, 20% si el cargo es semiexclusivo, 50% si el  cargo es exclusivo
        sueldo=self.getSueldo()
        if self.__cargo.upper()=='SIMPLE':
            sueldo=sueldo*10/100
        elif self.__cargo.upper()=="SEMIEXCLUSIVO":
            sueldo=sueldo*20/100
        elif    self.__cargo.upper()=="EXCLUSIVO":
            sueldo=sueldo*50/100
        else:
            print("Cargo no valido detectado")
            sueldo=0
        return sueldo+(self.getSueldo()*self.getAntiguedad())/100
        



    def getCatedra(self):
        return self.__catedra
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldo=super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                carrera=self.getCarrera(),
                cargo=self.getCargo(),
                catedra=self.getCatedra()


            )
        )
        return d
    
    def mostrar(self):
        super().mostrar()
        print("Carrera: {} Cargo: {} Catedra: {}".format(self.__carrera,self.__cargo,self.__catedra))