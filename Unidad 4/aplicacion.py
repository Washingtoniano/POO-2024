import tkinter as tk
from tkinter import *
#Utilizar Geometria grid
#pygugu-designer
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a=tk.Canvas(self,bg="#009000")
        label_b=tk.Canvas(self,bg="#ffff00")
        label_c=tk.Canvas(self,bg='#ff0000')
        label_d=tk.Canvas(self,bg='#0000ff')

        boton_a=tk.Button(self,bg="#00ff00")

        opts={'ipadx':50,'ipady':50,'sticky':'nswe'}
        label_a.grid(column=0,row=0,**opts)
        boton_a.grid(column=0,row=0,**opts)

        label_b.grid(column=0,row=1,**opts)
        label_c.grid(column=1,row=0,**opts)
        label_d.grid(column=1,row=1,**opts)
    