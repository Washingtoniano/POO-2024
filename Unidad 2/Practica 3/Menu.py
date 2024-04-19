from GestordeVenta import GestorVentas
import random
class menu():
    __gestor=GestorVentas
    def __init__(self) :
        self.__gestor=GestorVentas()
    def mostrar(self):
        self.__gestor.mostrar()
    def manejador(self):
        cod=input("Seleccione la opcion deseada\n a-Cargar Monto\n b-Calcular el total de facturación\n c-Buscar sucursal con mayor facturacíon por dia\n d-Sucursal con menor facturacion durante toda la semana\n e-Total facturado por todas las sucursales en la semana\n Otro valor para finalizar\n")
        while(cod<='e' and cod>='a'):
            if cod=='a':
                print("Ingrese los suiguientes datos\n")
                s=int(input("N° de sucursal\n"))
                d=int(input("Dia de la semana\n"))
                m=float(input("Monto a registrar\n$"))
                self.__gestor.acumular(d,s,m)
            elif cod=='b':
                s=int(input("N° de sucursal a facturar\n"))
                print("La sucursal {} facturo en total:{}".format(s,self.__gestor.calcular(s)))
            elif cod=='c':
                d=int(input("Ingrese el dia de la semana\n"))
                b=self.__gestor.maximo(d)
                if(b>0):
                    print("La sucursal que mas facturo fue la numero {}".format(b))
                else:
                    print("No se encontro la sucursal numero {}\n".format(d))
            elif(cod=="d"):
                b=self.__gestor.minimo()
                if(b>0):
                    print("La sucursal que menos facturo es la numero {}\n".format(b))
                else:
                    print("Error\n")
            elif(cod=="e"):
                self.__gestor.total()
            cod=input("Seleccione la opcion deseada\n a-Cargar Monto\n b-Calcular el total de facturación\n c-Buscar sucursal con mayor facturacíon por dia\n d-Sucursal con menor facturacion durante toda la semana\n e-Total facturado por todas las sucursales en la semana\n Otro valor para finalizar\n")

    def test(self):
        ungestor=self.__gestor
        for i in range (5):
            for j in range (7):
                d=random.randrange(1,7,1)
                s=random.randrange(1,5,1)
                m=random.randrange(20,27000,6)
                ungestor.acumular(d,s,m)
        self.mostrar()
        self.manejador()
            #self.manejador()
            #self.manejador()



