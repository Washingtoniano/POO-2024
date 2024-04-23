from Moto import moto
import csv
class GestorM():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    
    def inicializar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 4\\datos_Motos.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                #print("Fila{}".format(fila))
                unamoto=moto(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unamoto)
    def Buscar(self,pa,o=0):
        i=0
        Band=False
        if len(self.__lista)!=0:
        
            while (i<len(self.__lista)) and (pa!=self.__lista[i].getpatente()):
                i+=1
            Band=False
            if (i<len(self.__lista)):
        
                Band=True
        else:
            Band=0
        if o==1 and Band ==True:
            Band=i
        return Band
                
    def mostrar(self):
        for i in range (len(self.__lista)):
            print(self.__lista[i])
    def mostrarCon(self,pa):
        i=self.Buscar(pa,1)
        if type(i)== int:
            print("El conductor {}{}\n".format(self.__lista[i].getNombre(),self.__lista[i].getapellido()))
            i=self.__lista[i].getpatente()
        return (i)