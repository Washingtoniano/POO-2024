from MatReflactario import Reflactario
import csv
class GestorReflactario():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 2\\MatReflactario.csv",'r')
        band=False
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if band==False:
                band=True
            else:
                unreflactario=Reflactario(fila[0],fila[1],fila[2],fila[3])
                self.__lista.append(unreflactario)
        archivo.close()
    def buscarMat(self,id):
        i=0
        band=None
        long=len(self.__lista)
        while i<long and self.__lista[i].getMaterial()!=id:
            i+=1
        if i<long:
            band=self.__lista[i]
        return band
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
    