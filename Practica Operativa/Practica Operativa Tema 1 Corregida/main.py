
from gestorclientes import gestorC
from gestormovimiento import gestorM
from menu import menu

def manejador():
    GestorC=gestorC()
    GestorM=gestorM(20)
    inicializar(GestorM,GestorC)
    v=int(input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n"))
    while v>0:
        if v==1:
            DNI=int(input("ingrese el DNI del cliente a buscar\n"))
            Dni=GestorC.buscrDNI(DNI)
            if Dni==-1:
                print("No se encontro el dni\n")
            else:
                objeto=GestorC.darobjeto(Dni)
                I=Dni
                Num=Dni
                cant=GestorM.obtenerTeI(Num)
                
                print("\nCliente:{:10}Numero de Tarjeta:{:10}".format(objeto.getNombreYApellido(),objeto.getN()))
                print("saldo anterior:{:10}\n".format(objeto.getSaldo()))
                print("Movimientos:")
                print("Fecha:   Descrippcion:   Importe:   Tipo:    ")
                cant=GestorM.obtenerTeI(Num)


                GestorC.actualizar(I,cant)
                print("saldo Actualizado={:10}\n".format(GestorC.getsaldo(I)))
        elif v==2:
            numero=int(input("Ingrese el numero de tarjeta\n"))
            band=GestorM.buscarM(numero)
            if band==False:
                bandera =GestorC.buscarN(numero)
                if bandera ==False:
                    print("no se encontro el usuario\n")
                else:
                    print (bandera)
            else:
                print("El usuario realizo movimientos")
        elif v==3:
            GestorM.ordenar()
        elif v==4:
            print("Clientes:\n")
            GestorC.mostrar()
            print("Movimientos:\n")
            GestorM.mostrar()
        else:
            print("Dato erroneo\n")
        v=int(input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n"))
    
def inicializar(GestorM,GestorC):
    GestorM.leer()
    GestorC.leer()
if __name__ =="__main__":
    print("Bienvenido")
    #manejador()
    print("adios")

    unmenu=menu()
    GM=gestorM(10)
    GC=gestorC()
    unmenu.inicializar(GM,GC)
    v=input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n")
    while v!='0':
        unmenu.opcion(v,GM,GC)
        v=input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n")
    print("Adios")

