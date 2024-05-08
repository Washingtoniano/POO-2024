from cliente import cliente
import csv
class gestorC():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def leer(self):
        archivo=open("ClientesAbril2024.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band== False:
                band=True
            else:
                uncliente=cliente(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(uncliente)
        archivo.close()
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])
    def buscrDNI(self,dni):
        i=0
        band=False
        while band==False and i < len(self.__lista):
            if self.__lista[i].getDNI() ==dni:
      
                band=self.__lista[i].getN()
            i+=1
        return band
    def buscarindice(self,num):
        i=0
        band=False
        while i<len(self.__lista) and self.__lista[i].getN()!=num:
            i+=1
        if i<len(self.__lista):
            band=i
        return band
    def actualizar(self,i,act):
        self.__lista[i].putsaldo(act)
    def getNombreyApellido(self,i):
        return self.__lista[i].getNombreYApellido()
    def getN(self,i):
        return self.__lista[i].getN()
    def getsaldo(self,i):
        return self.__lista[i].getsaldo()
    def buscarN(self,num):
        i=0
        band=False
        while i< len(self.__lista) and band==False:
            if self.__lista[i].getN()== num:
                band=self.__lista[i].getNombreYApellido()
            i+=1
        return band
