import csv
from reserva import reserva
class gestorR():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]

    def leer(self):
        archivo=open("Reservas.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unareserva=reserva(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.append(unareserva)
        archivo.close()
    def buscarRegistro(self,numero):
        i=0
        band=False
        while i<len(self.__lista) and self.__lista[i].getCa()!=numero:
            i=i+1
        if i<len(self.__lista):
            band=True
        return band
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
    def buscarReserva(self,fecha):
        posicion=-1
        i=0
        while i< len(self.__lista) and self.__lista[i].getfecha()!=fecha:
            i+=1
        if i<len(self.__lista):
            posicion=i
        return posicion
    def mostrarReserva(self,fecha,cabaña):
        band=self.buscarReserva(fecha)
        if band!=-1:
            print(f"Reservas para la fecha:{fecha}")
            print(f"{'N° de cabaña':20}{'Importe Diario':20}{'Cantidad de dias':20}{'Seña':20}{'Importe a cobrar':20}")
            for i in range (len(self.__lista)):
                if self.__lista[i].getfecha()==fecha:
                    lacabaña=cabaña.buscar(self.__lista[i].getCa())
                    importe_diarop=lacabaña.getImporte()

                    print(self.formato(i,importe_diarop))
        else:
            print("No se encontro la fecha")
    def formato(self,i,IMPD):
        seña=self.__lista[i].getseña()
        cantdias=self.__lista[i].getdias()
        return("{:10}{:20}{:20}{:20}{:20}".format(self.__lista[i].getCa(),IMPD,cantdias,seña,((IMPD*cantdias)-seña)))

