import numpy as np
from cancha import cancha
import csv
class gestorC():
    __canchas:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int
    def __init__(self,dimension=10) -> None:
        self.__dimension=dimension
        self.__canchas=np.empty(self.__dimension,dtype=cancha)
        self.__cantidad=0
        self.__incremento=10
    def agregar(self,unacancha):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__canchas.resize(self.__dimension)
        self.__canchas[self.__cantidad]=unacancha
        self.__cantidad+=1
    def leer(self):
        archivo=open('Canchas.csv','r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unacancha=cancha(fila[0],fila[1],fila[2])
                self.agregar(unacancha)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__canchas)):
            if self.__canchas[i]!=None and self.__canchas[i]!=0:
                print(self.__canchas[i])
    def darobjeto(self,i):
        return self.__canchas[i]
    def buscarID(self,id):
        i=0
        posicion=-1
        while i<len(self.__canchas)and self.__canchas[i].getId()!=id:
            i+=1
        if i< len(self.__canchas): 
            posicion=i
       
        return posicion
