from menu import menu
from Lista import lista
from objectoencoder import ObjectEncoder
if __name__ =='__main__':
    unmenu=menu()
    lis=lista()
    json=ObjectEncoder()
    unmenu.inicializar(lis,json)
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-\n 2-\n 3-\n 4-\n 5-\n 6-\n 7-\n 8\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,lis,json)
        op=input("Ingrese la opcion que desea\n 1-\n 2-\n 3-\n 4-\n 5-\n 6-\n 7-\n 8\n 0-Salir\n")

    print("Adios")    

    