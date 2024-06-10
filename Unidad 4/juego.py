import tkinter as tk
from tkinter import *
from gameover import gameover
from tkinter import ttk
import time
#Utilizar Geometria grid
#pip install pygubu-designer
#pygubu-designer en la terminal para usar
from Gestor import gestor
from functools import partial
from manejador import manejador

#Modificar el tiempo e implementar la "animacion" de los canvas

#Esta ejecutando todo al mismo tiempo
import numpy as np
class juego(tk.Tk):
    __gestor:manejador
    __puntos:int
    __lista=[]
    __segundos:int
    

    def __init__(self,man):
    
        self.__segundos=500
        super().__init__()
        self.__puntaje=IntVar()
        self.__puntos=0

        
        self.__lista=[]

       
        self.label_a=tk.Canvas(self,bg="#009000",relief=RAISED)
        self.label_b=tk.Canvas(self,bg="#ffff00",relief=RAISED)
        self.label_c=tk.Canvas(self,bg='#ff0000',relief=RAISED)
        self.label_d=tk.Canvas(self,bg='#0000ff',relief=RAISED)


        label=tk.Label(self,text="Puntaje")
        labelp=tk.Label(self,textvariable=self.__puntaje)
        labelc=ttk.Label(self)
        

        labelc.grid(column=0,row=1,columnspan=1,ipadx=10,ipady=10,sticky=NSEW)


        opts={'ipadx':50,'ipady':50,'sticky':'nswe'}
        #Convertir los botones con self
    
        label.grid(column=0,row=0,ipadx=10,ipady=10,sticky=NSEW)
        labelp.grid(column=1,row=0,ipadx=10,ipady=10,sticky=NSEW)




        
        self.label_a.grid(column=0,row=2,**opts)

        self.label_b.grid(column=0,row=3,**opts)

        self.label_c.grid(column=1,row=2,**opts)

        self.label_d.grid(column=1,row=3,**opts)
        
        
        self.__gestor=man
        
        
        botonC=tk.Button(self,text="Comenzar",command=partial(self.botones,opts))

        botonC.grid(column=0,columnspan=2,row=1,ipadx=10,ipady=10,sticky=NSEW)
        
        self.mainloop()

        
    def setlista(self):
        self.__lista=[]
    def botones(self,opts):        
        self.boton_a=tk.Button(self,bg="#009000",relief=RAISED,command=partial(self.sumar,10,1))
        self.boton_b=tk.Button(self,bg="#ffff00",relief=RAISED,command=partial(self.sumar,10,2))
        self.boton_c=tk.Button(self,bg='#ff0000',relief=RAISED,command=partial(self.sumar,10,3))
        self.boton_d=tk.Button(self,bg='#0000ff',relief=RAISED,command=partial(self.sumar,10,4))
        
        self.boton_a.grid(column=0,row=2,**opts)
        self.boton_b.grid(column=0,row=3,**opts)
        self.boton_c.grid(column=1,row=2,**opts)
        self.boton_d.grid(column=1,row=3,**opts)
        #self.boton_a.bind(self.registrar,"<Button-1>")
        
        #self.boton_a.after(2000,self.change(),self.changeback())

        self.after(100,lambda:self.brillar())

    def sumar(self,d,v):

        self.__puntos+=d
        self.__gestor.setPuntos(self.__puntos)
        self.__puntaje.set(self.__puntos)
        self.registrar(v)

    def registrar(self,v):
        self.__lista.append(v)

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
        band=False
        for el in listaA:
            self.__segundos+=500
        i=0
        while i<len(listaA):
            #self.after(100,lambda:self.change(listaA[i]))
            self.change(listaA[i])
            #print(listaA[i])
            i+=1
            #self.after(150,lambda:self.aumentar(i))
        self.after(self.__segundos,lambda:self.__gestor.comprobar(self.__lista,self))
    def aumentar(self,i):
        i+=1
        return i
        
        


