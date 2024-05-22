from gestorCabañas import gestorC
from gestorReserva import gestorR
from menu import menu
if __name__ =='__main__':
    GC=gestorC()
    GR=gestorR()
    GR.leer()
    GC.leer()
    unmenu=menu()
    print("Bienvenido")
    op=input("Seleccione la opcion deseada\n 1-Buscar cabaña\n 2-Mostrar listado\n 3-Mostrar Datos\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,GC,GR)
        op=input("Seleccione la opcion deseada\n 1-Buscar cabaña\n 2-Mostrar listado\n 3-Mostrar Datos\n 0-Salir\n")

    print('Adios')
