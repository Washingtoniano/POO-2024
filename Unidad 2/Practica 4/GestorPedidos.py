#import numpy as np
import csv
from Pedido import pedido
class GestorP():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def inicializar(self):
        archivo=open("Pedidos.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            #print("Fila{}".format(fila))
            if band==False:
                band=True
            else:
                unpedido=pedido(fila[0],int(fila[1]),fila[2],fila[3],fila[4])
                self.__lista.append(unpedido)
        archivo.close()
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])
    
    def agregar(self,pa):
        unpedido=pedido
        print("Ingrese los valores del pedido\n")
        i=int(input("ID: "))
        c=input("Comidas: ")
        Te=input("Tiempo estimado de entrega: ")
        Pr=float(input("Precio Total: "))
        unpedido(pa,i,c,Te,Pr)
        self.__lista.append(unpedido)
    def modificar(self,pa,id,tr):
        i=0
        while i<len(self.__lista):
            print("Este es el len de la lista{}\n".format(len(self.__lista)))
            print("{}{}".format(pa,id))
            print("Patente{} ida{}\n".format(self.__lista[i].getpatente(),self.__lista[i].getId()))

            if((self.__lista[i]).getpatente()==pa) and ((self.__lista[i]).getId()==id):
                print("Este es el pedido{}\n".format(self.__lista[i]))
                self.__lista[i].ModTr(tr)
            i+=1
    def promedio(self,pa):
        i=0
        prom=0
        Con=0
        while i<len(self.__lista):
            if(self.__lista[i].getPatente()==pa):
                prom+=self.__lista[i].getTr()
                con+=1
            i=i+1
        return float(prom/con)
