from GestorFechas import gestorFechas
from GestorEquipos import gestorEquipos
class menu():
    __GF=gestorFechas()
    __GE=gestorEquipos()
    def __init__(self):
        self.__GE=gestorEquipos()
        self.__GF=gestorFechas()
    def inicializar(self):
        self.__GE.inicizalizar()
        self.__GF.inicializar()
    def manejadror(self):
        #self.inicializar()
        v=int(input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n3-Obtener listado\n4-Actualizar la tabla con las fechas\n5-Ordenar la tabla con posiciones mayor a menor\n6-Almacenar la tabla en un archivo csv\n"))
        band=False
        while band!=True and v>=0:
            if v==1:
                self.__GE.inicizalizar()
            elif v==2:
                self.__GF.inicializar()
            elif v==3:
                #Los goles se deben sacar del archivo de fechas si es local goles a favor cant de local y goles en contra cant de goles del visitante. Si es visitante se invierte. Si la diferencia puede ser negativa, aplicar valor absoluto. Si gana 3 puntos si empata 0 y si pierde -3
                E=input("Ingrese el nombre del equipo\n")
                res=self.__GE.buscarequipo(E.upper())
                if res != False:
                    print("Equipo:{}\nFecha   Goles a favor   Goles en contra   Diferencia de Goles, Puntos".format(E))
                    #self.__GF.buscarfecha(res)
                    puntos=0
                    for i in range (self.__GF.len()):
                        golV=self.__GF.getGolV(i)
                        golL=self.__GF.getGolV(i)
                        d=0
                        m=0
                        acumDIF=0
                        acumFavor=0
                        acumcontra=0
                        if res== self.__GF.getIDL(i):
                            d=self.calcular(golV,golL)
                            print("{}  {}  {}  {}  {}".format(self.__GF.getfecha(i),golL,golV,golL-golV,d))
                            acumDIF+=golL-golV
                            acumFavor+=golL
                            acumcontra+=golV
                        elif res ==self.__GF.getIDV(i):
                            #se pueden hacer columnas colocansd un unmero entr las llaves {x}
                            m=self.calcular(golV,golL)
                            print("{}  {}  {}  {}  {}".format(self.__GF.getfecha(i),golV,golL,golV-golL,m))
                            acumDIF+=golV-golL
                            acumFavor+=golV
                            acumcontra+=golL
                        puntos=puntos+d+m
                    print("Totales: {} {} {} {}".format(acumFavor,acumcontra,acumDIF,puntos))
                else: 
                    print("No se encontro el equipo")

            elif v==4:
                fecha=None
                v=int(input("Se disputaron mas de una fecha\n 1-Si  2-No"))
                if v==1:
                    fecha=[]
                    a=input("Ingrese las fechas de los partidos 0 para finalizar")
                    while a!=0:                 
                        fecha.append(a)
                        a=input("")
                else:
                    fecha=input("Ingrese las fechas de los partidos")
                self.actualizar(fecha)
            elif v==7:
                self.mostrarLista()
            elif v==0:
                band=True
            else:
                print("Datos erroneos\n")
            v=int(input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n"))
        
        
    def mostrarLista(self):
        print("\nEquipos\n")
        self.__GE.mostrar()
        print("\nFechas\n")
        self.__GF.mostrar()
    def actualizar(self,fe):
        if fe==None:
            print("dato erroneo\n")
        elif type(fe) ==list:
            for i in range (len(fe)):
                pass
        else:
            self.__GF.buscarID(fe)
            self.__GE.actualizar(fe)
    def calcular(self,v,l):
        puntos:int
        if v>l:
            puntos=3
        elif v==l:
            puntos=0
        else:
            puntos=-3
        return puntos