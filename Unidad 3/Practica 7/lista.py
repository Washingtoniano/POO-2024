from nodo import nodo
from zope.interface import implementer
from Personal import personal
from interfaz import Interfaz
from Apoyo import apoyo
from Investigador import investigador 
from Docente import docente
from Docente_Investigador import docente_investigador
@implementer(Interfaz)
class lista():
    __actual:nodo
    __comienzo:nodo
    __indice:int
    __tope:int
    def __init__(self) -> None:
        self.__actual=None
        self.__comienzo=None
        self.__indice=0
        self.__tope=0
#Agrego un nuevo elemento al inicio de la lista
    def AgregarElemento(self,dato):
        unnodo=nodo(dato)
        unnodo.setSiguiente(self.__comienzo)
        self.__comienzo=unnodo
        self.__actual=unnodo
        self.__tope+=1


    def __next__(self):
        if self.__tope==self.__indice:
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
    
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            Personal=[personal.tojson() for personal in self]
        )
        return d
    #Muestro todos los datos de la lista
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.getDato().mostrar()
            aux=aux.getSiguiente()
#Solicito los datos de un nuevo usuario
    def solicitar(self):
        try:
            C=input("Ingrese el tipo de personal que agregara (A(Apoyo)--D(Docente)--I(Investigador)--DI(Docente Investigador))\n")

            while C.upper()!='A' and  C.upper()!='D' and  C.upper()!='I' and  C.upper()!='DI':
                print("Dato no valido")
                C=input("Ingrese el tipo de personal que agregara (A(Apoyo)--D(Docente)--I(Investigador)--DI(Docente Investigador))")
            cuil=input("Cuil--> ")
            apellido=input("Apellido--> ")
            nombre=input("Nombre--> ")
            sueldo=float(input("Sueldo--> "))
            antiguedad=int(input("Antiguedad(en años)--> "))
            if C.upper()=='A':
                categoria=input("Categoria--> ")
                unpersonal=apoyo(cuil=cuil,apellido=apellido,nombre=nombre,sueldo=sueldo,antiguedad=antiguedad,categoria=categoria)
            elif C.upper()=='D':
                carrera=input("Carrera--> ")
                cargo=input ("Cargo--> ")
                catedra=input("Catedra--> ")
                unpersonal=docente(cuil=cuil,apellido=apellido,nombre=nombre,sueldo=sueldo,antiguedad=antiguedad,carrera=carrera,cargo=cargo,catedra=catedra)

            elif C.upper()=='I':
                area= input("Area--> ")
                tipo=input("Tipo--> ")
                unpersonal=investigador(cuil=cuil,apellido=apellido,nombre=nombre,sueldo=sueldo,antiguedad=antiguedad,area=area,tipo=tipo)

            else:
                carrera=input("Carrera--> ")
                cargo=input ("Cargo--> ")
                catedra=input("Catedra--> ")
                area= input("Area--> ")
                tipo=input("Tipo--> ")
                categoria=input("Categoria--> ")
                importeextra=float(input("Importe Extra--> "))
                unpersonal=docente_investigador(cuil=cuil,apellido=apellido,nombre=nombre,sueldo=sueldo,antiguedad=antiguedad,carrera=carrera,cargo=cargo,catedra=catedra,area=area,tipo=tipo,categoria=categoria,importeextra=importeextra)

            return unpersonal
        except ValueError:
            print("Se esperaba un numero")

    #Inserto un elemento en una posicion determinada
    def insertar(self,pos):
        con=0
        aux=self.__comienzo
        if pos==0:
            unnodo=nodo(self.solicitar())
            unnodo.setSiguiente(aux)
            self.__comienzo=unnodo
        else:

            while aux!=None and con!=pos:
                ant=aux
                aux=aux.getSiguiente()
                con+=1

            if con==pos:
                unnodo=nodo(self.solicitar())
                ant.setSiguiente(unnodo)
                unnodo.setSiguiente(aux)
            else:
                print("No se pudo insertar\n")
    #solicito la longitud de la lista
    def len(self):
        con=0
        aux=self.__comienzo
        while aux!=None:
            aux=aux.getSiguiente()
            con+=1
        return con
    #Muestro el tipo de elmento en una posicion
    def MostrarElemento(self,pos):
        con=0
        aux=self.__comienzo
        while aux!=None and con!=pos:
            aux=aux.getSiguiente()
            con+=1
        if con==pos:

            if isinstance(aux.getDato(),apoyo):
                print("Es apoyo")
            elif isinstance (aux.getDato(),docente):
                print("Docente")
            elif isinstance(aux.getDato(),docente_investigador):
                print("Docente Investigador")
            else:
                print("Investigador")
        else:
            print("no se encontro la posicion")


#Busco por carrera y agrego a una lista
    def MostrarDI(self,carrera):
        aux=self.__comienzo
        listado=[]
        while aux!=None:
            if isinstance(aux.getDato(),docente_investigador):
                if aux.getDato().getCarrera().upper()==carrera:
                    listado.append(aux.getDato())
            aux=aux.getSiguiente()
        #Ordeno la lista y muestro los datos
        listado.sort()
        for i in range(len(listado)):
            listado[i].mostrar()


    def MostrarArea(self,area):
        aux=self.__comienzo
        conI=0
        conDI=0
        while aux!=None:
            if isinstance(aux.getDato(),docente_investigador):
                if aux.getDato().getArea().upper()==area.upper():
                    conDI+=1
            elif isinstance (aux.getDato(),investigador):
                if aux.getDato().getArea().upper()==area.upper():
                    conI+=1
            aux=aux.getSiguiente()
        print("La cantidad de docentes investigadores que se dedican a esa area son:\n °Investigadores: {}\n °Docentes Investigadores: {}".format(conI,conDI))

    def MostrarCategoria(self,car):
        aux=self.__comienzo
        total=0
        listado=[]
        while aux!=None:
            if isinstance(aux.getDato(),docente_investigador):
                if aux.getDato().getCategoria().upper()==car.upper():
                    listado.append(aux.getDato())

            aux=aux.getSiguiente()
        for i in range(len(listado)):
            print("Nombre: {}  Apellido: {}  Importe extra: {}".format(listado[i].getNombre(),listado[i].getApellido(),listado[i].getImpExtra()))
            total+=listado[i].getImpExtra()
        print("El total de importe extra es de {}".format(total))



        


