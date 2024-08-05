from Menu import menu
from Lista import lista
if __name__ =="__main__":
    unmenu=menu()
    unalista=lista()
    unalista.leer()
    #unalista.mostrar()
    print("Bienvenido")
    op=input("Seleccione la opcion deseada\n 1-\n 2-\n 3-\n 4\n 5-Mostrar\n 0-salir\n")
    while op!='0':
        unmenu.opcion(op,unalista)
        op=input("Seleccione la opcion deseada\n 1-\n 2-\n 3-\n 4\n 5-Mostrar\n 0-salir\n")
    print("Adios")

