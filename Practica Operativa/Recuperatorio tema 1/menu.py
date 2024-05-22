from gestorCabañas import gestorC
from gestorReserva import gestorR
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3

        }

    def opcion(self,op,GC,GR):
        fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
        if op =='1' or op=='2' or op=='3':
            fun(GC,GR)
        else:
            fun()
     
    def opcion1(self,GC,GR):
        if type(GC)==gestorC and type(GR)==gestorR:
            cant=int(input("Ingrese la cantidad de huspedes"))
            GC.comprobar(cant,GR)
        else:
            print("parametro erroneo")
    
    def opcion2(self,GC,GR):
        if type(GC)==gestorC and type(GR)==gestorR:
            fecha=input("Ingrese la fecha que desea\n")
            GR.mostrarReserva(fecha,GC)
        else:
            print("parametro erroneo")
    def opcion3(self,GC,GR):
        if type(GC)==gestorC and type(GR)==gestorR:
            GC.mostrar()
            GR.mostrar()
        else:
            print("parametro erroneo")
    