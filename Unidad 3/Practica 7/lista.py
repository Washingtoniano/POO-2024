from nodo import nodo
from zope.interface import implementer
from Personal import personal
from interfaz import Interface
from Apoyo import apoyo
from Investigador import investigador 
from Docente import docente
from Docente_Investigador import docente_investigador
@implementer(Interface)
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
    
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.getDato().mostrar()
            aux=aux.getSiguiente()

    def solicitar(self):
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

        self.AgregarElemento(unpersonal)
