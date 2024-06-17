from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

class GestorSucur():
    __lista:list
    def __init__(self) -> None:
        self.__lista=[]
    def agregar(self,dato):
        self.__lista.append(dato)

