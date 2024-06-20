from flask import Flask,render_template, request,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
app=Flask(__name__)
app.config.from_pyfile("config.py")
#Los id se auto generan,(cuando se ingres un nuevo elemento su id sera el del anterior mas 1)
#db browser for sqlite
from models import db
from models import Sucursal,Repartidor,Transporte,Paquete
#sqlite3 Editor (Extension(yy0391))
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/repartidor")
def repartidor():
    return render_template("repartidor.html")

@app.route("/despachador",methods=['GET','POST'])
def despachador():
    if request.method=='POST':
        if not request.form['sucursales']:
            return render_template("despachador.html",sucursales=Sucursal.query.all(),sucursal_seleccionada=None)
        else:
            sucursal_seleccionada=Sucursal.query.get(request.form['sucursales'])
            session["sucursal"]=sucursal_seleccionada.id
           
            return render_template("despachador.html",sucursales=None,sucursal_seleccionada=Sucursal.query.get(request.form['sucursales']))      
    else:

        return render_template("despachador.html",sucursales=Sucursal.query.all(),sucursal_seleccionada=None)


"""""
@app.route("/registrar_llegada",methods=['POST','GET'])
def registrar_llegada():
#se pueden utilizar checkbox para enviar mas de un paquete o uno por uno.
    id=session["sucursal"]
    re
    if request.method=='POST':
        if not request.form['sucursales']:
            return render_template("registrar_llegada.html",sucursales=Sucursal.query.where(Sucursal.id!=session["sucursales"]),sucursal_seleccionada=None)
        elif request.form['sucursales'] and not request.form['paquete']:
            

            return render_template("registrar_llegada.html",sucursales=None,sucursal_seleccionada=Sucursal.query.get(request.form['sucursales']))
        if not request.form["paquete"] and request.form['sucursales']:
            return render_template("registrar_llegada.html",sucursales=None,sucursal_seleccionados=Sucursal.query.get(request.form['paquete']),paquetes=Paquete.query.where(Paquete.idsucursal==session["sucursal"] and Paquete.idrepartidor==0 and Paquete.entregado==False))
        else:
            sucu=Sucursal.query.get('sucursales')
            pa=Paquete.query.get('paquete')
            for p in pa:
                p.idsucursal=sucu.id
    
    else:
        return render_template("registrar_llegada.html",paquetes=Paquete.query.where(Paquete.idsucursal==session["sucursal"] and Paquete.idrepartidor==0),paquetes_seleccionados=None)





"""""
@app.route("/registrar_salida",methods=['POST','GET'])
def registrar_salida():
#se pueden utilizar checkbox para enviar mas de un paquete o uno por uno.
#No funciona: problemas con el if nor request.form["paquetes"] key error
    if request.method=='POST':
        if  not request.form['paquetes'] and not request.form['sucursales'] :
            return render_template("registrar_salida.html",paquetes=Paquete.query.where(Paquete.idsucursal==session["sucursal"] and Paquete.idrepartidor==0),paquetes_seleccionados=None,sucursales=Sucursal.query.where(Sucursal.id!=session["sucursal"]))
        else:
        
            for p in Transporte.query.all():
                num=p.numerotransporte
            paq=Paquete.query.get(request.form["paquetes"])
            suc=Sucursal.query.get(request.form["sucursales"])
            print(type(paq))
            print(type(suc))
            
            untransporte=Transporte(numerotransporte=num+1,idsucursal=request.form["sucursales"],idpaquete=request.form["paquetes"],fechahorasalida=datetime.now())
            db.session.add(untransporte)
            db.session.commit()
            return render_template("registar_salida.html",paquetes=None,paquetes_seleccionados=Paquete.query.get(request.form["paquetes"]),sucursales=None,sucursal_seleccionada=Sucursal.query.get(request.form["sucursales"]))
    

    else:
        return render_template("registrar_salida.html",paquetes=Paquete.query.where(Paquete.idsucursal==session["sucursal"] and Paquete.idrepartidor==0),paquetes_seleccionados=None,sucursales=Sucursal.query.where(Sucursal.id!=session["sucursal"]))
    
    

@app.route("/registrar_llegada",methods=["POST","GET"])
#solo cambiar el estado de entrega de verdadero a falso, y registrar la hora actual
def registrar_llegada():
    if request.method=='POST':
        if not request.form['paquetes']:
            return render_template("registrar_llegada.html",transportes= Transporte.query.where(Transporte.idsucursal==session["sucursal"] and Transporte.fechahorasalida==''),paquetes=Paquete.query.where(Paquete.idsucursal==session["sucursal"]))
        else:

                paquete=Paquete.query.get(request.form['paquetes'])
                transporte=Transporte.query.get(request.form['transportes'])
                paquete.entregado=True
        
                transporte.query.update(fechahorallegada=datetime.now())
                paquete.query.update(entregado=True)
                
                db.session.refresh()
                return render_template(paquetes=None,transporte=None,transporte_seleccionado=Transporte.query.get(request.form['transportes']),paquete_seleccionado=Paquete.query.get(request.form['paquetes']))

    else:
        return render_template("registrar_llegada.html",transportes= Transporte.query.where(Transporte.idsucursal==session["sucursal"]),paquetes=Paquete.query.where(Paquete.idsucursal==session["sucursal"]))

@app.route("/registrar_paquete",methods=['GET','POST'])
def registrar_paquete():
    try:
        if request.method=='POST':
            if not request.form['nombre'] or not request.form['peso'] or not request.form['direccion']:
                return render_template('error.html',error="Los datos ingresados no son correctos...")
            else:
                paquetes=Paquete.query.all()
                for p in paquetes:
                    num=p.numeroenvio
                nuevoPaquete=Paquete(nomdestinatario=request.form['nombre'],peso=request.form['peso'],dirdestinatario=request.form['direccion'],entregado=False,idrepartidor=0,idtransporte=0,idsucursal=session["sucursal"],numeroenvio=num+20,observaciones='')
                print(nuevoPaquete)
                db.session.add(nuevoPaquete)
                db.session.commit()#Usar try en el commit para verificar exito o fracaso
        
                return render_template("menudespachador.html")
        return render_template("registrar_paquete.html")
    except:
        return render_template("error.html",error="Hubo un error al cargar el paquete")




if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
