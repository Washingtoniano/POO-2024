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
            lis.agregar(uncalecactor)

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
    test(lis,json)
    unmenu.inicializar(lis,json)
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-\n 2-\n 3-\n 4-\n 5-\n 6-\n 7-\n 8\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,lis,json)
        op=input("Ingrese la opcion que desea\n 1-\n 2-\n 3-\n 4-\n 5-\n 6-\n 7-\n 8\n 0-Salir\n")

    print("Adios")    

    