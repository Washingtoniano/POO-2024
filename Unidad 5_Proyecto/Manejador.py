from Gestor_repartidor import GestorRepartidor
from Gestor_Sucursal import GestorSucur 
from GestorPaquete import GestorPaquete
from interfaz import IDespachador
from zope.interface import implementer
from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

@implementer (IDespachador)
class manejador():
    __paquetes:object
    __sucursales:object
    __repartidores:object

    def __init__(self) -> None:
        self.__paquetes=GestorPaquete(db.Model)
        self.__repartidores=GestorRepartidor(db.Model)
        self.__sucursales=GestorSucur(db.Model)


    def menu_des(self):
        op=input("1-")
