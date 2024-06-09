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
        self.__gestor.iniciar()
        
        
        botonC=tk.Button(self,text="Comenzar",command=partial(self.botones,opts))

        botonC.grid(column=0,columnspan=2,row=1,ipadx=10,ipady=10,sticky=NSEW)
        
        self.mainloop()

        

    def botones(self,opts):        
        self.boton_a=tk.Button(self,bg="#009000",relief=RAISED,command=partial(self.sumar,10,1))
        self.boton_b=tk.Button(self,bg="#ffff00",relief=RAISED,command=partial(self.sumar,10,2))
        self.boton_c=tk.Button(self,bg='#ff0000',relief=RAISED,command=partial(self.sumar,10,3))
        self.boton_d=tk.Button(self,bg='#0000ff',relief=RAISED,command=partial(self.sumar,10,4))
        
        self.boton_a.grid(column=0,row=2,**opts)
        self.boton_b.grid(column=0,row=3,**opts)
        self.boton_c.grid(column=1,row=2,**opts)
        self.boton_d.grid(column=1,row=3,**opts)
        #self.boton_a.after(2000,self.change(),self.changeback())

        self.after(100,lambda:self.brillar())

    def sumar(self,d,v):

        self.__puntos+=d
        self.__gestor.setPuntos(self.__puntos)
        self.__puntaje.set(self.__puntos)
        self.registrar(v)
 

    def registrar(self,v):
        self.__lista.append(v)
        self.after(200,lambda:self.comprobar())
       
    def Darpuntos(self):
        return self.__puntos
    

    def changeback(self,d):
        if d==1:
            self.label_a.configure(relief=RAISED)
            self.label_a.configure(bg="#009000")
            self.boton_a.configure(relief=RAISED)
            self.boton_a.configure(bg="#009000")
        elif d==2:
            self.label_b.configure(relief=RAISED,bg="#ffff00")
            self.boton_b.configure(relief=RAISED,bg="#ffff00")
        elif d==3:
            self.label_c.configure(relief=RAISED,bg="#ff0000")
            self.boton_c.configure(relief=RAISED,bg="#ff0000")
        else: 
            self.label_d.configure(relief=RAISED,bg="#0000ff")
            self.boton_d.configure(relief=RAISED,bg="#0000ff")
        self.after(2000,lambda:self.registrar(d))
   
      
    
    def change(self,d):

        if d==1:
            self.label_a.configure(relief=GROOVE,bg="#000000")
            self.boton_a.configure(relief=GROOVE,bg="#000000")
        

        elif d==2:
            self.label_b.configure(relief=GROOVE,bg="#000000")
            self.boton_b.configure(relief=GROOVE,bg="#000000")
          
        elif d==3:
            self.label_c.configure(relief=GROOVE,bg="#000000")
            self.boton_c.configure(relief=GROOVE,bg="#000000")
          
        else: 
            self.label_d.configure(relief=GROOVE,bg="#000000")
            self.boton_d.configure(relief=GROOVE,bg="#000000")
           
        self.after(200,lambda:self.changeback(d))


    def comprobar(self):
        b=self.__gestor.comprobar(self.__lista)
        if b==0:
            
            self.gameover()
            print ("No igual")
        else:
            self.__lista=[]
            print ("Si igual")
            self.brillar()

    def brillar(self):
        lista=[]
        print(" estoy en comenzar")
        lista=self.__gestor.getLista().getListad()
        Ma=1
        i=0
        while i<len(lista):
            print("hOLA")
            if lista[i]==1: 
                self.label_a.after(200,lambda:self.change(1))
                
                
                print("hOLAsdhs")
            elif  lista[i]==2:
                self.label_b.after(200,lambda:self.change(2))            
                #self.boton_b.after(2000,self.__gestor.over())
                
            elif lista[i]==3:
                self.label_c.after(200,lambda:self.change(3))
                #self.boton_c.after(2000,self.__gestor.over())

            else:
                self.label_d.after(200,lambda:self.change(4))
                #self.boton_d.after(2000,self.__gestor.over())
                
            i+=1

    def gameover(self):
        self.destroy()

        