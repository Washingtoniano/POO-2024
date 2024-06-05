from juego import juego
from inicio import inicio
from objectoencoder import objectencoder
from puntaje import puntaje
from manejador import manejador
import csv

def testarchivo(obj):
    
    arhvivo=open("archivo.csv",'r')
    lista=[]
    reader=csv.reader(arhvivo,delimiter=';')
    band=False
    for fila in reader:
        if band==False:
            band=True
        else:
            unjugador=puntaje(Puntaje=fila[3])
            lista.append(unjugador)
    obj.guardarJSONArchivo(lista)

def testapp():
    mi_app=inicio()
    mi_app.mainloop()
def main():
    obj=objectencoder("pysimonpuntajes.json")
    unmanejador=manejador()

if __name__ == '__main__':
    #unmanejador=manejador()
    #unmanejador.inicio()

    #un=objectencoder("pysimonpuntajes.json")
    #testarchivo(un)
    main()