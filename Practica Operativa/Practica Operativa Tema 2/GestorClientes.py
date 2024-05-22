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
    def BC(self,DNI):
        i=0
        posicion=-1
        while i<len(self.__lista) and self.__lista[i].getDNI()!=DNI:
            i+=1
        if i<len(self.__lista):
            posicion=i
        return posicion
    def darobjeto(self,i):
        return self.__lista[i]
    




            


