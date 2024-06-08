from zope.interface import implementer
from IDirector import IDirector
from ITesorero import ITesorero
from Apoyo import apoyo
from Docente_Investigador import docente_investigador,docente
@implementer(IDirector)
@implementer(ITesorero)
def Tesorero(Manejador_autoridades:ITesorero):
    print("1-Buscar gastos por DNI")
    DNI=input("DNI a buscar--> ") 
    Manejador_autoridades.gastosSueldoPorEmpleado(DNI)
def Director(Manejador_autoridades:IDirector):
    try:
        DNI=int(input("Ingrese el DNI a buscar"))
        op=input("1-ModificarBasico\n2-Modificar Porcentaje por Cargo\n3-Modificar Porcentaje por Categoria\n4-ModifcarImporte extra\n0-salir")
        while op!='0':
            if op=='1':
                nuevo=float(input("ingrese el nuevo basico"))
                Manejador_autoridades.ModificarSueldo(DNI,nuevo)
            elif op=='2':
                por=float(input("Nuevo porcentaje"))
                Manejador_autoridades.modificarPorcentajeporcargo(DNI,por)
            elif op=='3':
                por=float(input("Nuevo porcentaje"))
                Manejador_autoridades.modificarPorcentajeporcategoría(DNI,por)
            elif op=='4':
                nuevo=float(input("ingrese el nuevo basico"))
                Manejador_autoridades.modificarImporteExtra(DNI,nuevo)
            else:
                print("Dato erroneo")
            op=input("1-ModificarBasico\n2-Modificar Porcentaje por Cargo\n3-Modificar Porcentaje por Categoria\n4-ModifcarImporte extra\n0-salir")

    except ValueError:
        print ("Se esperaba un numero")



#¡¡¡ATENCION :  La narrativa no inclui DNI, el programa no funcionara!!!
class Manejador_autoridades():

    __lista:object
    def getLista(self,lis):
        self.__lista=lis

    def gastosSueldoPorEmpleado(self,dni):
        b=self.__lista.buscarDNI(dni)
        if b==None:
            print("No se encontro el dni")
        else:
            print(b)
    def ModificarSueldo(self,DNI,nuevobasico):
        b=self.buscarDNI(DNI)
        if b==None:
            print("No se encontro el DNI")
        else:
            b.setSueldo(nuevobasico)
    def modificarPorcentajeporcargo(self,dni, nuevoPorcentaje):  
        b=self.buscarDNI(dni)
        if b==None:
            print("no se encontro el dni")
        else:
            if isinstance(b,docente):
                op=input("Cual porcentaja va a cambiar\n1-Simple\n2-Semiexlusivo\n3-Exclusivo")
                
                b.setPorcentaje(nuevoPorcentaje)
            else:
                print("El dni no corresponde a un docente")
    def modificarPorcentajeporcategoría(self,dni, nuevoPorcentaje):  
        b=self.buscarDNI(dni)
        if b==None:
            print("No se encotro el DNI")
        else:
            if isinstance(b,apoyo):

                b.setPorcentaje(nuevoPorcentaje)
            else:
                print("El deni no corresponde a un docente investigador")
    
    def modificarImporteExtra(self,dni, nuevoImporteExtra):  
        b=self.buscarDNI(dni)
        if b==None:
            print("No se encotro el DNI")
        else:
            if isinstance(b,docente_investigador):
                b.setImpExtra(nuevoImporteExtra)
            else:
                print("El deni no corresponde a un docente investigador")
  


