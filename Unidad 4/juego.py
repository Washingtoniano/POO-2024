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
    __lista=[]

    def __init__(self,man):
    

        super().__init__()
        self.__puntaje=IntVar()
        self.__puntos=0

      
        self.__lista=[]

       
        self.label_a=tk.Canvas(self,relief=FLAT,bg="#009000")
        self.label_b=tk.Canvas(self,relief=RAISED,bg="#ffff00")
        self.label_c=tk.Canvas(self,relief=SUNKEN,bg='#ff0000')
        self.label_d=tk.Canvas(self,relief=GROOVE,bg='#0000ff')


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
        self.__gestor.iniciar()
        
        
        botonC=tk.Button(self,text="Comenzar",command=partial(self.botones,opts))

        botonC.grid(column=0,columnspan=2,row=1,ipadx=10,ipady=10,sticky=NSEW)
        
        self.mainloop()

        

    def botones(self,opts):        
        self.boton_a=tk.Button(self,bg="#009000",command=partial(self.sumar,10,1))
        self.boton_b=tk.Button(self,bg="#ffff00",command=partial(self.sumar,10,2))
        self.boton_c=tk.Button(self,bg='#ff0000',command=partial(self.sumar,10,3))
        self.boton_d=tk.Button(self,bg='#0000ff',command=partial(self.sumar,10,4))
        
        self.boton_a.grid(column=0,row=2,**opts)
        self.boton_b.grid(column=0,row=3,**opts)
        self.boton_c.grid(column=1,row=2,**opts)
        self.boton_d.grid(column=1,row=3,**opts)

        self.after(1000,self.brillar())

    def sumar(self,d,Boton):

        self.__puntos+=d
        self.__gestor.setPuntos(self.__puntos)
        self.__puntaje.set(self.__puntos)
        self.registrar(Boton)

    def registrar(self,v):
        self.__lista.append(v)
       
    def Darpuntos(self):
        return self.__puntos
    


    
    


    def brillar(self):
        print(" estoy en comenzar")
        lista=self.__gestor.getLista()
        Ma=1
        i=0
        while i<len(lista):
            print("hOLA")
            if Ma==1: 
                self.label_a.configure(bg='#000000')
                self.after(2000,self.label_a.configure(bg="#009000"))
                #self.boton_a.configure(bg='#009000')
                print("hOLAsdhs")
            elif  lista[i]==2:
                self.boton_b.configure(bg='#000000')                
                self.after(2000)
                self.boton_b.configure(bg="#ffff00")                
                #self.boton_b.after(2000,self.__gestor.over())
                
            elif lista[i]==3:
                self.boton_c.configure(bg='#000000')                
                self.after(2000)
                self.boton_c.configure(bg="#ff0000")
                #self.boton_c.after(2000,self.__gestor.over())

            else:
                self.boton_d.configure(bg='#000000')
                self.after(2000)
                self.boton_d.configure(bg="#0000ff")
                #self.boton_d.after(2000,self.__gestor.over())

            i+=1
        self.after(10000)
        b=self.__gestor.comprobar(self.__lista)
        if b==0:
            print ("No igual")
        else:
            print ("Si igual")
        