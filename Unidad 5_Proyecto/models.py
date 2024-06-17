from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)
class paquete(db.Model):
    __tablename__="paquete"
    __id=db.Column(db.Integer,primary_key=True)
    __numero=db.Column(db.Integer,primary_key=True)
    __peso=db.Column(db.Integer,primary_key=True)
    __NombreD=db.Column(db.String(60),primary_key=True)
    __DireccionD=db.Column(db.String(100),primary_key=True)
    __Entregado=db.Column(db.Boolean,primary_key=True)
    __observacion=db.Column(db.Text,primary_key=True)
    __idSucursal=db.relationship("sucursal",backref="paquete")
    __idTransporte=db.relationship("transporte",backref="paquete")
    __idRepartior=db.relationship("repartidor",backref="paquete")

    def getNumero(self):
        return self.__numero
    def getPeso(self):
        return self.__peso
    def getNombreD(self):
        return self.__NombreD
    def getDireccionD(self):
        return self.__DireccionD
    def getEntregado(self):
        return self.__Entregado
    def getObservacion(self):
        return self.__observacion
    def getRepartidor(self):
        return self.__Repartidor


 


class repartidor(db.Model):
    __tablename__="repartidor"
    __id=db.Column(db.Integer,primary_key=True)
    __numero=db.Column(db.Integer,primary_key=True)
    __nombre=db.Column(db.String(60),primary_key=True)
    __dni=db.Column(db.String(8),primary_key=True)
    __iSucursal=db.relationship("sucursal",backref="repartidor")
    __paquete=db.relationship("paquete",backref="repartidor")

    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__dni
    def getPaquete(self):
        return self.__paquete
    def getSucursal(self):
        return self.__sucursal


class sucursal(db.Model):
    __tablename__ ="sucursal"
    __id=db.Column(db.Integer,primary_key=True)
    __numero=db.Column(db.Integer,primary_key=True)
    __provincia=db.Column(db.String(30),primary_key=True)
    __localidad=db.Column(db.String(30),primary_key=True)
    __direccion=db.Column(db.String(30),primary_key=True)
    __paquetes=db.relationship("paquete",backref="sucursal")
    __repartidor=db.relationship("repartidor",backref="sucursal")
    __transporte=db.relationship("transporte",backref="sucursal")


    def getNumero(self):
        return self.__numero
    def getProvincia(self):
        return self.__provincia
    def getLocalidad(self):
        return self.__localidad
    def getDireccion(self):
        return self.__direccion
    def getRep(self):
        return self.__repartidor
    def getPa(self):
        return self.__paquetes
    def getTrans(self):
        return self.__transporte

   
class transporte(db.Model):
    __tablename__ ="transporte"
    __id=db.Column(db.Integer,primary_key=True)
    __numero=db.Column(db.Integer,primary_key=True)
    __fechaS=db.Column(db.DATETIME,primary_key=True)
    __fechaLL=db.Column(db.DATETIME,primary_key=True)
    __sucursal=db.relationship("sucursal",backref="transporte")
    __paquete=db.relationship("paquete",backref="transporte")



    def getNumero(self):
        return self.__numero
    def getFechaL(self):
        return self.__fechaLL
    def getFechaS(self):
        return self.__fechaS
    def getPaquete(self):
        return self.__paquete
    def getSucursal(self):
        return self.__sucursal
    
 
