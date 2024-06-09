import json
from pathlib import Path
#from manejador import manejador

#El json solo necesita la clase puntos(ahora llamada jugador)
class objectencoder:
    __pathArchivo=object
    def __init__(self,patharchivo) -> None:
        self.__pathArchivo=patharchivo

    def decodificar(self,d):


        if "__class__" not in d:
            return d
        else:
            from gestorJugadores import gestorJugadores
            from jugador import Jugador
            class_name=d['__class__']
            class_=eval(class_name)
            
            if class_name =='gestorJugadores':
                jugador=d['Jugador']
                gestorJugadores=class_()
                for i in range(len(jugador)):
                    djugador=jugador[i]
                    class_name=djugador.pop('__class__')
                    class_=eval(class_name)
                    atributos=djugador['__atributos__']
                    unpuntaje=class_(**atributos)
                    gestorJugadores.agregar(unpuntaje)
        return gestorJugadores
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
                