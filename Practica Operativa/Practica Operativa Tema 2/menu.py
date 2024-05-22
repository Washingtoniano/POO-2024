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
            if numero==-1:
                print("No se encontro el cliente\n")
            else:
                objeto=GC.darobjeto(numero)
                print("\nCliente:{:20}Numero de cuenta:{}\nSaldo anterior:${}".format(objeto.getNomb()+objeto.getApelli(),objeto.getNum(),objeto.getSaldo()))
                print("Movimientos")
                print(f'{"Fecha":20}{"Descripcion":20}{"Importe":20}{"Tipo":20}')
                acum=GM.actualizar(objeto.getNum())
                objeto.setSaldo(acum)
                print("Saldo Actualizado:${}\n".format(objeto.getSaldo()))

        else:
            print("Parametro no valido")
    
    def opcion2(self,GM,GC):

        if type(GM)==GestorM and type(GC)==GestorC:
            dni=int(input("Ingrese el numero de DNI"))
            numero=GC.BC(dni)
            if numero==-1:
                print("No se encontro el dni")
            else:
                objeto=GC.darobjeto(numero)
                bandera=GM.BC(objeto.getNum())
                if bandera!=-1:
                    print("El cliente {} si realizo movimientos".format (objeto.getNomb()+objeto.getApelli()))
                else:
                    print("El cliente {} no realizo movimientos".format (objeto.getNomb()+objeto.getApelli()))

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
