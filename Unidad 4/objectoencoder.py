import json
from pathlib import Path
from manejador import manejador
from puntaje import puntaje
class objectencoder:
    __pathArchivo=object
    def __init__(self,patharchivo) -> None:
        self.__pathArchivo=patharchivo

    def decodificar(self,d):
        if __class__ not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            
            if class_name =='manejador':
                puntos=d['puntaje']
                manejador=class_()
                for i in range(len(puntos)):
                    dpuntos=puntos[i]
                    class_name=dpuntos.pop('__class__')
                    clas_=eval(class_name)
                    atributos=dpuntos['__atributos__']
                    unpuntaje=class_(**atributos)
                    manejador.agregar(unpuntaje)
        return manejador
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
                