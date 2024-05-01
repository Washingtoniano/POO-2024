from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones
class menu():
    __GC=GestorCuentas(10)
    __GT=GestorTransacciones()
    def __init__(self):
        self.__GC=GestorCuentas(10)
        self.__GT=GestorTransacciones()
    def manejador(self):
        self.__GC.inicializar()
        self.__GT.inicializar()
        v=int(input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CVU\n5-Almacenar datos\n6-Mostrar\n0-Salir\n"))
        band=False
        while v >0 and band!=True:
            if v==1:
                DNI=int(input("Ingrese el numero de DNI"))
                CVU=self.__GC.buscarCVU(DNI)
                if CVU==False:
                    print("No se encontro el CVU")
                else:
                    saldo=self.__GT.calcular(CVU[1],CVU[2])
                    self.__GC.setsaldo(CVU[0],saldo)
                    print(self.__GC.mostrarI(CVU[0]))
            elif v==2:
                por=float(input("Ingrese el nuevo porcentaje (%)\n"))
                self.__GC.NPorcentaje(por)
            elif v==3:
                self.__GC.actualizar()
            elif v==4:
                CVU=input("Ingrese el CVU a buscar")
                saldo=self.__GC.buscarSaldo(CVU)
                
                if saldo!=False:
                    print("El saldo es{}".format(saldo[1]))
                    
                    self.__GC.setsaldo(saldo[0],self.__GT.calcular(CVU,saldo[1]))
                    self.__GC.mostrarI(saldo[0])
                else:
                    print("ERROR")
            elif v==5:
                self.__GC.escribir()

            elif v==6:
                self.__GC.mostrar()
                self.__GT.mostrar()
            else:
                print("Dato erroneo")
            v=int(input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CVU\n5-Almacenar datos\n6-Mostrar\n0-Salir\n"))
