#from MatReflactario import Reflactario
class ladrillo():
    __alto=7
    __largo=25
    __ancho=15
    __cantidad:int
    __id:int
    __kgMPU:float
    __costo:float
    __reflactario=[]
    def __init__(self,cantidad,id,MP,costo) -> None:
        self.__cantidad=int(cantidad)
        self.__id=int(id)
        self.__kgMPU=float(MP)
        self.__costo=float(costo)
        self.__reflactario=[]
        
    def agregarMaterial(self,mat):
        self.__reflactario.append(mat)

    def getCantidad(self):
        return self.__cantidad
    def getID(self):
        return self.__id
    def getkgMPU(self):
        return self.__kgMPU
    def getCosto(self):
        return self.__costo
    def getReflactario(self):
        if self.__reflactario!=None:
            for i in range(len(self.__reflactario)):
                print(self.__reflactario[i])
        else:
            print("El ladrillo no posee materiales reflactario")
    def getCostoAdi(self,id):
        total=0
        for i in range(len(self.__reflactario)):
            if self.__reflactario[i].getMaterial()==id:
                print("costo adicional {}".format(self.__reflactario[i].getCA()))
                total+=self.__reflactario[i].getCA()
        print("Costo total {}\n" .format (total+self.__costo))
    def getMaterial(self):
        return self.__reflactario
    
    @classmethod
    def getAlto(cls):
        return cls.__alto
    @classmethod
    def getLargo(cls):
        return cls.__largo
    @classmethod
    def getAncho(cls):
        return cls.__ancho
    def __str__(self) -> str:
        return("Cantidad: {} ID: {} KG: {} Costo:{}".format(self.__cantidad,self.__id,self.__kgMPU,self.__costo))