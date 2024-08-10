from lista import lista
class menu():
    __switcher:None
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
            fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
                fun(lis)
            else:
                fun()
        else:
            print("Error de tipo\n")
    def opcion1(self,lis):
        try:
            top=lis.getTope()
            va=int(input("La lista posee {} elementos. Por favor ingrese un valor entre 0 y {}\n".format (top,top-1)))
            lis.buscar(va)
        except ValueError:
            print("Se esperaba un numero")
        except IndexError:
            print("Indice fuera de rango")
    def opcion2(self,lis):
        cober=input("Ingrese el tipo de cobertura a buscar\n")
        lis.BCober(cober.upper())
    def opcion3(self,lis):
        cant=int(input("Ingrese la cantidad de canales internacionales\n"))
        lis.BCanales(cant)
    def opcion4(self,lis):
        lis.Mostrar()
    def opcion5(self,lis):
        lis.mostrar()