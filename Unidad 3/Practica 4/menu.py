from lista import lista
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,

        }
    def opcion(self,op,lis):
        if type (lis)==lista:
            fun=self.__switcher.get(op,lambda:print("dato erroneo"))
            if op=='1' or op=='2' or op=='3' or op=='4':
                fun(lis)
            else:
                fun()
        else: 
            print("parametro erroneo")
    def opcion1(self,lis):
        long=lis.longitud()
        posicion=int(input("la lista posee una longitud de {} ingrese un numero de 0 a {}".format(long,long-1)))
        print(lis.obtener(posicion))
    def opcion2(self,lis):
        pass
    def opcion3(self,lis):
        pass
    def opcion4(self,lis):
        lis.mostrar()
