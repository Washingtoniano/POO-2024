from pathlib import Path
import json

class ObjectEncoder():
    def GuardarArchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def DecodificarArchivo(self,d):
        if '__class__' not in  d:
            return d
        else:
            from lista import lista
            from Docente import docente
            from Docente_Investigador import docente_investigador
            from Apoyo import apoyo
            from Investigador import investigador
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='lista':
                personal=d['Personal']
                dPersonal=personal[0]
                lista=class_()
                for i in range(len(personal)):
                    dPersonal=personal[i]
                    class_name=dPersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersonal['__atributos__']
                    unpersonal=class_(**atributos)
                    lista.AgregarElemento(unpersonal)
                return lista
    def LeerArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8")as fuente:
            diccionario=json.load(fuente)
            fuente.close
            return diccionario
    def ConvertirTextoADiccionario(self,text):
        return json.loads(text)