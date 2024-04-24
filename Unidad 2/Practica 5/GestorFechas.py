import csv
from Fecha import fecha
class gestorFechas():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def inicializar(self):
        archivo =open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 4\\fechasFutbol.csv",'r')
        reader= csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unafecha=fecha(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unafecha)
        archivo.close
