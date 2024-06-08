from menu import menu
from Lista import lista
from objectoencoder import ObjectEncoder
import csv
from CalefactorE import calefactorE
from CalefactorG import calefactorG

def test(lis,json):
    archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 6\\calefactores.csv",'r')
    reader=csv.reader(archivo,delimiter=';')
    band=False
    for fila in reader:
        if band==False:
            band=True
        else:
            if len(fila)==8:
                uncalecactor=calefactorE(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
            else:
                uncalecactor=calefactorG(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
            lis.AgregarElemento(uncalecactor)

    lis.mostrar()
    listado=[]
    for dato in lis:
        listado.append(dato)
    d=lis.tojason()
    json.guardarJSONArchivo(d,"C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 6\\calefactores.json")


if __name__ =='__main__':
    unmenu=menu()
    lis=lista()
    json=ObjectEncoder()
    #test(lis,json)
    d=json.leerJSONArchivo("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 6\\calefactores.json")
    lis=json.decodificarDIccionario(d)
    #unmenu.inicializar(lis,json)
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Insertar en una posicion determinada\n 2-Agregar un elemento\n 3-Tipo de una posicion\n 4-Calefactor de menor precio\n 5-Buscar marca de calefactores electricos\n 6-Mostrar Calefactores en promocion\n 7-Guardar JSON\n 8-Mostrar\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,lis,json)
        op=input("Ingrese la opcion que desea\n 1-Insertar en una posicion determinada\n 2-Agregar un elemento\n 3-Tipo de una posicion\n 4-Calefactor de menor precio\n 5-Buscar marca de calefactores electricos\n 6-Mostrar Calefactores en promocion\n 7-Guardar JSON\n 8-Mostrar\n 0-Salir\n")

    print("Adios")    

    