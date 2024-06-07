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

class juego(tk.Tk):
    __gestor:manejador
    __puntos:int
    lista=[]

    def __init__(self,man):
    

        super().__init__()
        self.__puntaje=IntVar()
        self.__puntos=0

      
        self.lista=[]

       
        self.label_a=tk.Canvas(self,relief=FLAT,bg="#009000")
        self.label_b=tk.Canvas(self,relief=RAISED,bg="#ffff00")
        self.label_c=tk.Canvas(self,relief=SUNKEN,bg='#ff0000')
        self.label_d=tk.Canvas(self,relief=GROOVE,bg='#0000ff')

        self.boton_a=tk.Button(self,bg="#009000",command=partial(self.sumar,10,1))
        self.boton_b=tk.Button(self,bg="#ffff00",command=partial(self.sumar,10,2))
        self.boton_c=tk.Button(self,bg='#ff0000',command=partial(self.sumar,10,3))
        self.boton_d=tk.Button(self,bg='#0000ff',command=partial(self.sumar,10,4))
        label=tk.Label(self,text="Puntaje")
        labelp=tk.Label(self,textvariable=self.__puntaje)
        labelc=ttk.Label(self)
        

        labelc.grid(column=0,row=1,columnspan=1,ipadx=10,ipady=10,sticky=NSEW)
 

        

        

        opts={'ipadx':50,'ipady':50,'sticky':'nswe'}
        #Convertir los botones con self
    
        label.grid(column=0,row=0,ipadx=10,ipady=10,sticky=NSEW)
        labelp.grid(column=1,row=0,ipadx=10,ipady=10,sticky=NSEW)




        self.label_a.grid(column=0,row=2,**opts)
        self.boton_a.grid(column=0,row=2,**opts)

        self.label_b.grid(column=0,row=3,**opts)
        self.boton_b.grid(column=0,row=3,**opts)

        self.label_c.grid(column=1,row=2,**opts)
        self.boton_c.grid(column=1,row=2,**opts)

        self.label_d.grid(column=1,row=3,**opts)
        self.boton_d.grid(column=1,row=3,**opts)
        
        
        self.__gestor=man
        self.__gestor.iniciar()
        botonC=ttk.Button(self,text="Comenzar",command=self.brillar(self.__gestor.getLista()))

        botonC.grid(column=0,columnspan=2,row=1,ipadx=10,ipady=10,sticky=NSEW)



    def sumar(self,d,Boton):
        self.__puntos+=d
        self.__puntaje.set(self.__puntos)
        self.registrar(Boton)

    def registrar(self,v):
        self.lista.append(v)
    def Darpuntos(self):
        return self.__puntos
    


    def change_back(self,d):
        if d==1:
            self.boton_a.configure(bg='#009000')
        elif d==2:
            self.boton_b.configure(bg="#ffff00")
        elif d==3:
            self.boton_c.configure(bg="#ff0000")
        else:
            self.boton_d.configure(bg="#0000ff")
    
    
    
    
    def change(self,d):
        if d==1:
            self.boton_a.configure(bg='#000000')
            self.boton_a.after(2000,self.change_back(d))
            #self.boton_a.after(200,self.__gestor.over())
        elif d==2:
            self.boton_b.configure(bg='#000000')
            self.boton_b.after(2000,self.change_back(d))
            #self.boton_b.after(200,self.__gestor.over())
        elif d==3:
            self.boton_c.configure(bg='#000000')
            self.boton_c.after(2000,self.change_back(d))
            #self.boton_c.after(200,self.__gestor.over())
        else:
            self.boton_d.configure(bg='#000000')
            self.boton_d.after(2000,self.change_back(d))
            #self.boton_d.after(200,self.__gestor.over())



    def brillar(self,li):
        lista=li
        Ma=1
        i=0
        while i<len(lista):
            print("hOLA")
            if lista[i]==1: 
                self.change(1)
                print("hOLAsdhs")
            elif  lista[i]==2:
                self.change(2)
                #self.boton_b.after(2000,self.__gestor.over())
                
            elif lista[i]==3:
                self.change(3)
                self.boton_c['bg']="#000000"
                #self.boton_c.after(2000,self.__gestor.over())

            else:
                self.change(4)
                self.boton_d['bg']="#000000"    
                #self.boton_d.after(2000,self.__gestor.over())

            i+=1
        b=self.__gestor.comprobar(self.lista)