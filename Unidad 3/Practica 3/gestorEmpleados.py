import csv
from Empleado import empleado
class GEmpleado():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def agregar(self,unempleado):
        self.__lista.append(unempleado)
    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 3\\Empleados.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            unempleado=empleado(fila[0],fila[1],fila[2])
            self.agregar(unempleado)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])