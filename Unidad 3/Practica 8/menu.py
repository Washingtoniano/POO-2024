from lista import lista
from ObjectENcoder import ObjectEncoder
from ManejadorAutoridad import Manejador_autoridades
from ManejadorAutoridad import *
class menu():
    __switcher:None
    __autoridades:Manejador_autoridades
    
    def __init__(self) -> None:
        self.__autoridades=Manejador_autoridades()
        self.__switcher={
                        '1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3,
                        '4':self.opcion4,
                        '5':self.opcion5,
                        '6':self.opcion6,
                        '7':self.opcion7,
                        '8':self.opcion8,
                        '9':self.opcion9,
                        '10':self.opcion10,
                        "11":self.opcion11

        }
    def opcion(self,op,lis,json):
        if type(lis)==lista and type(json)==ObjectEncoder: 
            fun =self.__switcher.get(op,lambda:print("Dato erroneo"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7' or op=='8' or op=='9' or op =='10' or op=='11' :
                fun(lis,json)
            else:
                fun()
        else:
            print("dato no valido")
    def opcion2(self,lis,json):
        dato=lis.solicitar()
        lis.AgregarElemento(dato)

    def opcion1(self,lis,json):
        try:
            long=lis.len()
            pos=int(input("La lista tiene {} elementos\nIngrese un valor de 0 a {}\n".format(long,long-1)))
            lis.insertar(pos)
        except ValueError:
            print("Se esperaba un numero")
    def opcion3(self,lis,json):
        try:
            long=lis.len()
            pos=int(input("La lista tiene {} elementos\nIngrese un valor de 0 a {}\n".format(long,long-1)))
            lis.MostrarElemento(pos)
        except ValueError:
            print("Se esperaba un numero")

    def opcion4(self,lis,json):
        p=input("Ingrese el nombre de una carrera\n")
        lis.MostrarDI(p)
    def opcion5(self,lis,json):
        area=input("Ingrese un area de investigacion\n")
        lis.MostrarArea(area)

    def opcion6(self,lis,json):
        lis.ordenar()
        
        
        
    def opcion7(self,lis,json):
        categoria=input("Ingrese la categoria del investigador\n")
        lis.MostrarCategoria(categoria)
        


    def inicializar(self,lis,json):
        if type(lis)==lista and type(json)==ObjectEncoder:
            diccionario=json.LeerArchivo("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 7\\Personal.json")
            lis=json.DecodificarArchivo(diccionario)
    def opcion8(self,lis,json):
        d=lis.tojson()
        json.GuardarArchivo(d,"C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 7\\NuevoPersonal.json")

    def opcion9(self,lis,json):
        lis.mostrar()
    def opcion10(self,lis,json):
        self.__autoridades.getLista(lis)

        user=input("Ingrese el id del usuario\n")
        if user=='uTesoreso':
            contraseña=input("Ingrese la contraseña\n")
            if contraseña=='ag@74ck':
                Tesorero(self.__autoridades)
            else:
                print("Contraseña invalida")
        else:
            print("Usuario invalido")
        
    def opcion11(self,lis,json):
        user=input("Ingrese el id del usuario\n")
        if user=='uDirector':
            contraseña=input("Ingrese la contraseña\n")
            if contraseña=='ufC77#!1 ':
                Director(self.__autoridades)
            else:
                print("Contraseña invalida")
        else:
            print("Usuario invalido")
        

