from nodo import nodo
from objectoencoder import ObjectEncoder
from CalefactorE import calefactorE
from CalefactorG import calefactorG
from zope.interface import implementer
from interfaz import Interface
@implementer (Interface)
class lista():
    __comienzo:nodo
    __indice:int
    __tope:int
    __actual:nodo
    def __init__(self) -> None:
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
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
    def __iter__(self):
        return self
    def AgregarElemento(self,dato):
        Nodo=nodo(dato)
        Nodo.setSiguiente(self.__comienzo)
        self.__comienzo=Nodo
        self.__actual=Nodo
        self.__tope+=1

    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            aux.mostrar()
            aux=aux.getSiguiente()
   
    def tojason(self):
        d=dict(
            __class__=self.__class__.__name__,
            Calefactores=[calefactor.tojason()for calefactor in self]
        )
        return d
    
    def len(self):
        longitud=0
        aux=self.__comienzo
        while(aux!=None):
            aux=aux.getSiguiente()
            longitud+=1
        return ("La lista tiene {} de longitud, ingrese un elemento de 0 a {}\n".format(longitud,longitud-1))
    
    def InsertarElemento(self,pos):
        aux=self.__comienzo
        actual=0
        while aux!=None and actual!=pos:
            ant=aux
            aux=aux.getSiguiente()
            actual+=1
        if actual==pos:
            unnodo=nodo(self.solicitar())
            
            unnodo.setSiguiente(aux)
            ant.setSiguiente(unnodo)
    def solicitar(self):
        try:
            cal=input("Ingrese el tipo de calefactor(E/Electrico--G/Gas\n)")
            while cal.upper()!='E' and cal.upper()!='G':
                print("Dato erroneo\n")
                cal=input("Ingrese el tipo de calefactor(E/Electrico--G/Gas\n)")
            print("Ingres los datos\n")
            marca=input("Marca---> ")
            modelo=input("Modelo--> ")
            pais=input("Pais--> ")
            precio=float(input("Precio--> "))
            FP=input("Forma de pago -->  ")
            if FP.upper()=='CONTADO':
                cc=1
            else:
                cc=int(input("Cantidad de cuotas--> "))
            promocion=input("Tiene promocion--> ")
            if cal.upper()=='E':
                max=int(input("Ingrese la potencia maxima--> "))
                uncalefactor=calefactorE(marca,modelo,pais,precio,FP,cc,promocion,max)

            else:
                matricula=input("Matricula--> ")
                calorias= int(input("Calorias-- "))
                uncalefactor=calefactorG(marca,modelo,pais,precio,FP,cc,promocion,matricula,calorias)

            return uncalefactor
        except ValueError:
            print("Se esperaba un numero")

    def MostrarElemento(self,pos):
        try:
            aux=self.__comienzo
            actual=0
            while aux!=None and actual!=pos:
                actual+=1
                aux=aux.getSiguiente()

            if actual==pos:
                if isinstance(aux.getDato(),calefactorE):
                    cal="Calefactor electrico"
                else:
                    cal="Calefactor a gas"

                print("El calefactor ubicado en la posicion {} es de un {}".format(pos,cal))
        except IndexError:
            print("La lista se fue de rango")

    def menor(self):
        ant=self.__comienzo
        meno=ant
        aux=ant.getSiguiente()
        while ant !=None:
            if ant<aux:
                meno=ant
            ant=ant.getSiguiente()
            aux=aux.getSiguiente()
            if aux==None:
                ant=ant.getSiguiente()

        print("El calefactor de menor precio es el:")
        print(meno.getDato().mostrarF())

    def buscarMarca(self):
        marca=input("Ingrese la marca a buscar\n")
        aux=self.__comienzo
        while aux!=None:
            if aux.getDato().getMarca().upper()==marca.upper() and isinstance(aux.getDato(),calefactorE):
                print(aux.getDato().getPM())
                print("Modelo: {} Potenica: {} Precio de lista: ${}".format(aux.getDato().getModelo(),aux.getDato().getPM(),aux.getDato().getPrecio()))
            aux=aux.getSiguiente()

    def buscarPromocion(self):
        aux=self.__comienzo
        while aux!=None:
            if aux.getDato().getPromocion().upper()=='SI': 
                print("Marca: {} Modelo: {} Pais: {} Precio de lista: ${}".format(aux.getDato().getMarca(),aux.getDato().getModelo(),aux.getDato().getPais(),aux.getDato().getPrecio()))
            aux=aux.getSiguiente()
    def guardar(self,json):
        json.guardar

   


        

