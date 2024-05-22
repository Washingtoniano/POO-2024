from GestorAlquiler import gestorA
from GestorCancha import gestorC
from Menu import menu
if __name__ =='__main__':
    GA=gestorA()
    GC=gestorC()
    GC.leer()
    GA.leer()
    unmenu=menu()
    print("Bienvenido")
    op=input("Sleccione la opcion que dese\n 1-Listad\n 2-cantidad total alquilada\n 3-Mostrar\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,GC,GA)
        op=input("Sleccione la opcion que dese\n 1-Listad\n 2-cantidad total alquilada\n 3-Mostrar\n 0-Salir\n")
    print ("Adios")
