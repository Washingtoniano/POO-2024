import csv
from Alquiler import alquiler
import numpy as np
class gestorA():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def leer(self):
        archivo=open("Alquiler.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unalquiler=alquiler(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unalquiler)
        archivo.close()
    def mostrar(self):
        print(type(self.__lista))
        for i in range (len(self.__lista)):
            print(self.__lista[i])
    def totalCancha(self,id):
        acum=0
        for i in range (len(self.__lista)):
            if self.__lista[i].getId()==id:
                acum+=self.__lista[i].getDuracion()
        return acum
    def mostrarFormato(self,GC):
        self.ordenar()
        acum=0
        print(f"{'Hora':10}{'Id de chancha':15}{'Duracion de alquiler':20} {'Importe por hora':20}{'Importe alquiler':20}")
        #print(type(self.__lista))
        for i in range (len( self.__lista)):
            bandera=GC.buscarID(self.__lista[i].getId())
            if bandera!=-1:
                objeto=GC.darobjeto(bandera)
                duracion=self.__lista[i].getDuracion()/60
                print (self.formato(i,duracion,objeto.getImporte()))
                acum+=(duracion*bandera)
        print(f"{'Total Recaudado':80}{acum}")
    def formato(self,i,duracion,importe):
        hora=str(self.__lista[i].getHora())+":"+str(self.__lista[i].getMinutos())
        #print(hora)
        return("{:15}{:10}{:10}{:20}{:20}".format(hora,self.__lista[i].getId(),duracion,importe,importe*duracion))

    def ordenar(self):
        self.__lista.sort(reverse=True)