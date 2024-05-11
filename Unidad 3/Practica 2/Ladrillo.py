#from MatReflactario import Reflactario
class ladrillo():
    alto=7
    largo=25
    ancho=15
    __cantidad:int
    __id:int
    __kgMPU:float
    __costo:float
    __reflactario=object
    def __init__(self,cantidad,id,MP,costo,ref) -> None:
        self.__cantidad=cantidad
        self.__id=id
        self.__kgMPU=MP
        self.__costo=costo
        if ref!=None:
            self.__reflactario=ref
            self.__costo=costo+self.__reflactario.getCA()

    def getCantidad(self):
        return self.__cantidad
    def getID(self):
        return self.__id
    def getkgMPU(self):
        return self.__kgMPU
    def getCosto(self):
        return self.__costo