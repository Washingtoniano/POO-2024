from GestorAlquiler import gestorA
from GestorCancha import gestorC
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
        }
    def opcion(self,op,GC,GA):
        if type(GA)==gestorA and type(GC)==gestorC:
            fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
            if op=='1' or op=='2' or op=='3':
                
                fun(GC,GA)
            else:
                fun()
        else:
            print("parametro no valido")
    def opcion1(self,GC,GA):
       
        GA.mostrarFormato(GC)

    def opcion2(self,GC,GA):
     
            id=(input("Ingrese el id de una cancha"))
            bandera=GC.buscarID(id)
            if bandera==True:
                total=GA.totalCancha(id)
                print("La cancha {} se alquilo un total de {} minutos".format(id,total))
            else:
                print("No se encontro la cancha")
       
    def opcion3(self,GC,GA):
     
            GC.mostrar()
            GA.mostrar()
     