from PCapacitacion import Pcapacitacion
import csv
class GProgramas():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def agregar(self,unacapacitacion):
        self.__lista.append(unacapacitacion)
    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 3\\Programas.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            unacapacitacion=Pcapacitacion(fila[0],fila[1],fila[2])
            self.agregar(unacapacitacion)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])