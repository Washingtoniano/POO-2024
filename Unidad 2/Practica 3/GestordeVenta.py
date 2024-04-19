class GestorVentas ():
    __ventas=[]
    __dias=7
    __farmacia=5
    def __init__(self):
        for i in range (self.__farmacia):
            self.__ventas.append([0]*self.__dias)
        #self.__ventas=[0]*5[0]*7
    def acumular(self,d,s,importe):
        self.__ventas[s-1][d-1]+=importe
    def calcular(self,s):
        acum=0.0
        for i in range (self.__dias):
            acum+=self.__ventas[s-1][i]
        return acum
    def maximo(self,d):
        max=0
        sucu=0
        for i in range (self.__farmacia):
            if self.__ventas[i][d-1]>max:
                max=self.__ventas[i][d-1]
                sucu=i+1
        return sucu
    def mostrar(self):
        for i in range (self.__farmacia):
            for j in range(self.__dias):
                print("Sucursal:{} Dia{}: Valor:{}".format(i+1,j+1,self.__ventas[i][j]))
    def minimo(self):
        min=9999999
        sucu=0
        for i in range (self.__farmacia):
            val=self.calcular(i+1)
            if min> val:
                min=val
                sucu=i+1
        return sucu
    def total(self):
        for i in range (self.__farmacia):
            val=self.calcular(i+1)
            print("Sucursal {} Total facturado:{}\n".format(i+1,val))
