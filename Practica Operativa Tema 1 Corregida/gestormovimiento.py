from movimiento import movimiento
import numpy as np
import csv
class gestorM():
    __dimension:int
    __cantidad=int
    __incremento=int
    __movimiento=np.ndarray
    def __init__(self,dimension) -> None:
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=10
        self.__movimiento=np.empty(self.__dimension,dtype=movimiento)
    def agregar(self,unmov):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__movimiento.resize(self.__dimension)
        self.__movimiento[self.__cantidad]=unmov
        self.__cantidad+=1

    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Practica Operativa Corregida\\MovimientosAbril2024.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unmov=movimiento(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregar(unmov)
        archivo.close()
    def mostrar(self):
        for i in range (len(self.__movimiento)):
            if self.__movimiento[i]!=None and self.__movimiento[i]!=0:
                print(self.__movimiento[i])

    def obtenerTeI(self,numero):
        lista=[]
        acumC=0
        acumP=0
        j=1
        for i in range (len(self.__movimiento)):
            if self.__movimiento[i]!=None and self.__movimiento[i] !=0:
                if self.__movimiento[i].getNumero()==numero:
                    if self.__movimiento[i].getTipo()=='P':
                        print("{:10}{:10}{:10}{:10}".format(self.__movimiento[i].getFecha(),self.__movimiento[i].getD(),self.__movimiento[i].getImporte(),self.__movimiento[i].getTipo()))
                        acumP+=self.__movimiento[i].getImporte()
                        #print(f"{self.__movimiento[i].getFecha():10}{self.__movimiento[i].getD():10}-{self.__movimiento[i].getImporte():10}{self.__movimiento[i].getTipo:10}")
                    elif self.__movimiento[i].getTipo()=='C':
                        #print(f"{self.__movimiento[i].getFecha():10}{self.__movimiento[i].getD():10}-{self.__movimiento[i].getImporte():10}{self.__movimiento[i].getTipo:10}")
                        acumC+=self.__movimiento[i].getImporte()
                        print("{:10}{:10}{:10}{:10}".format(self.__movimiento[i].getFecha(),self.__movimiento[i].getD(),self.__movimiento[i].getImporte(),self.__movimiento[i].getTipo()))
    
        return acumC-acumP
    def buscarM(self,num):
        band=False
        i=0
        while i <len(self.__movimiento) and band==False:
            if self.__movimiento[i]!=None and self.__movimiento[i]!=0:
                if self.__movimiento[i].getNumero()==num:
                    band=True
            i+=1
        return band
    def ordenar(self):
        for i in range(len(self.__movimiento)):
            if self.__movimiento[i]==None:
                self.__movimiento[i]=0
        self.__movimiento=np.sort(self.__movimiento)

