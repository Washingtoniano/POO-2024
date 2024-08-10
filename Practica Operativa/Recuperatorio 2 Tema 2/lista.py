import csv
from nodo import nodo
from PTelefonia import Telefonia
from PTelevision import Television
class lista():
    __comienzo:None
    __actual:None
    __indice:int
    __tope:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def ag(self,dato):
        unnodo=nodo(dato)
        if self.__comienzo==None:
            self.__comienzo=unnodo
            self.__actual=unnodo
        else:
            aux=self.__comienzo
            while aux.getSiguiente()!=None:
                aux=aux.getSiguiente()
            aux.setSiguiente(unnodo)
        self.__tope+=1

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            dato=self.__actual.getDato()
            self.__indice+=1
            self.__actual=self.__actual.getSiguiente()
            return dato
    def __iter__(self):
        return self

    def agregar(self,dato):
        unnodo=nodo(dato)
        unnodo.setSiguiente(self.__comienzo)
        self.__comienzo=unnodo
        self.__actual=unnodo
        self.__tope+=1
    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Practica Operativa\\Recuperatorio 2 Tema 2\\planes.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                nombre=fila[1]
                duracion=fila[2]
                cober=fila[3]
                precio=fila[4]
                d=dict({"nombre":nombre,"dura":duracion,"cober":cober,"precio":precio})
                if fila[0]=='T':
                    na=fila[5]
                    int=fila[6]
                    unplan=Television(**d,CN=na,CI=int)
                else:
                    tipo=fila[5]
                    min=fila[6]
                    unplan=Telefonia(**d,tipo=tipo,min=min)
                self.ag(unplan)
    def mostrar(self):
        for dato in self:
            dato.mostrar()
    def getTope(self):
        return self.__tope
    def buscar(self,va):
        if va<self.__tope and va>=0:
            po=0
            aux=self.__comienzo
            while(aux!=None and po!=va):
                aux=aux.getSiguiente()
                po+=1
            dato=aux.getDato()
            if isinstance(dato,Telefonia):
                tipo="Telefonia"
            else :
                tipo="Television"
            print("El plan ubicado en la posicion {} es un plan de {}".format (va,tipo))
        else:
            raise IndexError
        
    def BCober(self,co):
        cont=0
        for dato in self:
            if dato.getCobertura().upper()==co:
                cont+=1
                dato.mostrar()
        print("\nLa cantidad de planes de cobertura {} es de {}".format(co,cont))
    def BCanales(self,ca):
        print("Empresas con igual o mayor cantidad de canales\n")
        for dato in self:
            if isinstance(dato,Television):
                if dato.getCN()>=ca:
                    print(dato.getNombre())
    def Mostrar(self):
        for dato in self:
            if isinstance(dato,Telefonia):
                tipo="Telfonia"
            else:
                tipo="Televisiva"
            dato.Mostrar()