from Ladrillo import ladrillo
import csv
class GestorLadrillo():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def leer(self,GR):

        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 2\\Ladrillo.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        cont=0
        for fila in reader:
            if band==False:
                band=True
            else:

                unladrillo=ladrillo(fila[0],fila[1],fila[2],fila[3])
                self.__lista.append(unladrillo)
                unmaterial=GR.buscarMat(int(fila[1]))
                if unmaterial!=None:
                    self.__lista[cont].agregarMaterial(unmaterial)
                    cont+=1
        archivo.close()

    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
    def mostrarmaterial(self,id):
        i=0
        long=len(self.__lista)
        while i<long and self.__lista[i].getID()!=id:
            i+=1
        if i<long:
            self.__lista[i].getReflactario()
        else:
            print("no se encontro el ladrillo")
    def CostoTotal(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            if self.__lista[i].getMaterial!=None:
                self.__lista[i].getCostoAdi(self.__lista[i].getID())


    def mostrarFormato(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i]) 
            materiales=self.__lista[i].getMaterial()
            if materiales !=None:
                 id=self.__lista[i].getID()
                 self.formato(id,materiales)

    def formato(self,id,materiales):
        print(f"{'N° Identificador':10}{'Material':10}{"Costo asociado":10}")
        for i in range(len(materiales)):
            print(f"{id:10}{materiales[i].getMaterial():10}{materiales[i].getCA():10}")