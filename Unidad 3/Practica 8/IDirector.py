from zope.interface import Interface
class IDirector(Interface):
    def ModificarSueldo(DNI,nuevobasico):
        pass
    def modificarPorcentajeporcargo(dni, nuevoPorcentaje):  
        pass  
    def modificarPorcentajeporcategoría(dni, nuevoPorcentaje):  
        pass  
    def modificarImporteExtra(dni, nuevoImporteExtra):  
        pass 