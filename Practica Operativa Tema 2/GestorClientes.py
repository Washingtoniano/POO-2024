import csv
from Clientes import clientes
class GestorC():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def leer(self):
        archivo=open('C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Practica Operativa Tema 2\\ClientesfarmaCiudad.csv','r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                uncliente=clientes(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(uncliente)
        archivo.close
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])
    def BC(self,DNI,bandera=None):
        i=0
        band=False
        while i<len(self.__lista) and self.__lista[i].getDNI()!=DNI:
            i+=1
        if i<len(self.__lista):
            band=self.__lista[i].getNum()
        if bandera!=None:
            nombre=self.__lista[i].getNomb()
            apellido=self.__lista[i].getApelli()
            band=(nombre)+(apellido)
        return band
    def actualizar(self,acum,DNI):
        i=0
        while i< len(self.__lista) and self.__lista[i].getDNI()!=DNI:
            i+=1
        if i<len(self.__lista):
            self.__lista[i].setSaldo(acum)
    def indice(self,DNI):
        i=0
        while i< len(self.__lista) and self.__lista[i].getDNI()!=DNI:
            i+=1
        return i
    def getNombre(self,i):
        return self.__lista[i].getNomb()
    def getApellid(self,i):
        return  self.__lista[i].getApelli()
    def getNumero(self,i):
        return self.__lista[i].getNum()
    def getSaldo(self,i):
        return self.__lista[i].getSaldo()
            


