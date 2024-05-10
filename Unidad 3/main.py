from Gestor import gestor
from Menu import menu

if __name__ =='__main__':
    ungestor=gestor()
    #ungestor.leer()
    unmenu=menu()
    unmenu.leer(ungestor)
    print("Bienvenido\n")
    op=input("Ingrese la opcion que desea\n1-Mostrar propietarios de un edificio\n2-\n3-\n4-\n5-\n0-Salir\n")
    while op!='0':
        unmenu.opcion(op,ungestor)
        op=input("Ingrese la opcion que desea\n1-Mostrar propietarios de un edificio\n2-\n3-\n4-\n5-\n0-Salir\n")

    print("adios")
    