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
           
            return render_template("menudespachador.html")
    else:

        return render_template("despachador.html",sucursales=Sucursal.query.all(),sucursal_seleccionada=None)


@app.route("/menudespachador")
def menudespachador():
    return render_template ("menudespachador.html")
@app.route("/registrar_salida",methods=['POST','GET'])
def registrar_salida():
#se pueden utilizar checkbox para enviar mas de un paquete o uno por uno.
#No funciona: problemas con el if nor request.form["paquetes"] key error
    try: 
        if request.method=='POST':
            if  not request.form['paquetes'] and not request.form['sucursales'] :
                return render_template("registrar_salida.html",paquetes=Paquete.query.filter(Paquete.idsucursal==session["sucursal"], Paquete.idrepartidor==0 , Paquete.entregado==False),paquetes_seleccionados=None,sucursales=Sucursal.query.filter(Sucursal.id!=session["sucursal"]))
            else:
                    for t in Transporte.query.all():
                        num=t.numerotransporte
                    paq=request.form.getlist("paquetes")
                    suc=Sucursal.query.get(request.form["sucursales"])
                    print(type(paq))
                    print(type(suc))
                    idpac=[]
                    untransporte=Transporte(numerotransporte=num+1,idsucursal=suc.id,fechahorasalida=datetime.now())
                    db.session.add(untransporte)
                    for p in paq:
                        unpaquete=Paquete.query.get(p)
                        unpaquete.idtransporte=untransporte.id
                        unpaquete.idsucursal=suc.id
                        idpac.append(unpaquete)
                    untransporte.idpaquete=idpac
        
                    db.session.commit()
                                    
                    return render_template("exito.html",exito="Se cargo un paquete")
               
            
        else:
            return render_template("registrar_salida.html",paquetes=Paquete.query.filter(Paquete.idsucursal==session["sucursal"], Paquete.idrepartidor==0),paquetes_seleccionados=None,sucursales=Sucursal.query.filter(Sucursal.id!=session["sucursal"]))
    except:
            if request.form['sucursales']:
                        return render_template("error.html",error="No hay paquetes")
            else:
                return render_template("error.html",error="No se pudo registrar la salida")
    

@app.route("/registrar_llegada",methods=["POST","GET"])
#solo cambiar el estado de entrega de verdadero a falso, y registrar la hora actual
def registrar_llegada():
    try:
        if request.method=='POST':
            if not request.form['transportes']:
                return render_template("registrar_llegada.html",transportes= Transporte.query.filter(Transporte.idsucursal==session["sucursal"], Transporte.fechahorallegada==None) )
            else:
                    transporte=Transporte.query.get(request.form['transportes'])
                    transporte.fechahorallegada=datetime.now()
                    
                    db.session.commit()
                    return render_template("exito.html",exito="Se registro su llegada")
               

        else:
                return render_template("registrar_llegada.html",transportes= Transporte.query.filter(Transporte.idsucursal==session["sucursal"], Transporte.fechahorallegada==None) )
    except:
            
                return render_template("error.html",error="No hay transportes")

    

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
