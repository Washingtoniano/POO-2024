from lista import lista
from menu import menu
if __name__=="__main__":
    unalista=lista()
    unmenu=menu()
    unalista.leer()
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Cant de pacientes con neumonia\n 2-Cant de Pacientes ambulatorios\n 3-Monto cobrado a todos los pacientes\n 4-Obtener tipo segun una posicion\n 5-cambiar importe general\n 6-Mostrar datos guardados\n 0-Salir\n")
    while op!= '0':
        unmenu.opcion(op,unalista)
        op=input("Ingrese la opcion que desea\n 1-Cant de pacientes con neumonia\n 2-Cant de Pacientes ambulatorios\n 3-Monto cobrado a todos los pacientes\n 4-Obtener tipo segun una posicion\n 5-cambiar importe general\n 6-Mostrar datos guardados\n 0-Salir\n")
    print("Adios")

