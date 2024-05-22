from GestorClientes import GestorC
from GestorMovimientos import GestorM
from menu import menu
if __name__ == '__main__':
    GC=GestorC()
    GM=GestorM()
    GM.leer()
    GC.leer()
    unmenu=menu()
    print("Bienvenido")
    op=input("Seleccione una opcion\n 1-Actualizar saldo de un cliente\n 2-Informar si un cliente tuvo o no movimientos\n 3-Ordenar el gestor\n 4-Mostrar Datos\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,GM,GC)
        op=input("Seleccione una opcion\n 1-Actualizar saldo de un cliente\n 2-Informar si un cliente tuvo o no movimientos\n 3-Ordenar el gestor\n 4-Mostrar Datos\n 0-Salir\n")
    print("Adios")