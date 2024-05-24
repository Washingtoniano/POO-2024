from nodo import Nodo
from LibroImpreso import LibroImpreso
from AudioLibro import AudioLibro
from publicacion import publicacion
import csv
class lista():
    __comienzo=Nodo
    def __init__(self) -> None:
        self.__comienzo=None
    def agregar(self,dato):
        nodo=Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    def cargar(self):
        archivo=open("Publicaciones.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if len(fila)==6:
                unlibro=LibroImpreso(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            else:
                unlibro=AudioLibro(fila[0],fila[1],fila[2],fila[3],fila[4])

            self.agregar(unlibro)
        archivo.close()
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.mostrar())
            aux=aux.getSiguiente()
    def longitud(self):
        cant=0
        aux=self.__comienzo
        while aux!=None:
            cant+=1
            aux=aux.getSiguiente()
        return cant
    def obtener(self,posicion):
        aux=self.__comienzo
        cant=0
        elemento=self.recorrer(aux,posicion,cant)
        libro=None
        if isinstance(elemento,AudioLibro):
            libro="Audio Libro"
        else:
            libro='Libro Impreso'
        return libro
    def recorrer(self,aux,posicion,cant):
        if cant!=posicion:
            aux=aux.getSiguiente()
            cant+=1
            self.recorrer(aux,posicion,cant)
        else:
            return aux.getDato()
