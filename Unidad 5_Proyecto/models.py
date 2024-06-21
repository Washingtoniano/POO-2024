from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)
class Paquete(db.Model):
    __tablename__="paquete"
    id=db.Column(db.Integer,primary_key=True)
    numeroenvio=db.Column(db.Integer,nullable=False)
    peso=db.Column(db.Integer)
    nomdestinatario=db.Column(db.String(60),nullable=False)
    dirdestinatario=db.Column(db.String(100),nullable=False)
    entregado=db.Column(db.Boolean)
    observaciones=db.Column(db.Text)
    idsucursal=db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    idtransporte=db.Column(db.Integer,db.ForeignKey('transporte.id'))
    idrepartidor=db.Column(db.Integer,db.ForeignKey('repartidor.id'))

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
 


class Repartidor(db.Model):
    __tablename__="repartidor"
    id=db.Column(db.Integer,primary_key=True)
    numero=db.Column(db.Integer,nullable=False)
    nombre=db.Column(db.String(60),nullable=False)
    dni=db.Column(db.String(8),nullable=False)
    iSucursal=db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    paquete=db.relationship('Paquete',backref='repartidor')

    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__dni


class Sucursal(db.Model):
    __tablename__ ="sucursal"
    id=db.Column(db.Integer,primary_key=True)
    numero=db.Column(db.Integer,nullable=False)
    provincia=db.Column(db.String(30),nullable=False)
    localidad=db.Column(db.String(30),nullable=False)
    direccion=db.Column(db.String(30),nullable=False)
    idpaquetes=db.relationship("Paquete",backref="sucursal")
    idrepartidor=db.relationship("Repartidor",backref="sucursal")

    idtransporte=db.relationship("Transporte",backref="sucursal")

    def getNumero(self):
        return self.__numero
    def getProvincia(self):
        return self.__provincia
    def getLocalidad(self):
        return self.__localidad
    def getDireccion(self):
        return self.__direccion
    def getid(self):
        return self.__id
 
   
class Transporte(db.Model):
    __tablename__ ="transporte"
    id=db.Column(db.Integer,primary_key=True)
    numerotransporte=db.Column(db.Integer,nullable=False)
    fechahorasalida= db.Column(db.DateTime)

    fechahorallegada=db.Column(db.DateTime)

    idsucursal=db.Column(db.Integer,db.ForeignKey('sucursal.id'))

    #idpaquete=db.relationship("Paquete",backref="transporte")



    def getNumero(self):
        return self.__numero
    def getFechaL(self):
        return self.__fechaLL
    def getFechaS(self):
        return self.__fechaS
 
    
 
