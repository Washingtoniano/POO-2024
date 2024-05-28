import json
from pathlib import Path
class ObjectEncoder():
    def decodificarDIccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='lista':
                calefactores=d('Calefactores')
                dcalefactores=calefactores[0]
                lista=class_()
                for i in range(len(calefactores)):
                    dcalefactores=calefactores[i]
                    class__name=dcalefactores.pop('__class__')
                    class_=eval(class_name)
                    atributos=dcalefactores['__atributos__']
                    uncalefactor=class_(**atributos)
                    lista.agregar(uncalefactor)
                return lista
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open('w',encoding='UTF-8') as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
    def convertirTextoADiccionario(self,texto):
        return json.loads(texto)
