from nodo import nodo
from EquipoE import EquipoE
from EquipoP import EquipoP
import csv
class lista():
    __comienzo:nodo
    __actual:nodo
    __tope:int
    __indice:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def ag(self,daot):
        unnodo=nodo(daot)
        unnodo.setSiguiente(self.__comienzo)
        self.__comienzo=unnodo
        self.__actual=self.__comienzo
        self.__tope+=1

    def agregar(self,dato):
        unnodo=nodo(dato)
        if self.__comienzo==None:
            unnodo.setSiguiente(None)
            self.__comienzo=unnodo
            self.__actual=self.__comienzo

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
            self.__actual=self.__actual.getSiguiente()
            self.__indice+=1
            return dato
    def __iter__(self):
        return self
    
    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Practica Operativa\\Recuperatorio 2 Tema 1\\equipos.csv")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                d=dict({"marca":fila[1], "modelo":fila[2],"año":fila[3],"com":fila[4],"pot":fila[5],"cap":fila[6],"tarifa":fila[7],"dias":fila[8]})
                if fila[0]=='E':
                    unequipo=EquipoE(**d,fuente=fila[9])
                else:
                    unequipo=EquipoP(**d,tipo=fila[9],peso=fila[10])
                self.agregar(unequipo)
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.getDato().mostrar()
            aux=aux.getSiguiente()
    def long(self):
        lo=0
        aux=self.__comienzo
        while aux!=None:
            lo+=1
            aux=aux.getSiguiente()
        return lo
    def buscar(self,va):
        dato=None
        aux=self.__comienzo
        po=0
        while aux!=None and po!=va:
            aux=aux.getSiguiente()
            po+=1
        if aux!=None:
            dato=aux.getDato()

            if isinstance(dato,EquipoE):
                equipo="electronico"
            else:
                equipo="pesado"
            print("El equipo en la posicion {} ({} en el archivo) es {}".format(va,va+1,equipo))

        else:
            raise IndexError
    def conteo(self,año):
        con=0
        for dato in self:
            if dato.getAño()==año:
                con+=1
        if con==0:
            print("No hay equipos con ese año de fabricacion")
        else:
            print("Se contaron {} equipos fabricados ese año".format (con))
    def cap(self,cap):
        for dato in self:
            if isinstance(dato,EquipoP) and dato.getCapacidad()!="N/A":
                if int(dato.getCapacidad())<=cap:
                    dato.mostrar()
    def mostrarTotal(self):
        for dato in self:
            dato.mostrar()
            print("Monto total ${}".format(dato.Total()))
            
