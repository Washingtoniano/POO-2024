from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones
class menu():
    __GC=GestorCuentas(30)
    __GT=GestorTransacciones()
    def __init__(self):
        self.__GC=GestorCuentas(30)
        self.__GT=GestorTransacciones()
    def manejador(self):
        self.__GC.inicializar()
        self.__GT.inicializar()
        v=int(input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CSV\n5-Almacenar datos\n6-Mostrar\n0-Salir\n"))
        band=False
        while v >0 and band!=True:
            if v==1:
                pass
            elif v==2:
                por=float(input("Ingrese el nuevo porcentaje (%)\n"))
                self.__GC.NPorcentaje(por)
            elif v==3:
                pass
            elif v==4:
                pass
            elif v==5:
                pass

            elif v==6:
                self.__GC.mostrar()
                self.__GT.mostrar()
            else:
                print("Dato erroneo")
            v=int(input("Seleccione la opcion que desea\n1-Leer DNI del cliente\n2-Leer nuevo porcentaje\n3-Actualizar saldo\n4-Leer CSV\n5-Almacenar datos\n6-Mostrar\n0-Salir\n"))
