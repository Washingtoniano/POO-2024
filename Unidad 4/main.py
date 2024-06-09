from juego import juego
from inicio import inicio
from objectoencoder import objectencoder
from jugador import Jugador

from gestorJugadores import gestorJugadores
from manejador import manejador
from gameover import gameover

import csv

def testarchivo(obj):
    ungestor=gestorJugadores()
    arhvivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 4\\archivo.csv",'r')
    reader=csv.reader(arhvivo,delimiter=';')
    band=False
    for fila in reader:
        if band==False:
            band=True
        else:
            unjugador=Jugador(Jugador=fila[0],Puntaje=fila[3])
            ungestor.agregar(unjugador)
    d=ungestor.tojson()
    obj.guardarJSONArchivo(d)

def testapp():
    mi_app=inicio()
    mi_app.mainloop()


def main():
    unobjecto=objectencoder("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 4\\pysimonpuntajes.json")
    uninicio=inicio()
    nom=uninicio.darNombre()
    
    ungestorJ=gestorJugadores()
    d=unobjecto.leerJSONArchivo()
    ungestorJ=(unobjecto.decodificar(d))
    unmanejador=manejador(nom)
    unmanejador.ejecutar()
    ungameover=gameover(unmanejador.getPuntos())
    #unpunto=Jugador(Jugador=unmanejador.getnombre(),Puntaje=unmanejador.getPuntos())
    #ungestorJ.agregar(unpunto)
    #d=ungestorJ.tojson()
    #unobjecto.guardarJSONArchivo(d)
    
    print("P")
    
    print("a")
    
    

if __name__ == '__main__':
    #unmanejador=manejador()
    #unmanejador.iniciar()

    #un=objectencoder("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 4\\pysimonpuntajes.json")
    #testarchivo(un)
    main()