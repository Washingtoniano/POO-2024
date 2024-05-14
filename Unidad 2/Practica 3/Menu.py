from GestordeVenta import GestorVentas
import random
class menu():
    __switcher=None
    def __init__(self) :
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.mostrar

                        }
    def opcion(self,op,GV):
        fun=op(self.__switcher.get(op,lambda:print("Dato erroneo")))
        if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
            fun(GV)
        else:
            fun()
    def opcion1(self,GV):
        if type(GV)==GestorVentas:
            print("Ingrese los suiguientes datos\n")
            s=int(input("N° de sucursal\n"))
            d=int(input("Dia de la semana\n"))
            m=float(input("Monto a registrar\n$"))
            GV.acumular(d,s,m)

    def opcion2(self,GV):
        if type(GV)==GestorVentas:
            s=int(input("N° de sucursal a facturar\n"))
            print("La sucursal {} facturo en total:{}".format(s,GV.calcular(s)))
    

    def opcion3(self,GV):
        if type(GV)==GestorVentas:
            d=int(input("Ingrese el dia de la semana\n"))
            b=GV.maximo(d)
            if(b>0):
                print("La sucursal que mas facturo fue la numero {}".format(b))
            else:
                print("No se encontro la sucursal numero {}\n".format(d))
    def opcion4(self,GV):
        if type(GV)==GestorVentas:
                b=GV.minimo()
                if(b>0):
                    print("La sucursal que menos facturo es la numero {}\n".format(b))
                else:
                    print("Error\n")
    def opcion5(self,GV):
        if type(GV)==GestorVentas:
            GV.total()


    def mostrar(self,GV):
        if type(GV)==GestorVentas:
            GV.mostrar()
    
    def test(self,GV):
        for i in range (5):
            for j in range (7):
                d=random.randrange(1,7,1)
                s=random.randrange(1,5,1)
                m=random.randrange(20,27000,6)
                GV.acumular(d,s,m)
        self.mostrar(GV)
        #self.manejador()
            #self.manejador()
            #self.manejador()



