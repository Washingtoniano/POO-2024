from GestorEquipos import gestorEquipos
from GestorFechas import gestorFechas
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3,
                        '4':self.opcion4,
                        '5':self.opcion5,
                        '6':self.opcion6,
                        '7':self.opcion7,
                        }
    def opcion(self,op,GE,GF):
        fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
        if op =='1' or  op =='2' or  op =='3' or  op =='4' or  op =='5' or  op =='6' or  op =='7':
            fun(GE,GF)
        else:
            fun()
    def opcion1(self,GE,GF):
        if type(GE)==gestorEquipos and type (GF)==gestorFechas:
            GE.inicizalizar()

        else:
            print("Parametro erroneo")
    def opcion2(self,GE,GF):
        if type(GE)==gestorEquipos and type(GF)==gestorFechas:
            GF.inicializar()

        else:
            print("Parametro erroneo")
    def opcion3(self,GE,GF):
        if type(GE)==gestorEquipos and type (GF)==gestorFechas:
#Los goles se deben sacar del archivo de fechas si es local goles a favor cant de local y goles en contra cant de goles del visitante. Si es visitante se invierte. Si la diferencia puede ser negativa, aplicar valor absoluto. 
                E=input("Ingrese el nombre del equipo\n")
                res=GE.buscarequipo(E.upper())
                if res != False:
                    n=27
                    print(f"Equipo:{E}\n")
                    print(f"{"Fecha":{n}}{"Goles a Favor":{n}}{"Goles en contra":{n}}{"Diferencia de goles":{n}}{"Puntos":{n}}")
                    #GF.buscarfecha(res)
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
                    for i in range (GF.len()):
                        golV=GF.getGolV(i)
                        golL=GF.getGolL(i)
                        fecha=GF.getfecha(i)
                        d=0
                        m=0
                        if res== GF.getIDL(i):
                            d=self.puntos(golL,golV)
                            #print("{} {} {} {} {}".format(F,GF,GC,DG,P))
                         

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
                        
                        
                        elif res ==GF.getIDV(i):
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
        else:
            print("Parametro erroneo")
    def opcion4(self,GE,GF):
        try:
            if type(GE)==gestorEquipos and type (GF)==gestorFechas:
                    fecha=None
                    flag=False
                    k=int(input("Se disputaron mas de una fecha\n 1-Si  2-No"))
                    if k==1:
                        fecha=[]
                        i=0
                        a=input("Ingrese las fechas de los partidos 0 para finalizar")
                        while a!=0 and flag==False:                 
                            fecha.append(a)
                            bandera=self.actualizar(fecha,GE,GF)
                            if bandera!=False:
                                print("Fecha valida")
                            else:
                                print("Fecha no valida")
                            i+=1
                            a=input("")
                            if a=="0":
                                flag=True
                        # if flag==True:
                        #     for i in range (len(fecha)):
                        #         self.actualizar(fecha,fecha[i])
                        # print("Se actualizaron las listas\n")
                    elif k==2:
                        fecha=input("Ingrese la fecha del partido")
                        bandera=self.actualizar(fecha,GE,GF)
                        if bandera!=False:
                            print("Se actualizaron las listas\n")
                        else:
                            print("Hubo un error con la fecha")
                    else:
                        print("Dato erroneo")
            else:
                print("Parametro erroneo")
        except ValueError:
            print("Dato ingresado no valido")
    def opcion5(self,GE,GF):
        if type(GE)==gestorEquipos and type (GF)==gestorFechas:
            GE.ordenar()
            print("Se ordeno la lista")
        else:
            print("Parametro erroneo")
    def opcion6(self,GE,GF):
        if type(GE)==gestorEquipos and type (GF)==gestorFechas:
            GE.escribir()

        else:
            print("Parametro erroneo")
    def opcion7(self,GE,GF):
        if type(GE)==gestorEquipos and type (GF)==gestorFechas:
            self.mostrarLista(GE,GF)
        else:
            print("Parametro erroneo")


    def mostrarLista(self,GE,GF):
        print("\nEquipos\n")
        GE.mostrar()
        print("\nFechas\n")
        GF.mostrar()
    
    def actualizar(self,fe,GE,GF):
        #Utiliza la fecha para buscar los ID
        #i=0

        IDV=GF.buscarIDV(fe)
        IDL=GF.buscarIDL(fe)
        band=False
        if IDV==False or IDL==False:
            bandera=False
        # elif type(fe) ==list:
        #     for i in range (len(fe)):
               
        #         for  j in range (GF.len()):
        #         #Iter buscando la fecha si concide calcula:
        #             if fe[i] ==GF.getfecha(j):
        #                 for d in range (GE.len()):
        #                     if (GE.getID(d)==IDL):

        #                         self.calcular(j,IDL,fe[i])
        #                     if (GE.getID(d)==IDV):

        #                         self.calcular(j,IDV,fe[i])
        else:
            i=0
            while i< GF.len() and band!=True:
                #Iter hasta encontrar la fecha, si coincide envia el indice a calcula:
                if fe ==GF.getfecha(i):
                    j=0
                    while j<GE.len():
                        if GE.getID(j)==IDL:
                            self.calcular(i,IDL,GE,GF)
                        if(GE.getID(j)==IDV):
                            self.calcular(i,IDV,GE,GF)
                        j+=1
                    
                    band=True
                #else:
                i+=1
        if band==True:
            bandera=True
        return bandera
    def puntos(self,v,l):
        puntos:int
        if v>l:
            puntos=3
        elif v==l:
            puntos=1
        else:
            puntos=0
        return puntos 
    def calcular(self,i,IDF,GE,GF):
        #i refiere al indice de fecha e IDF al ie a buscar
        P:int
        band=False
        IDE=GE.buscarID(IDF)
        IDFL=GF.getIDL(i)
        IDFV=GF.getIDV(i)
        

        if IDE==IDFL:
            P=self.puntos(GF.getGolL(i),GF.getGolV(i))
            #la funcion GE.actualizar() recibe el id del equipo y los goles
            GE.actualizar(IDE,P,GF.getGolL(i),GF.getGolV(i))
            #GE.actualizarGOLES(IDE,GF.getGolV(i),GF.getGolL(i))
            band=True
        if IDE==IDFV:
            P=self.puntos(GF.getGolV(i),GF.getGolL(i))
            GE.actualizar(IDE,P,GF.getGolV(i),GF.getGolL(i))
            #GE.actualizarGOLES(IDE,IDFV,IDFL)
            band=True
        if band==False:
            print("Error")
        #else:
            #GE.actualizar(IDE,P)
    def verificar(self,v):
        d=0
        if v>=10:
            d=2
        else:
            d=1
        return d
