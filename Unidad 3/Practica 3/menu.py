from gestorEmpleados import GEmpleado
from gestorMatriculas import GMariculas
from gestorProgramas import GProgramas
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4

        }
    def opcion(self,op,GM,GP,GE):
        fun=self.__switcher.get(op,lambda:print("dato erroneo"))
        if op=='1' or op=='2' or op=='3' or op=='4':
            fun(GM,GP,GE)
        else:
            fun()
    def opcion1(self,GM,GP,GE):
        if type(GM)==GMariculas and type(GP)==GProgramas and type(GE) ==GEmpleado:
            pass
        else:
            print("Parametro erroneo")

    def opcion2(self,GM,GP,GE):
        if type(GM)==GMariculas and type(GP)==GProgramas and type(GE) ==GEmpleado:
            pass
        else:
            print("Parametro erroneo")
    def opcion3(self,GM,GP,GE):
        if type(GM)==GMariculas and type(GP)==GProgramas and type(GE) ==GEmpleado:
            pass
        else:
            print("Parametro erroneo")
    def opcion4(self,GM,GP,GE):
        if type(GM)==GMariculas and type(GP)==GProgramas and type(GE) ==GEmpleado:
            print("\nMatriculas")
            GM.mostrar()
            print("\nEmpleados")
            GE.mostrar()
            print("\nProgramas de capacitacion")
            GP.mostrar()
        else:
            print("Parametro erroneo")