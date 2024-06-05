from menu import menu
from lista import lista
from ObjectENcoder import ObjectEncoder
from Docente import docente
from Apoyo import apoyo
from Docente_Investigador import docente_investigador
from Investigador import investigador
import csv
def test(unalista,unobject):
    archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 7\\Personal.csv",'r')
    reader=csv.reader(archivo,delimiter=';')
    band=False
    for fila in reader:
        if band==False:
            band=True
        else:
            if len(fila)==6:
                unpersonal=apoyo(cuil=fila[0],apellido=fila[1],nombre=fila[2],sueldo=fila[3],antiguedad=fila[4],categoria=fila[5])
            elif len(fila)==8:
                unpersonal=docente(cuil=fila[0],apellido=fila[1],nombre=fila[2],sueldo=fila[3],antiguedad=fila[4],carrera=fila[5],cargo=fila[6],catedra=fila[7])

            elif len(fila)==7:
                unpersonal=investigador(cuil=fila[0],apellido=fila[1],nombre=fila[2],sueldo=fila[3],antiguedad=fila[4],area=fila[5],tipo=fila[6])

            else:
                unpersonal=docente_investigador(cuil=fila[0],apellido=fila[1],nombre=fila[2],sueldo=fila[3],antiguedad=fila[4],carrera=fila[5],cargo=fila[6],catedra=fila[7],area=fila[8],tipo=fila[9],categoria=fila[10],importeextra=fila[11])


            unalista.AgregarElemento(unpersonal)
    d=unalista.tojson()
    unobject.GuardarArchivo(d,"C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 7\\Personal.json")
    

if __name__ == '__main__':
    unalista=lista()
    unobject=ObjectEncoder()
    unmenu=menu()
    #test(unalista,unobject)
    unmenu.inicializar(unalista,unobject)
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Insertar en una posicion determinada\n 2-Agregar un elemento\n 3-Tipo de una posicion\n 4-Buscar por carrera\n 5-Mostrar cant. de un area\n 6-\n 7-Mostrar importe extra de una categoria\n 8-Guardar Json\n 9-Mostrar Datos\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,unalista,unobject)
        op=input("Ingrese la opcion que desea\n 1-Insertar en una posicion determinada\n 2-Agregar un elemento\n 3-Tipo de una posicion\n 4-Buscar por carrera\n 5-Mostrar cant. de un area\n 6-\n 7-Mostrar importe extra de una categoria\n 8-Guardar Json\n 9-Mostrar Datos\n 0-Salir\n")

    print("Adios")    
