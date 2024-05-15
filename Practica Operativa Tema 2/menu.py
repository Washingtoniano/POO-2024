from GestorClientes import GestorC
from GestorMovimientos import GestorM
class menu():
    __switcher=None
    def __init__(self) -> None:
        
        self.__switcher={'1':self.opcion1,
                    '2':self.opcion2,
                    '3':self.opcion3,
                    '4':self.opcion4

        }

    def opcion(self,op,GM,GC):
        fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
        if op=='1' or op=='2' or op=='3' or op== '4':
            fun(GM,GC)
        else:
            fun()
    def opcion1(self,GM,GC):

        if type(GM)==GestorM and type(GC)==GestorC:
            Dni=int(input("Ingrese el DNI del cliente\n"))
            numero=GC.BC(Dni)
            if numero==False:
                print("No se encontro el cliente\n")
            else:
                indice=GC.indice(Dni)
                print("Cliente:{:20}Numero de cuenta:{:20}\nSaldo anterior:{:20}".format(GC.getNombre(indice)+GC.getApellid(indice),GC.getNumero(indice),GC.getSaldo(indice)))
                print("Movimientos")
                print('Fecha      Descripcion      Importe     Tipo')
                acum=GM.actualizar(numero)
                GC.actualizar(acum,Dni)
                print("Saldo Actualizado:{}".format(GC.getSaldo(indice)))

        else:
            print("Parametro no valido")
    
    def opcion2(self,GM,GC):

        if type(GM)==GestorM and type(GC)==GestorC:
            dni=int(input("Ingrese el numero de DNI"))
            numero=GC.BC(dni)
            if numero==False:
                print("No se encontro el dni")
            else:
                bandera=GM.BC(numero)
                if bandera==False:
                    print("El cliente {} si realizao movimientos".format (GC.BC(dni,bandera)))

        else:
            print("Parametro no valido")
    def opcion3(self,GM,GC):

        if type(GM)==GestorM and type(GC)==GestorC:
            GM.ordenar()

        else:
            print("Parametro no valido")
    def opcion4(self,GM,GC):

        if type(GM)==GestorM and type(GC)==GestorC:

            GC.mostrar()
            GM.mostrar()

        else:
            print("Parametro no valido")
