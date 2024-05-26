from Matricula import matricula
from Empleado import empleado
from PCapacitacion import Pcapacitacion
import csv
class GMariculas():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
        
    def agregar(self,unamatricula):
        self.__lista.append(unamatricula)

    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 3\\Matricula.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:


            unempleado=empleado(fila[1],fila[2],fila[3])
            unacapacitacion=Pcapacitacion(fila[4],fila[5],fila[6])
            unamatricula=matricula(fila[0],unempleado,unacapacitacion)
            self.agregar(unamatricula)


        archivo.close()

    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
    def BuscarPrograma(self,Programa):
        lista=[]
        for i in range(len(self.__lista)):
            if self.__lista[i].getPC().getNombre()==Programa:
                lista.append(self.__lista[i].getEmp())
        print("\nEstan matriculados en el programa: {} los siguienste empleados:\n".format(Programa))
        for emp in lista:
            print(emp)
    def buscarempleado(self,empleado):
        i=0
        posicion=-1
        while i< len(self.__lista) and self.__lista[i].getEmp()!=empleado:
            i+=1
        if i<len(self.__lista):
            posicion=i
        return posicion
    def BuscarDuracion(self,empleado):
        total=0
        cant=0
        for i in range (len(self.__lista)):
            if self.__lista[i].getEmp()==empleado:
                total+=self.__lista[i].getPC().getDura() 
                cant+=1
        print("El empleado: {} esta incripto a {} cursos y su duracion total es de : {}".format(empleado.getNombre(),cant,total))
        