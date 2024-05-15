class movimientos():
    __numero:int
    __fecha:str
    __descripcion:str
    __tipo:str
    __importe:float
    def __init__(self,num,fecha,des,tipo,importe) -> None:
        self.__descripcion=des
        self.__fecha=fecha
        self.__numero=int(num)
        self.__tipo=tipo
        self.__importe=float(importe)

    def getImp(self):
        return self.__importe
    def gettipo(self):
        return self.__tipo
    def getnumero(self):
        return self.__numero
    def getdesc(self):
        return self.__descripcion
    def getFecha(self):
        return self.__fecha
    

    def __lt__(self,other):
        b=None
        #print(type(self))
        #print(type(other))
        if type(self)==int and type(other)!=int:
            
            b=0<other.getnumero()
        elif type(self)!=int and type(other)==int:
            b=self.__numero<0
        else:
            b=self.__numero< other.getnumero()


        return b
    def __gt__(self,other):
        b=None
        #print(type(self))
        #print(type(other))
        if type(self)==int and type(other)!=int:
            
            b=0>other.getnumero()
        elif type(self)!=int and type(other)==int:
            b=self.__numero>0
        else:
            b=self.__numero> other.getnumero()


        return b
    def __str__(self) -> str:
        return ("Numero:{:5}Fecha:{:5}Descripcion:{:5}Tipo:{:5}Importe:{:5}".format(self.__numero,self.__fecha,self.__descripcion,self.__tipo,self.__importe))