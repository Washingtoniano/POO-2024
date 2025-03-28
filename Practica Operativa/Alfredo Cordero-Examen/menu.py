from lista import lista

class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={
                        '1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3,
                        '4':self.opcion4,
                        '5':self.opcion5,
                        '6':self.opcion6
        }
    
    def opcion(self,op,lis):
        if type(lis)==lista:
            fun=self.__switcher.get(op,lambda:print("opcion invalida"))
            if op =='1' or op =='2' or op =='3' or op =='4' or op =='5' or op=='6':
                fun(lis)
            else:
                fun()
        else:
            print("Error de parametro")
    
    def opcion1(self,lis):
        to=lis.TotalNeumonia()
        print("La cantidad total de pacientes con neumnia es de {}".format(to))
    
    def opcion2(self,lis):
        to=lis.TotalAmbulatorio()
        print("La cantidad total de pacientes ambulatorios es de {}".format(to))
    
    def opcion3(self,lis): 
        print("La clinica cobra a todos sus clientes un importe de ${}".format(lis.getValorcon()))
    
    def opcion4(self,lis):
        top=lis.getTope()
        try:
            val=int(input("La lista posse {} elementos\nIngrese un valor del 0 a {}-->".format(top,top-1)))
            lis.posicion(val)
        except ValueError:
            print("Se esperaba un numero")
        except IndexError:
            print("Indice fuera de rango")

    
    def opcion5(self,lis):
        try:
            nuevo=float(input("Ingrese el nuevo importe general"))
            lis.setValorcon(nuevo)
        except ValueError:
            print("Se esperaba un numero")

    
    def opcion6(self,lis):
        lis.mostrar()