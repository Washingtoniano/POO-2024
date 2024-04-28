class fecha():
    __fPartido:str
    __idLocal:int
    __idVisitante:int
    __cantGolesL:int
    __cantGolesV:int
    def __init__(self,fPartido,IdL,IdV,cantL,cantV):
        self.__fPartido=fPartido
        self.__cantGolesL=int(cantL)
        self.__cantGolesV=int(cantV)
        self.__idLocal=int(IdL)
        self.__idVisitante=int(IdV)
    def getfecha(self):
        return self.__fPartido
    def getIDLocal(self):
        return self.__idLocal
    def __str__(self) :
        return("Fecha{:5} IdLocal:{:5} IdVisitante:{:5} cant goles Local {:5} Cant goles Vis{:5}  ".format(self.__fPartido,self.__idLocal,self.__idVisitante,self.__cantGolesL,self.__cantGolesV))
    def getIDVisitante(self):
        return self.__idVisitante
    def getGolesLocal(self):
        return self.__cantGolesL
    def getGolesVisitante(self):
        return self.__cantGolesV