import numpy as np
import csv
from Pedido import pedido
class GestorP():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def inicializar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 4\\datos_Pedidos.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            #print("Fila{}".format(fila))
            if band==False:
                band=True
            else:
                unpedido=pedido(fila[0],int(fila[1]),fila[2],fila[3],float(fila[4]))
                self.__lista.append(unpedido)
        archivo.close()
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])
    
    def agregar(self,pa):
        
        print("Ingrese los valores del pedido\n")
        i=int(input("ID: "))
        c=input("Comidas: ")
        Te=input("Tiempo estimado de entrega: ")
        Pr=float(input("Precio Total: "))
        unpedido=pedido(pa,i,c,Te,Pr)
        self.__lista.append(unpedido)
    def modificar(self,pa,id,tr):
        i=0
        while i<len(self.__lista):
            #Los comentarios eran metodos de control 
            #print("Este es el len de la lista{}\n".format(len(self.__lista)))
            #print("{}{}".format(pa,id))
            print("Patente{} ida{}\n".format(self.__lista[i].getpatente(),self.__lista[i].getId()))

            if((self.__lista[i]).getpatente()==pa) and ((self.__lista[i]).getId()==id):
                #print("Este es el pedido{}\n".format(self.__lista[i]))
                self.__lista[i].ModTr(tr)
            i+=1
    def promedio(self,pa):
        i=0
        prom=0
        con=0
        for i in range(len(self.__lista)):
            if(self.__lista[i].getpatente()==pa):
                prom+=self.__lista[i].getTr()
                con+=1
        return float(prom//con)
    def Ordenar(self):
        c=np.sort(self.__lista)
        self.__lista=c
    def regresa_lista(self):
        return self.__lista
    def getID(self,i):
        return (self.__lista[i].getId())
    def getTr(self,i):
        return (self.__lista[i].getTr())
    def getTe(self,i):
        return(self.__lista[i].getTe())
    def getprecio(self,i):
        return(self.__lista[i].getprecio())
    def getpatente(self,i):
        return self.__lista[i].getpatente()