from menu import menu
from lista import lista
if __name__ =="__main__":
    unalista=lista()
    unalista.leer()
    unmenu=menu()
    print("Bienvenido")
    op=input("Ingrese la opcion deseada\n 1-Obtener tipo den una posicion\n 2-Buscar compañias por cobertura\n 3-Buscar compañias segun la cantidad de canales nacionales\n 4-Mostrar Formato\n 5-Mostrar Datos\n 0-Salir\n")
    while op!= '0':
        unmenu.opcion(op,unalista)
        op=input("Ingrese la opcion deseada\n 1-Obtener tipo den una posicion\n 2-Buscar compañias por cobertura\n 3-Buscar compañias segun la cantidad de canales nacionales\n 4-Mostrar Formato\n 5-Mostrar Datos\n 0-Salir\n")
    print("adios")

