from GestorReflactario import GestorReflactario
from GestorLadrillos import GestorLadrillo
class menu():
    __swithcer=None
    def __init__(self) -> None:
        self.__swithcer={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4

                        }
    def opcion(self,op,GR,GL):
        if type(GR)==GestorReflactario and type(GL)==GestorLadrillo:
            fun=self.__swithcer.get(op,lambda:print("Dato no valido"))
            if op == '1' or op == '2' or op=='3' or op=='4':
                fun(GR,GL)
            else:
                fun()
    def opcion1(self,GR,GL):
        if type(GR)==GestorReflactario and type(GL)==GestorLadrillo:
             ID=int(input("Ingrese el id del ladrillo a buscar"))
             GL.mostrarmaterial(ID)
        else:
            print("Parametros invalidos")
    def opcion2(self,GR,GL):
        if type(GR)==GestorReflactario and type(GL)==GestorLadrillo:
             GL.CostoTotal()
        else:
            print("Parametros invalidos")
    def opcion3(self,GR,GL):
        if type(GR)==GestorReflactario and type(GL)==GestorLadrillo:
             GL.mostrarFormato()
        else:
            print("Parametros invalidos")
    def opcion4(self,GR,GL):
        if type(GR)==GestorReflactario and type(GL)==GestorLadrillo:
            GL.mostrar()
            GR.mostrar()

        else:
            print("Parametros invalidos")