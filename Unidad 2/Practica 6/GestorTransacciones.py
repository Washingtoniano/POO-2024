import csv
from Transaccion import Transaccion
class GestorTransacciones():
    __lista=[]
    def __init__(self) :
        self.__lista=[]
    def inicializar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 6\\transaccionesBilletera.csv","r")
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unaTransaccion=Transaccion(fila[0],fila[1],fila[2],fila[3])
                self.__lista.append(unaTransaccion)

        archivo.close()
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])