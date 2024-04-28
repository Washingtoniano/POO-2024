from GestorFechas import gestorFechas
from GestorEquipos import gestorEquipos
#puntaje:int=0
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
        v=int(input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n3-Obtener listado\n4-Actualizar la tabla con las fechas\n5-Ordenar la tabla con posiciones mayor a menor\n6-Almacenar la tabla en un archivo csv\n7-Mostrar Listas guardadas\n0-Cerrar\n"))
        band=False
        while band!=True and v>=0:
            if v==1:
                self.__GE.inicizalizar()
            elif v==2:
                self.__GF.inicializar()
            elif v==3:
                #Los goles se deben sacar del archivo de fechas si es local goles a favor cant de local y goles en contra cant de goles del visitante. Si es visitante se invierte. Si la diferencia puede ser negativa, aplicar valor absoluto. 
                E=input("Ingrese el nombre del equipo\n")
                res=self.__GE.buscarequipo(E.upper())
                if res != False:
                    n=27
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
                        golL=self.__GF.getGolL(i)
                        fecha=self.__GF.getfecha(i)
                        d=0
                        m=0
                        if res== self.__GF.getIDL(i):
                            d=self.puntos(golL,golV)
                            print("{} {} {} {} {}".format(F,GF,GC,DG,P))
                         

                            #Por algun motivo le sobran dos espacios

            #Aclaración y recordatorio para consulta, durante la elaboración de esta lista se presentaron muchos problemas que
            #tuve que solucionar como pude dentro de mis posibilidades. La lista resultante cumple con la consigna y el formato, sin embargo
            #tiene muchos parches y arreglos que le hice mientras probaba, si fue un proceso de prueba y error, de los cuales pude darme cuenta que
            #en muchos casos a al alista le sobraban o le faltaban espacios, espcialmente cuando usaba la constante {n}, para ello decidi hacer una formula
            #que calcule los espacio, basicamente a n se le restan los lugares de correspondientes a la cadena o elemento que quiere representar. Esto lo hice asi,
            #porque al aplicar n no quedaba parejo ni coincidian las filas con las columnas. Es mas si se alter n (n=20) la lista se desordenara
            #por lo visto los espacios asignados al primero elemento se suman con el segundo, es decir del primer al segundo elmento hay una diferencia de n*2 y del segundo en adelante de n.
                            F=n-len(fecha)
                            GF=n-self.verificar(golL)
                            GC=n-self.verificar(golV)
                            DG=n-self.verificar(golL- golV)
                            P=n-self.verificar(d)
                            #k=int(n/2)
                            
                            #print("{} {} {} {} {}".format(F,GF,GC,DG,P))
                            #print("if")
                            
                            #print(f"{fecha:{F}}{golL:{GF}}{golV:{GC}}{golL-golV:{DG}}{d:{P}}")
                            #print(f"{fecha:{n}}{golL:{k}}{golV:{k}}{golL-golV:{k}}{d:{k}}")
                            #print("Espacio{}".format(len(f"{fecha:{F}}")))
                            
                            print(f"{fecha:10}{golL:{GF}}{golV:{GC}}{golL-golV:{DG}}{d:{P}}")
                            
                            #print("{:10}{:10}{:10}{:10}{:10}".format(fecha,golL,golV,golL-golV,d))
                            acumDIF+=golL-golV
                            acumFavor+=golL
                            acumcontra+=golV
                            #self.actualizar(res,d)
                        
                        
                        elif res ==self.__GF.getIDV(i):
                            #se pueden hacer columnas colocando un unmero entr las llaves {x}
                            m=self.puntos(golV,golL)
                           
                            F=n-len(fecha)
                            GF=n-self.verificar(golV)
                            GC=n-self.verificar(golL)
                            DG=n-self.verificar(golV- golL)
                            P=n-self.verificar(m)
                            
                            #print("else")
                            print(f"{fecha}{golV:{GF}}{golL:{GC}}{golV-golL:{DG}}{m:{P}}")

                            #print(f"{fecha}{golV}{golL}{golV-golL}{d}")
                            acumDIF+=golV-golL
                            acumFavor+=golV
                            acumcontra+=golL
                        
                        puntos=puntos+d+m
                       
                    
                    #Por algun motivo le faltan dos espacios
                    #print("Totales{:10}{:10}{:10}".format(acumFavor,acumcontra,acumDIF,puntos))
                    print(f"{"Totales":10}{acumFavor:{GF}}{acumcontra:{GC}}{acumDIF:{DG}}{puntos:{P}}")
                    
                    #print(f"{"Totales":{F}}{acumFavor:{n}}{acumcontra:{n}}{acumDIF:{n}}{puntos:{n}}")

                else: 
                    print("No se encontro el equipo")

            elif v==4:
                #print("Se actualizaron las listas\n")
                fecha=None
                flag=False
                k=int(input("Se disputaron mas de una fecha\n 1-Si  2-No"))
                if k==1:
                    fecha=[]
                    a=input("Ingrese las fechas de los partidos 0 para finalizar")
                    while a!=0 and flag==False:                 
                        fecha.append(a)
                        a=input("")
                        if a==0:
                            flag=True
                        #self.actualizar(fecha)

                elif k==2:
                    fecha=input("Ingrese la fecha del partido")
                    flag=True
                if flag==True:
                    self.actualizar(fecha)
                else:
                    print("Dato erroneo")
            elif v==7:
                self.mostrarLista()
            elif v==0:
                band=True
            else:
                print("Datos erroneos\n")
            v=int(input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n3-Obtener listado\n4-Actualizar la tabla con las fechas\n5-Ordenar la tabla con posiciones mayor a menor\n6-Almacenar la tabla en un archivo csv\n7-Mostrar Listas guardadas\n0-Cerrar\n"))
        
        
    def mostrarLista(self):
        print("\nEquipos\n")
        self.__GE.mostrar()
        print("\nFechas\n")
        self.__GF.mostrar()
    
    def actualizar(self,fe):
        #Utiliza la fecha para buscar los ID
        i=0
        IDV=self.__GF.buscarIDV(fe)
        IDL=self.__GF.buscarIDL(fe)
        band=False
        if fe==None:
            print("dato erroneo\n")
        elif type(fe) ==list:
            for i in range (len(fe)):
                #Iter buscando la fecha si concide:
                if fe ==self.__GF.getfecha(i):
                    if (self.__GE.getID(i)==IDL):

                        self.calcular(i,IDL)
                    elif (self.__GE.getID(i)==IDV):
                        self.calcular(i,IDV)
        else:
            while i< self.__GF.len() and band!=True:
                #Iter hasta encontrar la fecha, si coincide envia el indice a calcula:
                if fe ==self.__GF.getfecha(i):
                    j=0
                    while j<self.__GE.len():
                        if self.__GE.getID(j)==IDL:
                            self.calcular(i,IDL)
                        elif(self.__GE.getID(j)==IDV):
                            self.calcular(i,IDV)
                        j+=1
                    
                    band=True
                #else:
                i+=1
    def puntos(self,v,l):
        puntos:int
        if v>l:
            puntos=3
        elif v==l:
            puntos=1
        else:
            puntos=0
        return puntos 
    def calcular(self,i,IDF):
        #REVISAR Utiliza el indice REVISAR  es posible que olo lo encontrase por que ambos
        P:int
        band=False
        IDE=self.__GE.buscarID(IDF)
        IDFL=self.__GF.getIDL(i)
        IDFV=self.__GF.getGolV(i)
        if IDE==IDFL:
            P=self.puntos(self.__GF.getGolL(i),self.__GF.getGolV(i))
            self.__GE.actualizar(IDE,P,self.__GF.getGolL(i),self.__GF.getGolV(i))
            #self.__GE.actualizarGOLES(IDE,self.__GF.getGolV(i),self.__GF.getGolL(i))
            band=True
        if IDE==IDFV:
            P=self.puntos(self.__GF.getGolV(i),self.__GF.getGolL(i))
            self.__GE.actualizar(IDE,P,self.__GF.getGolV(i),self.__GF.getGolL(i))
            #self.__GE.actualizarGOLES(IDE,IDFV,IDFL)
            band=True
        if band==False:
            print("Error")
        #else:
            #self.__GE.actualizar(IDE,P)
    def verificar(self,v):
        d=0
        if v>=10:
            d=2
        else:
            d=1
        return d
