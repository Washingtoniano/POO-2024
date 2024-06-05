from producto import producto
import datetime as date
class productoR(producto):
    __cod:str
    def __init__(self, nombre, FE, FV, Temp, pais, lote, costo,codigo) -> None:
        super().__init__(nombre, FE, FV, Temp, pais, lote, costo)
        self.__cod=codigo
    
    def getCodigo(self):
        return self.__cod
    
    def mostrar(self):
        super().mostrarFormato()
        print("Codigo de organismo-> {}".format(self.__cod))



    def calcular(self): ##se puede hacer mas simple
        try:
            precio=super().getCosto()
            Env=super().getFV()
            actual=None
            ant=None
            mes=None
            cont=0
            band=False
            i=0
            otro='0'
            while i<len(Env) and cont!=2:
                
                ant=actual
                actual=Env[i]
                
                if actual=='/':
                    cont+=1
                    if len(Env)==10 and band==False:
                        otro=Env[i+1]
                        band=True
                i+=1
            if cont==2:
                mes=otro+ant
            else:
                print("no se puedo recorrer")

            assert (cont==2),"No se puede leer la fecha el formato no es indicado"
            today=date.datetime.now()
            month=today.month
            dif=int(mes)-month
            if dif ==2:
                precio=(precio*10/100)*-1
            else:
                precio=(precio*1/100)

            return precio
        except ValueError:
            print("No se pudo convertir la fecha")

        

        
