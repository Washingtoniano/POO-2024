from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config.from_pyfile("config.py")
#Los id se auto generan,(cuando se ingres un nuevo elemento su id sera el del anterior mas 1)
#db browser for sqlite
from models import db
from models import Sucursal,Repartidor,Transporte,Paquete
@app.route("/repartidor")
def repartidor():
    return render_template("repartidor.html")

@app.route("/despachador",methods=['GET','POST'])
def despachador():
    if request.method=='POST':
        if not request.form['sucursales']:
            return render_template("despachador.html",sucursales=Sucursal.query.all(),sucursal_seleccionada=None)
        else:
            return render_template("despachador.html",sucursales=None,sucursal_seleccionada=Sucursal.query.get(request.form['sucursales']))
    else:
        return render_template("despachador.html",sucursales=Sucursal.query.all(),sucursal_seleccionada=None)

@app.route("/menu",methods=['GET','POST'])
def menu():
    return render_template("menudespachador.html")
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/registrar_llegada")
def registrar_llegada():
    return render_template("registrar_llegada.html")

@app.route("/registrar_salida")
def registrar_salida():
    return render_template("registrar_salida.html")

@app.route("/registrar_paquete")
def registrar_paquete():
    return render_template("registrar_paquete.html")




if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)