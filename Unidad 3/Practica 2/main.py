from Menu import menu
from GestorLadrillos import GestorLadrillo
from GestorReflactario import GestorReflactario
if __name__ =='__main__':
    GR=GestorReflactario()
    GL=GestorLadrillo()
    unmenu=menu()
    print ("Bienvenido")
    v=input("Ingrese la opcion que desea\n 1-\n 2-\n 3-\n 4-\n 0-Salir\n")
    while v!='0':
        unmenu.opcion(v,GR,GL)
        v=input("Ingrese la opcion que desea\n 1-\n 2-\n 3-\n 4-\n 0-Salir\n")
    print("Adios")