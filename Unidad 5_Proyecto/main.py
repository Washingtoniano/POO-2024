from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config.from_pyfile("config.py")
#Los id se auto generan,(cuando se ingres un nuevo elemento su id sera el del anterior mas 1)
#db browser for sqlite
from models import sucursal,repartidor,transporte,paquete
from models import db
@app.route("/")
def saludo():
    return render_template("index.html")



if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)