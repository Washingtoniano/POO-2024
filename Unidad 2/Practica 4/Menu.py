from GestorMotos import GestorM
from GestorPedidos import GestorP
class menu():
    __Gm=GestorM()
    __Gp=GestorP()
    def __init__(self):
        self.__Gm=GestorM()
        self.__Gp=GestorP()
    def manejadorar(self):
        #Menu desplegable con las opciones
        v=int(input("1-Leer datos de moto\n2-Leer datos de Pedidos\n3-Cargar un nuevo pedido\n4-Modificar tiempo real de entrega\n5-Mostrar Tiempo promedio de entrega\n6-Generar un listado para cada moto\n7-Mostrar datos\n8-Ordenar lista\n0-Finalizar\n"))
        band=False
        while v>0 and band==False:
            if v==1:
                self.__Gm.inicializar()
                #self.__Gm.mostrar()
            elif v==2:
                self.__Gp.inicializar()
                #self.__Gp.mostrar()
            elif v==3:
                pat=input("Ingrese la patente del pedido\n")
                Pan=self.__Gm.Buscar(pat)
                if Pan!=0:
                    while Pan!=True:
                        print("No se encontro la patente\n")
                        pat=input("Ingrese la patente del pedido\n")
                        Pan=self.__Gm.Buscar(pat)
                    self.__Gp.agregar(pat)
                else:
                    print("La lista esta vacia\n")

            elif v==4:
                print("Ingrese los siguientes datos")
                pa=input("\nPatente: ")
                id=int(input("\nId: "))
                Tr=input("\nTiempo real de entrega: ")
                self.__Gp.modificar(pa,id,Tr)

            elif v==5:
                pa=input("Ingrese patente de moto\n")
                dato=(self.__Gm.mostrarCon(pa)) #Busca la patente en el gestor de motos
                if type(dato)!=int and type(dato)!=str:
                    print("No se encontro la patente\n")
                else:
                    #print("{}".format(dato))
                    #Compara la patente encontrada en el gestor de motos y devuelve datos
                    print("Posee un promedio de {} en tiempo real\n".format(self.__Gp.promedio(dato)))
            elif v==6:
                self.__Gp.Ordenar()
                p=self.__Gp.regresa_lista()
                m=self.__Gm.regresa_lista()
                for i in range (len(m)):
                    print("\nPatente de Moto:{}\nConductor:{}".format(self.__Gm.regresapatente(i),self.__Gm.regresaconductor(i)))
                    print("Indentificador de Pedido   Tiempo Estimado   Tiempo real   Precio")
                    for l in range (len(p)):
                        cant=0
                        acum=0.0
                        band=False
                        if (self.__Gm.regresapatente(i)==self.__Gp.getpatente(l)):
                            band=True
                            print("     {}                        {}                {}        {}".format(self.__Gp.getID(l),self.__Gp.getTe(l),self.__Gp.getTr(l),self.__Gp.getprecio(l)))
                            #5,24,16,8 espacio
                            cant+=1
                            acum+=self.__Gp.getprecio(l)
                        if band==True:
                            print("\nComision:${}(20 del total)\n".format(acum*20/100))
                
            elif v==7:
                print("Datos de Pedidos\n")
                self.__Gp.mostrar()
                print("Datos de Motos\n")
                self.__Gm.mostrar()
            elif v==8:
                self.__Gp.Ordenar()
            elif v==0:
                band=True
            else:
                print("Datos Erroneos\n")
            v=int(input("1-Leer datos de moto\n2-Leer datos de Pedidos\n3-Cargar un nuevo pedido\n4-Modificar tiempo real de entrega\n5-Mostrar Tiempo promedio de entrega\n6-Generar un listado para cada moto\n7-Mostrar datos\n8-Ordenar lista\n0-Finalizar\n"))

            