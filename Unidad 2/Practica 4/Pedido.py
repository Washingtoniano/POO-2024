class pedido():
    __patente:str
    __id:int
    __comidas:str
    __Te:str
    __Tr:str
    __precio:float
    def __init__(self,patente,id,comidas,Te,precio,Tr=0):
        self.__patente=patente
        self.__id=id
        self.__comidas=comidas
        self.__Te=Te
        self.__Tr=Tr
        self.__precio=precio
        
    def __str__(self):
        return("Pedido id:{}--Patente:{}--Comidas:{}--Tiempo estimado:{}--Tiempo real:{}--Precio:{}".format(self.__id,self.__patente,self.__comidas,self.__Te,self.__Tr,self.__precio))
    def __lt__(self,other):
        return self.__patente<other.getpatente()
    def ModTr(self,tr):
        self.__Tr=tr
    def getpatente(self):
        return(self.__patente)
    def getId(self):
        return(self.__id)
    def getTr(self):
        return self.__Tr
    def getTe(self):
        return self.__Te
    def getprecio(self):
        return self.__precio