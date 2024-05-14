from Menu import menu
from GestorEquipos import gestorEquipos
from GestorFechas import gestorFechas
if __name__== '__main__':
    print("Bienvenido")
    unmenu=menu()
    GF=gestorFechas()
    GE=gestorEquipos()
    op=input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n3-Obtener listado\n4-Actualizar la tabla con las fechas\n5-Ordenar la tabla con posiciones mayor a menor\n6-Almacenar la tabla en un archivo csv\n7-Mostrar Listas guardadas\n0-Cerrar\n")
    while op!='0':
        unmenu.opcion(op,GE,GF)
        op=input("Seleccione la opcion que desa\n1-Leer datos de los equipos del archivo\n2-Leer los datos de las fechas del archivo\n3-Obtener listado\n4-Actualizar la tabla con las fechas\n5-Ordenar la tabla con posiciones mayor a menor\n6-Almacenar la tabla en un archivo csv\n7-Mostrar Listas guardadas\n0-Cerrar\n")

    print("Adios")