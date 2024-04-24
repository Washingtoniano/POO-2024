class fecha():
    __fPartido:str
    __idLocal:int
    __idVisitante:int
    __cantGolesL:int
    __cantGolesV:int
    def __init__(self,fPartido,cantL,cantV,IdL,IdV):
        self.__fPartido=fPartido
        self.__cantGolesL=cantL
        self.__cantGolesV=cantV
        self.__idLocal=IdL
        self.__idVisitante=IdV