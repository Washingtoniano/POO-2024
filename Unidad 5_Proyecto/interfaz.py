from zope.interface import Interface
class IRepartidor(Interface):
    def Acceder(clas):
        pass
    def entrega():
        pass
class IDespachador(Interface):
    def Acceder(clave):
        pass
    def Recepcion(paquete):
        pass
    def Salida(paquete):
        pass
    def LLegadaT(transporte):
        pass
    def AsignarPaquete():
        pass