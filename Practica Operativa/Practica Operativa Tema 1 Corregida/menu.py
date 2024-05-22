from gestorclientes import gestorC
from gestormovimiento import gestorM
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         #'0':self.salir
                        }
    def opcion(self,op,GM,GC):
        fun=self.__switcher.get(op,lambda:print("Opcion no valida"))
        if op=='1' or op =='2' or op=='3' or op=='4' or op=='0':
            fun(GM,GC)
        else:
            fun()

    def opcion1(self,GestorM,GestorC):
        if type(GestorM)==gestorM and type(GestorC)==gestorC:
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
                print("saldo anterior:{:10}\n".format(objeto.getsaldo()))
                print("Movimientos:")
                print("Fecha:   Descrippcion:   Importe:   Tipo:    ")
                cant=GestorM.obtenerTeI(objeto.getN())

                
                objeto.putsaldo(cant)
                print("saldo Actualizado={:10}\n".format(objeto.getsaldo()))
        else:
            print("Error de parametro")
    def opcion2(self,GestorM,GestorC):
        if type(GestorM)==gestorM and type(GestorC)==gestorC:
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
        else:
            print("Error de parametro")
    def opcion4(self,GestorM,GestorC):
        if type(GestorM)==gestorM and type(GestorC)==gestorC:
            print("Clientes:\n")
            GestorC.mostrar()
            print("Movimientos:\n")
            GestorM.mostrar()
        else:
            print("Error de parametro")
    def opcion3(self,GestorM,GestorC):
        if type(GestorM)==gestorM and type(GestorC)==gestorC:
            GestorM.ordenar()
        else:
            print("Error de parametro")
    #def salir(self):
      
        #print("Adios")
   



    '''def manejador(self):
        self.inicializar()
        v=int(input("Seleccione la opcion que desea\n 1-Leer DNI y actualizar saldo de un cliente\n 2-Leer numero de tarjeta\n 3-Ordenar los movimientos\n 4-Mostrar datos\n 0-Salir\n"))
        while v>0:
            if v==1:
                DNI=int(input("ingrese el DNI del cliente a buscar\n"))
                Dni=GestorC.buscrDNI(DNI)
                if Dni==False:
                    print("No se encontro el dni\n")
                else:
                    i=GestorC.buscarindice(Dni)
                    I=i
                    Num=Dni
                    cant=GestorM.obtenerTeI(Num)
                    
                    print("\nCliente:{:10}Numero de Tarjeta:{:10}".format(GestorC.getNombreyApellido(I),GestorC.getN(I)))
                    print("saldo anterior:{:10}\n".format(GestorC.getsaldo(I)))
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
    '''
    def inicializar(self,GestorM,GestorC):
        if type(GestorM)==gestorM and type(GestorC)==gestorC:
            GestorM.leer()
            GestorC.leer()
        else:
            print("Error de parametro")