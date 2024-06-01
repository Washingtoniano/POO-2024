from lista import lista
from LibroImpreso import LibroImpreso
from AudioLibro import AudioLibro
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.opcion6

        }
    def opcion(self,op,lis):
        if type (lis)==lista:
            fun=self.__switcher.get(op,lambda:print("dato erroneo"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='6' or op=='5':
                fun(lis)
            else:
                fun()
        else: 
            print("parametro erroneo")
    def opcion2(self,lis):
        long=lis.longitud()
        posicion=int(input("la lista posee una longitud de {} ingrese un numero de 0 a {}->".format(long,long-1)))
        print(lis.MostrarElemento(posicion))
    def opcion1(self,lis):
        libro= lis.nbtenerDatos()
        lis.agregar(libro)



    def opcion3(self,lis):
        lis.tipos()
    def opcion4(self,lis):
        lis.mostrar()
    def opcion5(self,lis):
        try:
            libro=lis.obtenerDatos()
            long=lis.longitud()
            posicion=int(input("la lista posee una longitud de {} ingrese un numero de 0 a {}->".format(long,long-1)))

            lis.Insertarelemento(libro,posicion)
        except ValueError:
            print("Se esperaba un numero")
    def opcion6(self,lis):
        nombre=(input("Ingrese el nombre del libro a elminar\n"))
        lis.ElminarELemento(nombre)
