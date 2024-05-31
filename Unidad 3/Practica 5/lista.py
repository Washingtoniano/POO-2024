from nodo import Nodo
from LibroImpreso import LibroImpreso
from AudioLibro import AudioLibro
import csv
from zope.interface import implementer
from interfaz import Interfaz
@implementer(Interfaz)

class lista():
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        
    def AgregarElemento(self,dato):
        nodo=Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def cargar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 5\\Publicaciones.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if len(fila)==6:
                unlibro=LibroImpreso(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            else:
                unlibro=AudioLibro(fila[0],fila[1],fila[2],fila[3],fila[4])

            self.AgregarElemento(unlibro)
        archivo.close()
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.mostrar()
            aux=aux.getSiguiente()
    def longitud(self):
        cant=0
        aux=self.__comienzo
        while aux!=None:
            cant+=1
            aux=aux.getSiguiente()
        return cant
    def obtener(self,posicion):
        try:
            aux=self.__comienzo
            cant=0
            elemento=self.recorrer(aux,posicion,cant)
            #print("El lemento es" .format(elemento))
            #print(elemento)
            libro=None
            if isinstance(elemento,AudioLibro):
                libro="Audio Libro"
            elif isinstance(elemento,LibroImpreso):
                libro="Libro Impreso"
            return libro
        except TypeError:
            print("Tenemos un problema con el libro")
    def recorrer(self,aux,posicion,cant):
        if cant!=posicion:
            aux=aux.getSiguiente()
            cant+=1
            dato=self.recorrer(aux,posicion,cant)
        else:
            dato=aux.getDato()
            #print(dato)
        #print(dato)

        return dato
    def tipos(self):
        aux=self.__comienzo
        cantA=0
        cantI=0
        while aux!=None:
            if isinstance(aux.getDato(),AudioLibro) :
                cantA+=1
            else:
                cantI+=1
            aux=aux.getSiguiente()
        print("La cantidad de elementos de catologo es\n Audio libros: {} y Libros Impresos: {}".format(cantA,cantI))
    def ElminarELemento(self,ele):
        aux=self.__comienzo
        encontrado=False
        if aux.getDato().getTitulo().upper()==ele.upper():
            encontrado=True
            print("El libro {} se elimino".format(ele))
            self.__comienzo=aux.getSiguiente()
            del aux
        else:
            ant=aux
            aux=aux.getSiguiente()
            while aux!=None and not encontrado:
                if ele==aux.getDato().getTitulo():
                    encontrado=True
                else:
                    ant=aux
                    aux=aux.getSiguiente()
            if encontrado:
                print("El libro {} se elmino".format(ele))
                ant.setSiguiente(aux.getSiguiente())

                del aux
            else:
                print("No se encontro el libro")

    def obtenerDatos(self):
        try:
                op=input("Que tipo de libro desea cargar\n 1-Adio Libro   2-Libro Impreso\n")
                while op!='2' and op !='1':
                    print("Dato no valido\n")
                    op=input("Que tipo de libro desea cargar\n 1-Adio Libro   2-Libro Impreso\n")
                print("Ingrese los datos los siguienstes datos\n")
                libro=None
                nombre=input("Nombre->")
                genero=input("Genero->")
                preciobase=input("Precio Base->")
                if op=='2':
                    autor=input("Autor->")
                    fecha=input("Fecha->")
                    edicion=int(input("N° de Edicion->"))
                    libro=LibroImpreso(nombre,genero,preciobase,autor,fecha,edicion)

                else :
                    duracion=input("Duracion->")
                    narrador=input("Narrador->")
                    libro=AudioLibro(nombre,genero,preciobase,duracion,narrador)
                return libro

        except ValueError:
                print("Se ingreseso un dato no valido")    
    def Insertarelemento(self,libro,pos):
        try:
            cant=0
            aux=self.__comienzo
            if pos==0:
               self.AgregarElemento(libro)
            else:
                cant=1
                ant=aux
                aux=aux.getSiguiente()
                while aux!=None and cant!=pos:
                   ant=aux
                   aux=aux.getSiguiente()
                   cant+=1
                if cant ==pos:
                    nuevo=Nodo(libro)
                    nuevo.setSiguiente(ant.getSiguiente())

                    ant.setSiguiente(nuevo)
                    self.mostrar()
                else:
                    print("Error")

                

        except IndexError:
            print("Lista fuera de rango")
        