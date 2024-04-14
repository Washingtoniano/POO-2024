class CajaDeAhorro():
    __ncuenta=str
    __cuil=str
    __apellido=str
    __nombre=str
    __saldo=float
    def __init__(self,ncuenta=None,cuil=None,apellido=None,nombre=None,saldo=0.0):
        self.__ncuenta=ncuenta
        b=0
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        while (b==0):
            if (self.comprobar(self.__cuil)==True):
                b=1
            else:
                cui=input("Cuil Invalido\n ingrese de nuevo\n")
                self.__cuil=cui
        #self.__saldo=saldo
        # if ncuenta=='':
        #     self.__ncuenta=None
        # else:
        #     self.__ncuenta=ncuenta

        # if cuil =='':
        #     self.__cuil=None
        # else:
        #     self.__cuil=cuil

        # if apellido=='':
        #     self.__apellido=None
        # else:
        #     self.__apellido=apellido

        # if nombre=='':
        #     self.__nombre=None
        # else:
        #     self.__nombre=nombre

        if saldo=='':
             self.__saldo=0.0
        else:
             self.__saldo=float(saldo)
    def __str__(self):
        return("Los datos son\n n°de cuenta:{} cuil: {} apellido:{} nombre:{} saldo:{}".format(self.__ncuenta,self.__cuil,self.__apellido,self.__nombre,self.__saldo))
    def mostrar(self):
        print("Los datos son\n n°de cuenta:{} cuil: {} apellido:{} nombre:{} saldo:{}".format(self.__ncuenta,self.__cuil,self.__apellido,self.__nombre,self.__saldo))
    def cargarA(self):
        self.__apellido()
    def extraer(self,monto):
        resultado=-1
        print("{}".format(type(self.__saldo)))
        if(self.__saldo>=monto):
            self.__saldo=self.__saldo-monto
            resultado=self.__saldo
        return resultado

    def depositar(self,monto):
        #valor=-1
        if(monto>0):
            self.__saldo=self.__saldo+monto
            #valor=self.__saldo
        return self.__saldo
    def darCuil(self):
        return self.__cuil
    def darNom(self):
        return self.__nombre
    def darApe(self):
        return self.__apellido
    def darNCuen(self):
        return self.__ncuenta
    #def darSal(self):
    #    return self.__saldo
    def comprobar(self, cuil):
        #print("{}".format(cuil))
        partes=cuil.split('-')
        band=False
        if len(partes)==3:
            if ((int (partes[0])==27) or (int (partes[0])==30) or (int (partes[0])==20) or (int(partes[0])==23)):
                if (int(len(partes[1]))==8):
                    if (int(len(partes[2]))==1):
                        acum=0
                        numeros=[5,4,3,2,7,6,5,4,3,2]
                        cant=partes[0]+partes[1]
                        #cant
                        for i in range (len(cant)):
                            acum=acum+(int(cant[i])*numeros[i])
                            print("{}*{}={}".format(cant[i],numeros[i],acum))
                        val=acum/11
                        rest=acum-(int(val)*11)
                        int(rest)
                        print("Val {}".format(val))
                        print("Rest {}".format(rest))
                        if rest==0:
                            if int(partes[2])==0:
                                band=True
                        elif rest==1:
                            
                            if int(partes[0])==23:
                                if int(partes[2])==9:

                                    band=True
                            elif int(partes[0])==23:
                                if int(partes[2])==4:

                                    band=True
                        else:
                            if int(partes[2])==(11-rest):
                                band=True
        return band