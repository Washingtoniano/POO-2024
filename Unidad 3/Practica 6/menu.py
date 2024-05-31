from Lista import lista
from objectoencoder import ObjectEncoder
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.opcion6,
                         '7':self.opcion7,
                         '8':self.opcion8,


        }
    def opcion(self,op,lis,json):
        if type(lis)==lista:
            fun=self.__switcher.get(op,lambda:print("Dato no valido"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7' or op=='8':
                fun(lis,json)
            else:
                fun() 
        else:
            print("Error de parametross")
    def inicializar(self,lis,json):
        if type (lis)==lista and type (json)==ObjectEncoder:
            diccionario=json.leerJSONArchivo("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 6\\calefactores.json")
            listado=json.decodificarDIccionario(diccionario)
            print(lis)
            for i in range (len(listado)):
                lis.agregar(listado[i])
            self.opcion8(lis,json)
        else:
            print("Parametro erroneos")

    def opcion1(self,lis,json):
        pass
    def opcion2(self,lis,json):
        pass
    def opcion3(self,lis,json):
        pass
    def opcion4(self,lis,json):
        pass
    def opcion5(self,lis,json):
        pass
    def opcion6(self,lis,json):
        pass
    def opcion7(self,lis,json):
        pass
    def opcion8(self,lis,json):
        lis.mostrar()

