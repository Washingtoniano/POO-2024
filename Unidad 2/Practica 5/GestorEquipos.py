import csv
from Equipo import equipo
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
                
