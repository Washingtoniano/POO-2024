from lista import lista
from ObjectENcoder import ObjectEncoder
class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,

        }
    def opcion(self,op,lis,json):
        if type(lis)==lista and type(json)==ObjectEncoder: 
            fun =self.__switcher.get(op,lambda:print("Dato erroneo"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7' or op=='8' or op=='9' or op=='10':
                fun(lis,json)
            else:
                fun()
        else:
            print("dato no valido")
    def opcion1(self):
        pass
    def inicializar(self,lis,json):
        if type(lis)==lista and type(json)==ObjectEncoder:
            diccionario=json.LeerArchivo("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 6\\Personal.json")
            lis=json.DecodificarArchivo(diccionario)