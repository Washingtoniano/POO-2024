from flask import Flask
from flask import render_template, request
import datetime as date
app=Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def inicio():
    if request.method=='POST':
        if request.form['usuario'] and request.form['password']:
            datos=request.form
            return render_template("menu.html")

@app.route('/menu',methods = ['POST', 'GET'])
def menu():


    print("Ingrese la opcion que desea\n")
    op=(input(" 1-\n 2-\n 3\n 4\n 5\n 6\n 7\n"))
    return render_template("index.html")
@app.route('/Saludo')
def saludo():
    return (render_template('inicio.html'))
if __name__ =='__main__':
    app.run(debug=True)