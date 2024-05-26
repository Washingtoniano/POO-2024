from gestorEmpleados import GEmpleado
from gestorMatriculas import GMariculas
from gestorProgramas import GProgramas
from menu import menu
if __name__ =='__main__':
    GE=GEmpleado()
    GP=GProgramas()
    GM=GMariculas()
    GE.leer()
    GP.leer()
    GM.leer()
    unmenu=menu()
    op=input("Ingrese la opcion que desea\n 1-Buscar empleado\n 2-Buscar Programa\n 3-Informar\n 4-Mostrar\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,GM,GP,GE)
        op=input("Ingrese la opcion que desea\n 1-Buscar empleado\n 2-Buscar Programa\n 3-Informar\n 4-Mostrar\n 0-Salir\n")
    print("Adios")
