class Reflactario():
    __material :int
    __caracteristicas:str
    __CantUtilizada:float
    __CostAdicional:float
    def __init__(self,material,car,CA,CU) -> None:
        self.__material=int(material)
        self.__caracteristicas=car
        self.__CostAdicional=float(CA)
        self.__CantUtilizada=float(CU)
    
    def getCA(self):
        return self.__CostAdicional
    def getMaterial(self):
        return self.__material
    def getCU(self):
        return self.__CantUtilizada
    def Caracterisitcas(self):
        return self.__caracteristicas
    
    def __str__(self) -> str:
        return("Material: {} Caracteristicas: {} CantTuilizada: {} Costo adicional: ${}".format(self.__material,self.__caracteristicas,self.__CantUtilizada,self.__CostAdicional))