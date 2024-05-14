from menu import menu
from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones

def manejador(GT,GC):
        GC.inicializar()
        GT.inicializar()
        v=int(input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CVU\n5-Almacenar datos\n6-Mostrar\n0-Salir\n"))
        band=False
        while v >0 and band!=True:
            if v==1:
                DNI=int(input("Ingrese el numero de DNI"))
                CVU=GC.buscarCVU(DNI)
                if CVU==False:
                    print("No se encontro el CVU")
                else:
                    saldo=GT.calcular(CVU[1],CVU[2])
                    GC.setsaldo(CVU[0],saldo)
                    print(GC.mostrarI(CVU[0]))
            elif v==2:
                por=float(input("Ingrese el nuevo porcentaje (%)\n"))
                GC.NPorcentaje(por)
            elif v==3:
                GC.actualizar()
            elif v==4:
                CVU=input("Ingrese el CVU a buscar")
                saldo=GC.buscarSaldo(CVU)
                
                if saldo!=False:
                    print("El saldo es{}".format(saldo[1]))
                    
                    GC.setsaldo(saldo[0],GT.calcular(CVU,saldo[1]))
                    GC.mostrarI(saldo[0])
                else:
                    print("ERROR")
            elif v==5:
                GC.escribir()

            elif v==6:
                GC.mostrar()
                GT.mostrar()
            else:
                print("Dato erroneo")
            v=int(input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CVU\n5-Almacenar datos\n6-Mostrar\n0-Salir\n"))



if __name__=='__main__':
    print("Bienvenido")
    GT=GestorTransacciones()
    GT.inicializar()
    GC=GestorCuentas(10)
    GC.inicializar()
    unmenu=menu()
    op=input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CVU\n5-Almacenar datos\n6-Mostrar\n0-Salir\n")
    while op!='0':
        unmenu.opcion(op,GC,GT)
        op=input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CVU\n5-Almacenar datos\n6-Mostrar\n0-Salir\n")
    #manejador(GT,GC)
    print ("Adios")