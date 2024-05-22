import numpy as np
from Movimientos import movimientos
import csv
class GestorM():
    __Mov=np.ndarray
    __incremento:int
    __dimension:int
    __cantidad:int
    def __init__(self,dimension=10) -> None:
        self.__dimension=dimension
        self.__Mov=np.empty(self.__dimension,dtype=GestorM)
        self.__cantidad=0
        self.__incremento=10
    def agregar(self,unMov):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__Mov.resize(self.__dimension)
        self.__Mov[self.__cantidad]=unMov
        self.__cantidad+=1
    def leer(self):
        archivo=open('C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Practica Operativa Tema 2\\MovimientosAbril2024.csv','r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unmovimento=movimientos(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregar(unmovimento)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__Mov)):
            if self.__Mov[i]!=None and self.__Mov[i]!=0:
                print(self.__Mov[i])
    def BC(self,numero):
        i=0
        band=False
        posicion=-1
        while i<len(self.__Mov) and band==False:
            if self.__Mov[i]!=0 and self.__Mov[i]!=None:
                if self.__Mov[i].getnumero()==numero:
                    band=i
            i+=1
        if i< len(self.__Mov):
            posicion=band
   
        return posicion
    def ordenar(self):
        for i in range(len(self.__Mov)):
            if self.__Mov[i]==None:
                self.__Mov[i]=0
        #self.mostrar()
        self.__Mov=np.sort(self.__Mov)
    def actualizar(self,numero):
        acum=0
        for i in range(len(self.__Mov)):
            if self.__Mov[i]!=None and self.__Mov[i]!=0:
                if self.__Mov[i].getnumero()==numero:
                    print(self.formato(i))
                    if self.__Mov[i].gettipo()=='P':
                        acum=acum-self.__Mov[i].getImp()
                    elif self.__Mov[i].gettipo()=='C':
                        acum=acum+self.__Mov[i].getImp()
                
        return acum
    def formato(self,i):
        return("{:20}{:20}{:10}           {:20}".format(self.__Mov[i].getFecha(),self.__Mov[i].getdesc(),self.__Mov[i].getImp(),self.__Mov[i].gettipo()))
                