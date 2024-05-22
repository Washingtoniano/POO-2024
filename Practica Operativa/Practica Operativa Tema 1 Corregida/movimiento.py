class movimiento():
    __numero:int
    __fecha:str
    __descricion:str
    __tipo:str
    __importe:float
    def __init__(self,numero,fecha,descripcion,tipo,importe) -> None:
        self.__numero=int(numero)
        self.__fecha=fecha
        self.__importe=float(importe)
        self.__descricion=descripcion
        self.__tipo=tipo
    def getNumero(self):
        return self.__numero
    def getTipo(self):
        return self.__tipo
    def getImporte(self):
        return self.__importe
    def getFecha(self):
        return self.__fecha
    def getD(self):
        return self.__descricion
    def __str__(self) -> str:
        return ("Numero:{:10}Fecha:{:10}Descripcion:{:20}Tipo:{:10}Importe:{:10}".format(self.__numero,self.__fecha,self.__descricion,self.__tipo,self.__importe))
    def __lt__(self,other):
        b=None
        if self !=None and other !=None:
            if type(other)== int and type (self)!=int:
                b= self.__numero<0
            elif type(self)== int and type(other) != int:
                b= 0< other.getNumero()
            elif type(self)!=int and type (other) !=int:
                b=self.__numero<other.getNumero()

        return b
    def __gt__(self,other):
        b=None
        if self != None and other !=None:
            if type (self)==int and type (other)!=int:
                b= 0>other.getNumero()
            elif type(other)==int and type (self)!=int: 
                b=self.__numero>0
            elif type(other) !=int and type(self) !=int :
                b=self.__numero>other.getNumero()
        
        return  b