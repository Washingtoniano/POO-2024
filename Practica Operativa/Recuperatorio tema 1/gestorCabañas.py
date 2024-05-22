import numpy as np
from cabaña import cabaña
import csv
class gestorC():
    __cabañas:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int
    def __init__(self,dimension=10) -> None:
        self.__dimension=dimension
        self.__cabañas=np.empty(self.__dimension,dtype=cabaña)
        self.__cantidad=0
        self.__incremento=1
    def agregar(self,unacabaña):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__cabañas.resize(self.__dimension)
        self.__cabañas[self.__cantidad]=unacabaña
        self.__cantidad+=1
    def leer(self):
        archivo=open('Cabañas.csv','r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unacabaña=cabaña(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregar(unacabaña)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__cabañas)):
            print(self.__cabañas[i])


    def comprobar(self,cant,reservas):
        bandera=False
        for i in range(len(self.__cabañas)):
            numero=self.__cabañas[i].getNumero()
            band=reservas.buscarRegistro(numero)
            if self.__cabañas[i]>=cant and band==False:
                bandera=True
                print("La cabaña{} tiene el espacio suficiente\n".format(self.__cabañas[i].getNumero()))
        if bandera==False:
            print("No hay cabañas disponibles")
    def buscar(self,numero):
        i=0
        posicion=-1
        while i<len(self.__cabañas) and self.__cabañas[i].getNumero()!=numero:
            i+=1
        if i< (len(self.__cabañas)):
            posicion=i
        return posicion
    def darobjeto(self,i):
        return self.__cabañas[i]
