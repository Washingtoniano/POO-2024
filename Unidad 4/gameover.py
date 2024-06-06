from tkinter import ttk, font
from tkinter import *

class gameover():
    __ventana=object
    def __init__(self,puntos) -> None:
        self.__ventana=Tk()
        self.__ventana.title="Game over"
        self.__ventana.resizable=(0,0)
        fuente=font.Font(weight='bold')
        self.marco=ttk.Frame(self.__ventana, borderwidth=2,relief="raised", padding=(10,10))
        self.gamelabel=ttk.Label(self.marco,text="Game Over",font=fuente,padding=(5,5))
        self.labelpuntos=ttk.Label(self.marco,text="Puntos",font=fuente,padding=(2,2))
        self.labelP=ttk.Label(self.marco,text=str(puntos),font=fuente,padding=(5,5))
        self.boton2 = ttk.Button(self.marco, text="salir",padding=(5,5), command=quit)
        
        self.marco.grid(column=0,row=0)
        self.gamelabel.grid(column=0,row=0)
        self.labelpuntos.grid(column=0,row=1)
        self.labelP.grid(column=1,row=1)
        self.boton2.grid(column=0,row=2,columnspan=1)

        
        self.__ventana.mainloop()