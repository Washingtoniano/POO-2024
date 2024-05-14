from GestorMotos import GestorM
from GestorPedidos import GestorP
class menu():
    __switcher=None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.opcion6,
                         '7':self.opcion7,
                         '8':self.opcion8

                        }
    def opcion(self,op,GM,GP):
        fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
        if op =='1'or op =='2'or op =='3'or op =='4'or op =='5'or op =='6'or op =='7'or op =='8':
            fun(GM,GP)
        else:
            fun()
    def opcion1(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
            GM.inicializar()
        else:
            print("Parametro erroneo")
    def opcion2(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
            GP.inicializar()
        else:
            print("Parametro erroneo")
    def opcion3(self,GM,GP):
        pat=input("Ingrese la patente del pedido\n")
        Pan=GM.Buscar(pat)
        if Pan!=0:
            while Pan!=True:
                print("No se encontro la patente\n")
                pat=input("Ingrese la patente del pedido\n")
                Pan=GM.Buscar(pat)
            GP.agregar(pat)
        else:
            print("La lista esta vacia\n")
    def opcion4(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
                print("Ingrese los siguientes datos")
                pa=input("\nPatente: ")
                id=int(input("\nId: "))
                Tr=input("\nTiempo real de entrega: ")
                GP.modificar(pa,id,Tr)
        else:
            print("Parametro erroneo")
    def opcion5(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
            pa=input("Ingrese patente de moto\n")
            dato=(GM.mostrarCon(pa)) #Busca la patente en el gestor de motos
            if type(dato)!=int and type(dato)!=str:
                print("No se encontro la patente\n")
            else:
                #print("{}".format(dato))
                #Compara la patente encontrada en el gestor de motos y devuelve datos
                print("Posee un promedio de {} en tiempo real\n".format(GP.promedio(dato)))
        else:
            print("Parametro erroneo")
    def opcion6(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
            GP.Ordenar()
            p=GP.regresa_lista()
            m=GM.regresa_lista()
            for i in range (len(m)):
                print("\nPatente de Moto:{}\nConductor:{}".format(GM.regresapatente(i),GM.regresaconductor(i)))
                print("Indentificador de Pedido   Tiempo Estimado   Tiempo real   Precio")
                for l in range (len(p)):
                    cant=0
                    acum=0.0
                    band=False
                    if (GM.regresapatente(i)==GP.getpatente(l)):
                        band=True
                        print("     {}                        {}                {}        {}".format(GP.getID(l),GP.getTe(l),GP.getTr(l),GP.getprecio(l)))
                        #5,24,16,8 espacio
                        cant+=1
                        acum+=GP.getprecio(l)
                    if band==True:
                        print("\nComision:${}(20 del total)\n".format(acum*20/100))
        else:
            print("Parametro erroneo")

    def opcion7(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
            print("Datos de Pedidos\n")
            GP.mostrar()
            print("Datos de Motos\n")
            GM.mostrar()
        else:
            print("Parametro erroneo")
    def opcion8(self,GM,GP):
        if type(GM)==GestorM and type(GP)==GestorP:
            GP.Ordenar()

        else:
            print("Parametro erroneo")
    
    
   