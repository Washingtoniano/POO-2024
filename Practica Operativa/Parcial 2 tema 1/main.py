from manejador import manejador
from menu import menu
if __name__== '__main__':
    unmanejador=manejador()
    unmenu=menu()
    unmanejador.leer()
    print("BIENVENIDO")
    op= input("Ingrese la opcion que desea\n 1-Agregar productos\n 2-Tipo de elemento\n 3-Mostrar tipos\n 4-Mostrar datos compartidos\n 5-Mostrar datos\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,unmanejador)
        op= input("Ingrese la opcion que desea\n 1-Agregar productos\n 2-Tipo de elemento\n 3-Mostrar tipos\n 4-Mostrar datos compartidos\n 5-Mostrar datos\n 0-Salir\n")
    print("Adios")




