from Menu import menu
from GestordeVenta import GestorVentas
import random
def mostrar(gestor):
    gestor.mostrar()
def manejador(gestor):
    gestor=GestorVentas()
    cod=input("Seleccione la opcion deseada\n a-Cargar Monto\n b-Calcular el total de facturación\n c-Buscar sucursal con mayor facturacíon por dia\n d-Sucursal con menor facturacion durante toda la semana\n e-Total facturado por todas las sucursales en la semana\n Otro valor para finalizar\n")
    while(cod<='e' and cod>='a'):
            if cod=='a':
                print("Ingrese los suiguientes datos\n")
                s=int(input("N° de sucursal\n"))
                d=int(input("Dia de la semana\n"))
                m=float(input("Monto a registrar\n$"))
                gestor.acumular(d,s,m)
            elif cod=='b':
                s=int(input("N° de sucursal a facturar\n"))
                print("La sucursal {} facturo en total:{}".format(s,gestor.calcular(s)))
            elif cod=='c':
                d=int(input("Ingrese el dia de la semana\n"))
                b=gestor.maximo(d)
                if(b>0):
                    print("La sucursal que mas facturo fue la numero {}".format(b))
                else:
                    print("No se encontro la sucursal numero {}\n".format(d))
            elif(cod=="d"):
                b=gestor.minimo()
                if(b>0):
                    print("La sucursal que menos facturo es la numero {}\n".format(b))
                else:
                    print("Error\n")
            elif(cod=="e"):
                gestor.total()
            cod=input("Seleccione la opcion deseada\n a-Cargar Monto\n b-Calcular el total de facturación\n c-Buscar sucursal con mayor facturacíon por dia\n d-Sucursal con menor facturacion durante toda la semana\n e-Total facturado por todas las sucursales en la semana\n Otro valor para finalizar\n")

def test(gestor):
        ungestor=gestor
        for i in range (5):
            for j in range (7):
                d=random.randrange(1,7,1)
                s=random.randrange(1,5,1)
                m=random.randrange(20,27000,6)
                ungestor.acumular(d,s,m)
        mostrar(ungestor)
        #manejador()
            #manejador()
            #manejador()




if __name__== '__main__':
    unmenu=menu()
    #test()
    gestor=GestorVentas()

    print("Bienvenido\n")
    b= int(input("Hay una función test con valores aleatorios disponible. ¿Desea ejecutarla?\n 1-SI     2-NO\n"))
    band=False
    while b!=2 and band==False:
        if b==1:
            test(gestor)
            print("Gracias por probar la función test\n")
            band=True
        else:
            print("Datos erroneo\n")
            b= int(input("Hay una función test con valores aleatorios disponible ¿Desea ejecutarla?\n 1-SI     2-NO\n"))

    if b==2:
        #unmenu.mostrar()
        manejador(gestor)
    print("Adios")
