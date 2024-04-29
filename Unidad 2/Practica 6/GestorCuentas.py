import numpy as np
import csv
from Cuenta import cuenta
class GestorCuentas():
    __lista=np.array
    def __init__(self):
        self.__lista=[]
    def inicializar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 6\\cuentasBilletera.csv","r")
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unacuenta=cuenta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.__lista.append(unacuenta)
        archivo.close()
        np.array(self.__lista)
    def NPorcentaje(self,p):
        for i in range(len(self.__lista)):
            self.__lista[i].porcentaje(p)
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])