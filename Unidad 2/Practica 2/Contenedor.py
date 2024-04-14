from CajaDeAhorro import CajaDeAhorro
class contenedor():
    __lista=[]
    __com=()
    def __init__(self):
        self.__lista=[]
        
    #def inicializar(self):
    #    print("Selecciona la opcion que desea\n 1-Agregar Caja De Ahorro\n 2-Mostrar lista\n 3-Buscar Cuil\n")

    def agregar(self,N,C,A,No,S):
        unacaja=CajaDeAhorro(N,C,A,No,S)
        self.__lista.append(unacaja)
    def mostrar(self):
        for i in range(len(self.__lista)):
            print("{}".format(self.__lista[i].mostrar()))
    def buscarC(self,cuil):
        i=0
        b="No se encontro el archivo"
        
        while self.__lista[i].darCuil()!=cuil:
            i+=1
        if i<=len(self.__lista):
            b= self.__lista[i]
        return b