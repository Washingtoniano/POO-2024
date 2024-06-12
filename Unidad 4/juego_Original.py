import tkinter as tk
from tkinter import *
from gameover import gameover
from tkinter import ttk,font
import time
#Utilizar Geometria grid
#pip install pygubu-designer
#pygubu-designer en la terminal para usar
from Gestor import gestor
from functools import partial
from manejador import manejador

#Modificar el tiempo e implementar la "animacion" de los canvas

#Esta ejecutando todo al mismo tiempo
class juego(tk.Tk):
    __gestor:manejador
    __puntos:int
    __lista=[]
    __segundos:int
    

    def __init__(self,man):
    
        self.__segundos=1000
        super().__init__()
        self.__puntaje=IntVar()
        self.__puntos=0

        self.__gestor=man
        self.__lista=[]

        self.fuente=font.Font(weight="normal")
        barramenu=Menu(self)
        menuPuntos=Menu(barramenu,tearoff=0)
        menuPuntos.add_command(label="Ver Puntajes",command=self.VerPuntos)
        menuPuntos.add_command(label="Salir",command=self.destroy)
        barramenu.add_cascade(label="Ver Puntajes",menu=menuPuntos)
        self.config(menu=barramenu)


        self.label_a=tk.Canvas(self,bg="#009000",relief=RAISED)
        self.label_b=tk.Canvas(self,bg="#ffff00",relief=RAISED)
        self.label_c=tk.Canvas(self,bg='#ff0000',relief=RAISED)
        self.label_d=tk.Canvas(self,bg='#0000ff',relief=RAISED)
        labelj=tk.Label(self,text=self.__gestor.getnombre())

        label=tk.Label(self,textvariable=self.__puntaje)
        #labelp=tk.Label(self,textvariable=self.__puntaje)
        labelc=ttk.Label(self)
        

        labelc.grid(column=0,row=1,columnspan=1,ipadx=10,ipady=10,sticky=NSEW)


        opts={'ipadx':50,'ipady':50,'sticky':'nswe'}
        #Convertir los botones con self
    
        label.grid(column=1,row=0,ipadx=5,ipady=5,sticky=NSEW)
        #labelp.grid(column=2,row=0,ipadx=5,ipady=5,sticky=NSEW)
        labelj.grid(column=0,row=0,ipadx=5,ipady=5,sticky=NSEW)




        
        self.label_a.grid(column=0,row=2,**opts)

        self.label_b.grid(column=0,row=3,**opts)

        self.label_c.grid(column=1,row=2,**opts)

        self.label_d.grid(column=1,row=3,**opts)
        
        
        
        
        botonC=tk.Button(self,text="Comenzar",command=partial(self.botones,opts))

        botonC.grid(column=0,columnspan=2,row=1,ipadx=10,ipady=10,sticky=NSEW)
        
        #self.mainloop()

        
    def setlista(self):
        self.__lista=[]
    def botones(self,opts):        
        self.boton_a=tk.Button(self,bg="#009000",relief=RAISED,command=partial(self.registrar,1))
        self.boton_b=tk.Button(self,bg="#ffff00",relief=RAISED,command=partial(self.registrar,2))
        self.boton_c=tk.Button(self,bg='#ff0000',relief=RAISED,command=partial(self.registrar,3))
        self.boton_d=tk.Button(self,bg='#0000ff',relief=RAISED,command=partial(self.registrar,4))
        
        self.boton_a.grid(column=0,row=2,**opts)
        self.boton_b.grid(column=0,row=3,**opts)
        self.boton_c.grid(column=1,row=2,**opts)
        self.boton_d.grid(column=1,row=3,**opts)
        #self.boton_a.bind(self.registrar,"<Button-1>")
        
        #self.boton_a.after(2000,self.change(),self.changeback())

        self.after(100,lambda:self.brillar())

    def sumar(self):

        self.__puntos+=1
        self.__gestor.setPuntos(self.__puntos)
        self.__puntaje.set(self.__puntos)

    def registrar(self,v):
        self.__lista.append(v)
        #self.sumar()
    def changeback(self,i):
        if i==1:
            self.boton_a.config(bg="#009000")
        elif i==2:
             self.boton_b.config(bg="#ffff00")
        elif i==3:
            self.boton_c.config(bg="#ff0000")
        else:
            self.boton_d.config(bg="#0000ff")
    def change(self,i):
        if i==1:
            self.boton_a.config(bg="#000000")
        elif i==2:
            self.boton_b.config(bg="#000000")
            
        elif i==3:
            self.boton_c.config(bg="#000000")
        else:
            self.boton_d.config(bg="#000000")
        self.after(200,lambda:self.changeback(i))




    def brillar(self):
        self.__lista=[]
        self.__gestor.iniciar()
        listaA=self.__gestor.getLista().getListad()
        self.__segundos=3000
        for el in listaA:
            self.__segundos+=300
        i=0
        self.secuencia(0,listaA)
    
    def secuencia(self,i,listaA):
        if i < (len(listaA)):
            self.after(200,lambda:self.change(listaA[i]))            
            #Utilizar sleep

            self.after(800,lambda:self.secuencia(self.aumentar(i),listaA))
        else:
            self.after(self.__segundos,lambda:self.__gestor.comprobar(self.__lista,self))
            #self.__gestor.comprobar(self.__lista,self)

    def aumentar(self,i):
        i+=1
        return i
    
    def VerPuntos(self):

        puntajes=Toplevel()
        puntajes.geometry("320x200")
        puntajes.resizable(width=False,height=False)
        puntajes.title("Galeria de Puntajes")
        fuente=font.Font(weight="normal")


        marco1=ttk.Frame(puntajes,padding=(10,10,10,10),relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)



        
        labelFecha=ttk.Label(marco1,text="Fecha",font=fuente)
        labelHora=ttk.Label(marco1,text="Hora",font=fuente)
        labelJugador=ttk.Label(marco1,text="Jugador",font=fuente)
        labelPuntaje=ttk.Label(marco1,text="Puntaje",font=fuente)
        op={"ipadx":2,"ipady":2,"sticky":"nswe"}
        labelFecha.grid(column=1,row=0,**op)
        labelJugador.grid(column=0,row=0,**op)
        labelPuntaje.grid(column=3,row=0,**op)
        labelHora.grid(column=2,row=0,**op)

        labelsPuntajes=self.__gestor.getJugadores()
        labelsPuntajes.ordenar()
        listas=labelsPuntajes.getLista()
        for i in range(len(listas)):
            labelnombre=ttk.Label(marco1,text=listas[i].getNombre())
            labelfecha=ttk.Label(marco1,text=listas[i].getFecha())
            labelhora=ttk.Label(marco1,text=listas[i].getHora())
            labelpuntos=ttk.Label(marco1,text=listas[i].getPuntos())
            
            
            
            labelnombre.grid(column=0,row=i+1,**op)
            labelfecha.grid(column=1,row=i+1,**op)
            labelhora.grid(column=2,row=i+1,**op)
            labelpuntos.grid(column=3,row=i+1,**op)
            
            


"""""
        for i in range (len(listas)):
            texto=listas[i]
            print(texto)
            juga=ttk.Label(self,text=str(texto),font=fuente,padding=(10,10))
"""""