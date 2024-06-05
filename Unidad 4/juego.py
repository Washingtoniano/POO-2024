import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
#Utilizar Geometria grid
#pip install pygubu-designer
#pygubu-designer en la terminal para usar 
from functools import partial

class juego(tk.Tk):
    __ventana=object
    __puntajeM:object
    __puntaje:object
    __puntos:int
    def __init__(self):
        #self.__ventana=Tk()
        #self.__puntajeM=StringVar()
        #mainframe=ttk.Frame(self.__ventana,padding="5 5 12 5")
        super().__init__()
        self.__puntaje=IntVar()
        self.__puntos=0

      
        label=tk.Label(self,text="Puntaje")
        labelp=tk.Label(self,textvariable=self.__puntaje)
        #labelp=ttk.Label(mainframe,textvariable=)
        label_a=tk.Canvas(self,bg="#009000")
        label_b=tk.Canvas(self,bg="#ffff00")
        label_c=tk.Canvas(self,bg='#ff0000')
        label_d=tk.Canvas(self,bg='#0000ff')

        boton_a=tk.Button(self,bg="#009000",command=partial(self.sumar,10))
        boton_b=tk.Button(self,bg="#ffff00",command=partial(self.sumar,10))
        boton_c=tk.Button(self,bg='#ff0000',command=partial(self.sumar,10))
        boton_d=tk.Button(self,bg='#0000ff',command=partial(self.sumar,10))

        opts={'ipadx':50,'ipady':50,'sticky':'nswe'}
    
        label.grid(column=0,row=0,ipadx=10,ipady=10,sticky=NSEW)
        labelp.grid(column=1,row=0,ipadx=10,ipady=10,sticky=NSEW)
        label_a.grid(column=0,row=1,**opts)
        boton_a.grid(column=0,row=1,**opts)

        label_b.grid(column=0,row=2,**opts)
        boton_b.grid(column=0,row=2,**opts)

        label_c.grid(column=1,row=1,**opts)
        boton_c.grid(column=1,row=1,**opts)

        label_d.grid(column=1,row=2,**opts)
        boton_d.grid(column=1,row=2,**opts)
    def sumar(self,d):
        self.__puntos+=d
        self.__puntaje.set(self.__puntos)