import csv
from Fecha import fecha
class gestorFechas():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def inicializar(self):
        archivo =open("/home/lia-t-04/Escritorio/Practica 5/fechasFutbol.csv",'r')
        reader= csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unafecha=fecha(fila[0],(fila[1]),(fila[2]),(fila[3]),(fila[4]))
                self.__lista.append(unafecha)
        archivo.close
    def buscarfecha(self,i):
        return self.__lista[i].getfecha()
    def getIDL(self,i):
        return self.__lista[i].getIDLocal()
    def getIDV(self,i):
        return self.__lista[i].getIDVisitante()
    def getfecha(self,i):
        return self.__lista[i].getfecha()
    def getGolL(self,i):
        return self.__lista[i].getGolesLocal()
    def getGolV(self,i):
        return self.__lista[i].getGolesVisitante()
    def len(self):
        return len(self.__lista)
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])