from gestorclientes import gestorC
from gestormovimiento import gestorM
class menu():
    __GestorC=gestorC()
    __GestorM=gestorM(20)
    def __init__(self) -> None:
        self.__GestorC=gestorC()
        self.__GestorM=gestorM(25)
    def manejador(self):
        self.inicializar()
        v=int(input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n"))
        while v>0:
            if v==1:
                DNI=int(input("ingrese el DNI del cliente a buscar\n"))
                Dni=self.__GestorC.buscrDNI(DNI)
                if Dni==False:
                    print("No se encontro el dni\n")
                else:
                    I=Dni[0]
                    Num=Dni[1]
                    cant=self.__GestorM.obtenerTeI(Num)
                    
                    print("\nCliente:{:10}Numero de Tarjeta:{:10}".format(self.__GestorC.getNombreyApellido(Dni[0]),self.__GestorC.getN(Dni[0])))
                    print("saldo anterior:{:10}\n".format(self.__GestorC.getsaldo(I)))
                    print("Movimientos:")
                    print("Fecha:   Descrippcion:   Importe:   Tipo:    ")
                    cant=self.__GestorM.obtenerTeI(Num)


                    self.__GestorC.actualizar(I,cant)
                    print("saldo Actualizado={:10}\n".format(self.__GestorC.getsaldo(I)))
            elif v==2:
                numero=int(input("Ingrese el numero de tarjeta\n"))
                band=self.__GestorM.buscarM(numero)
                if band==False:
                    bandera =self.__GestorC.buscarN()
                    if bandera ==False:
                        print("no se encontro el usuario\n")
                    else:
                        print (bandera)
                else:
                    print("El usuario realizo movimientos")

            elif v==3:
                self.__GestorM.ordenar()
            elif v==4:
                print("Clientes:\n")
                self.__GestorC.mostrar()
                print("Movimientos:\n")
                self.__GestorM.mostrar()
            else:
                print("Dato erroneo\n")
            v=int(input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n"))
    
    def inicializar(self):
        self.__GestorM.leer()
        self.__GestorC.leer()