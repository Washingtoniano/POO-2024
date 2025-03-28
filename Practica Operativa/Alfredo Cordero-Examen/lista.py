import csv

from nodo import nodo

from paciente import paciente
from Pambulatorio import ambulatorio
from PHospitalizados import hospitalizados
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

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__comienzo
            raise StopIteration
        else:
            dato=self.__actual.getDato()
            self.__indice+=1
            self.__actual=self.__actual.getSiguiente()
            return dato
        
    def agregar(self,dato):
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
        
    def getTope(self):
        return self.__tope
    
    def leer(self):
        archivo=open("pacientes.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                d=dict({"nom":fila[1],"ape":fila[2],"email":fila[3],"num":fila[4]})
                if fila[0]=='P':
                    unpaciente=paciente(**d)
                elif fila[0]=='O':
                    historial=fila[5]
                    alergia=fila[6]
                    obrasocial=fila[7]
                    unpaciente=ambulatorio(**d,alergia=alergia,his=historial,obra=obrasocial)
                else:
                    
                    habi=fila[5]
                    ingreso=fila[6]
                    diag=fila[7]
                    dias=fila[8]
                    des=fila[9]
                    unpaciente=hospitalizados(**d,habi=habi,ingreso=ingreso,diag=diag,dias=dias,des=des)
                self.agregar(unpaciente)

    def mostrar(self):
        print("Valor de consulta {} ".format(paciente.getValorcon()))
        for dato in self:
            dato.mostrar()

    def TotalNeumonia(self):
        con=0
        for dato in self:
            if isinstance(dato,hospitalizados):
                if dato.getDiagnostico().upper()=='NEUMONIA':
                    con+=1
        return con
    
    def TotalAmbulatorio(self):
        con=0
        for dato in self:
            if isinstance(dato,ambulatorio):
                con+=1
        return con
    
    def posicion(self,val):
        if val>=0 and val<self.__tope:
            i=0
            aux=self.__comienzo
            while i!=val and aux!=None:
                aux=aux.getSiguiente()
                i+=1
            dato=aux.getDato()
            if dato!=None:
                if isinstance(dato,hospitalizados):
                    tipo="Paciente Hospitalizado"
                elif isinstance(dato,ambulatorio):
                    tipo="Paciente Ambulatorio"
                else:
                    tipo="Paciente"

                print("El valor en la posicion {} es un {}".format(val,tipo))
            else:
                print("Ocurrio un error inesperado")
        else:
            raise IndexError
        
    def getValorcon(self):
        return paciente.getValorcon()
    
    def setValorcon(self,dato):
        paciente.setValorCon(dato)