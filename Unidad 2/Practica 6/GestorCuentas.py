import numpy as np
import csv
from Cuenta import cuenta
class GestorCuentas():
    __cuentas=np.ndarray
    __dimension:int
    __cantidad:int
    def __init__(self,dimension):
        self.__cuentas=np.empty(dimension,dtype=cuenta)
        self.__dimension=dimension
        self.__cantidad=0
    def agregar (self,cuenta):
        if self.__cantidad < self.__dimension:
            self.__cuentas[self.__cantidad]=cuenta
            self.__cantidad+=1
    def inicializar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 6\\cuentasBilletera.csv","r")
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unacuenta=cuenta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregar(unacuenta)
        archivo.close()
    def NPorcentaje(self,p):
        cuenta.setporcentaje(p)
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])