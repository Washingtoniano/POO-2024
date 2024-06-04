from productoC import productoC
from productoR import productoR
import csv
class manejador():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]

    def agregar(self,dato):
        self.__lista.append(dato)

    def leer(self):
        archivo=open("productos.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                if fila[0]=='C':
                    unproducto=productoC(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12])
                else:
                    unproducto=productoR(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
                self.agregar(unproducto)
        archivo.close()
    
    def mostrar(self):
        for i in range(len(self.__lista)):
            self.__lista[i].mostrar()

    def mostrarFormato(self):
        for i in range(len(self.__lista)):
            self.__lista[i].mostrarFormato()
    def mostrarTipos(self):
        cantE=0
        cantC=0
        for i in range (len(self.__lista)):
            if isinstance(self.__lista[i],productoC):
                cantC+=1
            else:
                cantE+=1
        print("Hay un total de {} productos de los cuales {} son congelados y {} envasados\n".format(cantC+cantE,cantC,cantE))

    def nuevoproducto(self):
        try:
            codigo=input("Ingrese el codigo del pruducto(C-ongelado/E-Envasado)\n")
            if codigo.upper()!="C" and codigo.upper()!="E":
                print("Dato no valido")
            else:
                print("Ingrese los datos del producto")
                nom =input("Nombre-> ")
                Fv=input("Fecha de vencimiento-> ")
                Fe=input("Fecha de embalaje-> ")
                tem=float(input("Temperatura-> "))
                pais=input("Pais-> ")
                lote=input("Lote-> ")
                costo=float(input("Costo->"))
                if codigo.upper()=='C':
                    met=input("Metodo de congelacion-> ")
                    print("Porcentaje de")
                    oxigeno=int(input("Oxigeno->"))
                    nitrogeno=int(input("Nitrogeno-> "))
                    dio=int(input("Dioxido de carbono-> "))
                    agu=int(input("Agus->"))
                    unproducto=productoC(nom,Fe,Fv,tem,pais,lote,costo,nitrogeno,oxigeno,dio,agu,met)
                else:
                    cod=input("Codigo->")
                    unproducto=productoR(nom,Fe,Fv,tem,pais,lote,costo,cod)
                self.agregar(unproducto)


        except ValueError:
            print("Se esperaba un numero")


    def tipo(self):
        try:
            long=len(self.__lista)
            num=int(input("la lista tiene {} de longitud\ningrese un valor que este entre 0 y {}".format(long,long-1)))

            if isinstance(self.__lista[num],productoC):
                print("El producto en la posicio {} es un producto congelado\n".format(num))
            else:
                print("El producto en la posicio {} es un producto envasado\n".format(num))

        except IndexError:
            print("La lista se fue de rango")
        except ValueError:
            print("Se esperaba un numero")

        