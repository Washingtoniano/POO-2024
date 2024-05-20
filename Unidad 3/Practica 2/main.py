from Menu import menu
from GestorLadrillos import GestorLadrillo
from GestorReflactario import GestorReflactario
if __name__ =='__main__':
    GR=GestorReflactario()
    GL=GestorLadrillo()
    GR.leer()
    GL.leer(GR)

    unmenu=menu()
    print ("Bienvenido")
    v=input("Ingrese la opcion que desea\n 1-Buscar ID\n 2-Costo total de fabricacion\n 3-Mostrar Formato\n 4-Mostrar Datos\n 0-Salir\n")
    while v!='0':
        unmenu.opcion(v,GR,GL)
        v=input("Ingrese la opcion que desea\n 1-Buscar ID\n 2-Costo total de fabricacion\n 3-Mostrar Formato\n 4-Mostrar Datos\n 0-Salir\n")
    print("Adios")