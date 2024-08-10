from Menu import menu
from Lista import lista
if __name__ =="__main__":
    unmenu=menu()
    unalista=lista()
    unalista.leer()
    #unalista.mostrar()
    print("Bienvenido")
    op=input("Seleccione la opcion deseada\n 1-Obtener tipo en una posicion\n 2-Cantidad de herramientas electricas fabricadas en un año\n 3-Maquinaria pesada cuya capacidad es menor a\n 4-Mostrar\n 5-Mostrar datos\n 0-salir\n")
    while op!='0':
        unmenu.opcion(op,unalista)
        op=input("Seleccione la opcion deseada\n 1-Obtener tipo en una posicion\n 2-Cantidad de herramientas electricas fabricadas en un año\n 3-Maquinaria pesada cuya capacidad es menor a\n 4-Mostrar\n 5-Mostrar datos\n 0-salir\n")
    print("Adios")

