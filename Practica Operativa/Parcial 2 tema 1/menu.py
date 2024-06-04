from manejador import manejador
class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5

        }
    def opcion(self,op,man):
        if type(man)==manejador:
            fun=self.__switcher.get(op,lambda:print("Dato erroneo"))
            if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
                fun(man)
            else:
                fun()
        else:
            print("Parametro no valido")

    def opcion3(self,man):
        man.mostrarTipos()
    def opcion2(self,man):
        man.tipo()
    def opcion1(self,man):
        man.nuevoproducto()

    def opcion4(self,man):
        man.mostrarFormato()
    def opcion5(self,man):
        man.mostrar()