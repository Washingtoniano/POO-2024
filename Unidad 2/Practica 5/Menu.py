from GestorFechas import gestorFechas
from GestorEquipos import gestorEquipos
class menu():
    __GF=gestorFechas()
    __GE=gestorEquipos()
    def __init__(self):
        self.__GE=gestorEquipos()
        self.__GF=gestorFechas()
    def inicializar(self):
        self.__GE.inicizalizar()
        self.__GF.inicializar()
    def manejadror(self):
        #self.inicializar()
        v=int(input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n3-Obtener listado\n4-Actualizar la tabla con las fechas\n5-Ordenar la tabla con posiciones mayor a menor\n6-Almacenar la tabla en un archivo csv\n"))
        band=False
        while band!=True and v>0:
            if v==1:
                self.__GE.inicizalizar()
            elif v==2:
                self.__GF.inicializar()
            elif v==0:
                band=True
            else:
                print("Datos erroneos\n")
            v=int(input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n"))
