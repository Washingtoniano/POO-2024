import csv
from Equipo import equipo
import numpy as np
class gestorEquipos():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def inicizalizar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 5\\equipos2024.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unequipo =equipo(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.__lista.append(unequipo)
        archivo.close

    def buscarequipo(self,E):
        i=0
        band=False
        while i<len(self.__lista) and band ==False:
            if(self.__lista[i].getnombre().upper()==E):
                band=True
            else:
                i+=1
        if band==True:
            band=self.__lista[i].getID()
        return band 
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])
                
    def actualizar(self,id,puntos,GF,GC):
        #Busca el ID en la lista y actualiza los datos
        i=0
        band=False
        while i < len(self.__lista) and band ==False:
            if id ==self.__lista[i].getID():
                self.__lista[i].actualizar(puntos,GF,GC)
                band=True
            else:
                i+=1
    def getID(self,i):
        return self.__lista[i].getID()
    def buscarID (self,GF):
        i=0
        flag=False
        while i <len(self.__lista) and flag==False:
            if self.__lista[i].getID()==GF:
                flag=self.__lista[i].getID()
            else:
                i+=1
        return flag
    def len(self):
        return len(self.__lista)

    def ordenar(self):
        hj=np.sort(self.__lista)
        self.__lista=hj
        #for i in range (len(hj)):
        #    print(hj[i])