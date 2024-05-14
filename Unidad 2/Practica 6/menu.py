from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones
class menu():
    __switcher=None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3,
                        '4':self.opcion4,
                        '5':self.opcion5,
                        '6':self.opcion6,

                        }
        
    def opcion(self,op,GC,GT):
        fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
        if op =='1' or op =='2' or op =='3' or op =='4' or op =='5' or op =='6':
            fun(GC,GT)
        else:
            fun()

    def opcion1(self,GC,GT):
        if type(GC)==GestorCuentas and type(GT)==GestorTransacciones:
            DNI=int(input("Ingrese el numero de DNI"))
            CVU=GC.buscarCVU(DNI)
            if CVU==False:
                print("No se encontro el CVU")
            else:
                saldo=GT.calcular(CVU[1],CVU[2])
                GC.setsaldo(CVU[0],saldo)
                print(GC.mostrarI(CVU[0]))
        else:
            print("Parametro erroneo")
    def opcion2(self,GC,GT):
        if type(GC)==GestorCuentas and type(GT)==GestorTransacciones:
            por=float(input("Ingrese el nuevo porcentaje (%)\n"))
            GC.NPorcentaje(por)
        else:
            print("Parametro erroneo")
    def opcion3(self,GC,GT):
        if type(GC)==GestorCuentas and type(GT)==GestorTransacciones:
            pass
        else:
            print("Parametro erroneo")
    def opcion4(self,GC,GT):
        if type(GC)==GestorCuentas and type(GT)==GestorTransacciones:
            CVU=input("Ingrese el CVU a buscar")
            saldo=GC.buscarSaldo(CVU)
                
            if saldo!=False:
                print("El saldo es{}".format(saldo[1]))
                    
                GC.setsaldo(saldo[0],GT.calcular(CVU,saldo[1]))
                GC.mostrarI(saldo[0])
            else:
                print("ERROR")
        else:
            print("Parametro erroneo")
    def opcion5(self,GC,GT):
        if type(GC)==GestorCuentas and type(GT)==GestorTransacciones:
            GC.escribir()
        else:
            print("Parametro erroneo")
    def opcion6(self,GC,GT):
        if type(GC)==GestorCuentas and type(GT)==GestorTransacciones:
            GC.mostrar()
            GT.mostrar()
        else:
            print("Parametro erroneo")
    