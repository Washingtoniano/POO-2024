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
                    n=20
                    print(f"Equipo:{E}\n")
                    print(f"{"Fecha":{n}}{"Goles a Favor":{n}}{"Goles en contra":{n}}{"Diferencia de goles":{n}}{"Puntos":{n}}")
                    #self.__GF.buscarfecha(res)
                    puntos=0
                    acumDIF=0
                    acumFavor=0
                    acumcontra=0
                    F=int(len("Fecha"))
                    #print("Espacio: {}".format(len(f"{"Fecha":{n}}")))
                    GF=int((len("Goles a Favor")))
                    GC=int((len("Goles en contra")))
                    DG=int((len("Diferencia de goles")))
                    P=int((len("Puntos")))
                    #print("Espacio {}".format(F+GF+GC+DG+P))
                    for i in range (self.__GF.len()):
                        golV=self.__GF.getGolV(i)
                        golL=self.__GF.getGolV(i)
                        fecha=self.__GF.getfecha(i)
                        d=0
                        m=0
                        if res== self.__GF.getIDL(i):
                            d=self.calcular(golL,golV)
                            #print("{} {} {} {} {}".format(F,GF,GC,DG,P))
                            F=n-len(fecha)

                            #Por algun motivo le sobran dos espacios

            #Aclaración y recordatorio para consulta, durante la elaboración de esta lista se presentaron muchos problemas que
            #tuve que solucionar como pude dentro de mis posibilidades. La lista resultante cumple con la consigna y el formato, sin embargo
            #tiene muchos parches y arreglos que le hice mientras probaba, si fue un proceso de prueba y error, de los cuales pude darme cuenta que
            #en muchos casos a al alista le sobraban o le faltaban espacios, espcialmente cuando usaba la constante {n}, para ello decidi hacer una formula
            #que calcule los espacio, basicamente a n se le restan los lugares de correspondientes a la cadena o elemento que quiere representar. Esto lo hice asi,
            #porque al aplicar n no quedaba parejo ni coincidian las filas con las columnas. Es mas si se alter n (n=20) la lista se desordenara
            #por lo visto los espacios asignados al primero elemento se suman con el segundo, es decir del primer al segundo elmento hay una diferencia de n*2 y del segundo en adelante de n.
                            GF=n-self.verificar(golL)
                            GC=n-self.verificar(golV)
                            DG=n-self.verificar(golL-golV)
                            P=n-2-self.verificar(m) 
                            
                            
                            #print("{} {} {} {} {}".format(F,GF,GC,DG,P))
                            print(f"{fecha:{F}}{golL:{GF}}{golV:{GC}}{golL-golV:{DG}}{d:{P}}")
                            #print(f"{fecha:{n}}{golL:{n}}{golV:{n}}{golL-golV:{n}}{d:{n}}")
                            #print("Espacio{}".format(len(f"{fecha:{F}}")))
                            #print(f"{fecha:10}{golL:GF}{golV:GC}{golL-golV:DG}{d:P}")
                            acumDIF+=golL-golV
                            acumFavor+=golL
                            acumcontra+=golV
                        
                        
                        elif res ==self.__GF.getIDV(i):
                            #se pueden hacer columnas colocando un unmero entr las llaves {x}
                            m=self.calcular(golV,golL)
                            F=n-len(fecha)
                            GF=n-self.verificar(golV)
                            GC=n-self.verificar(golL)
                            DG=n-self.verificar(golV-golL)
                            P=n-self.verificar(m)-1
                            
                            print(f"{fecha}{golV}{golL}{golV-golL}{d:}")
                            acumDIF+=golV-golL
                            acumFavor+=golV
                            acumcontra+=golL
                        puntos=puntos+d+m
                    
                    #Por algun motivo le faltan dos espacios
                    print(f"Totales:{acumFavor:{GF+2}}{acumcontra:{GC}}{acumDIF:{DG}}{puntos:{P}}")
                    
                    #print(f"Totales:{acumFavor:{n}}{acumcontra:{n}}{acumDIF:{n}}{puntos:{n}}")

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
    def verificar(self,v):
        d=0
        if v>=10:
            d=2
        else:
            d=1
        return d
