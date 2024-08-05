from Lista import lista
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5
        }
    def opcion(self,op,lis):
        if type(lis)==lista:
            fun=self.__switcher.get(op,lambda:print("Opcion no valida"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
                fun(lis)
            else:
                fun()
        else:
            print("Dato invalido")
    def opcion1(self,lis):
        try:
            lon=lis.long()
            va=int(input("La lista posee una longitud de {}\nPor favor introdusca un valor entre 0 y {}\n".format(lon,lon-1)))
            lis.buscar(va)
        except IndexError:
            print("Indice fuera de rango")
        except ValueError:
            print("se esperaba un numero")
    def opcion2(self,lis):
        año=input("Ingrese el año de fabricacion\n")
        lis.conteo(año)
    def opcion3(self,lis):
        try:
            cap=int(input("Capacidad de carga-->"))
            lis.cap(cap)
        except ValueError:
            print("Se esperaba un numero")
    def opcion4(self,lis):
        lis.mostrarTotal()
    def opcion5(self,lis):
        for dato in lis:
            dato.mostrar()