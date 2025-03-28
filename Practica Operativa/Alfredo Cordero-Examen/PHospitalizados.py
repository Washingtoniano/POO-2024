from paciente import paciente
class hospitalizados(paciente):

    __NHabitacion:int
    __FIngreso:str
    __diagnostico:str
    __InterDias:int
    __descartables:float
    def __init__(self, **kwards) -> None:
        super().__init__(**kwards)
        self.__NHabitacion=int(kwards["habi"])
        self.__FIngreso=kwards["ingreso"]
        self.__diagnostico=kwards["diag"]
        self.__InterDias=int(kwards["dias"])
        self.__descartables=float(kwards["des"])
    def getHabitacion(self):
        return self.__NHabitacion
    def getIngreso(self):
        return self.__FIngreso
    def getDiagnostico(self):
        return self.__diagnostico
    def getDias(self):
        return self.__InterDias
    def getDescartables(self):
        return self.__descartables
    def calculo(self):
        total=self.__InterDias*150000+self.__descartables
        return total
    def mostrar(self):
        super().mostrar()
        print("N° Habitacion: {} Fecha Ingreso: {} Diagnostico: {} Dias de internacion: {} Descartables: {}".format(self.__NHabitacion,self.__FIngreso,self.__diagnostico,self.__InterDias,self.__descartables))