from tkinter import font,ttk
from tkinter import *
from aplicacion import Ventana
class inicio():
    __ventana=object
    __usuario=str
    def __init__(self) -> None:
    
        self.__ventana=Tk()
        self.__ventana.title="Bienvenido"
        self.__ventana.resizable=(0,0)
        fuente = font.Font(weight='bold')
        self.marco = ttk.Frame(self.__ventana, borderwidth=2,relief="raised", padding=(10,10))
        self.usuarioLbl = ttk.Label(self.marco, text="Usuario:",font=fuente, padding=(5,5))
        self.__usuario = StringVar()
        self.__usuario.set('')
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.__usuario,width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar",padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar",padding=(5,5), command=quit)
        self.marco.grid(column=0, row=0)
        self.usuarioLbl.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)
        self.ctext1.focus_set()
        self.__ventana.mainloop()
    def aceptar(self):
        self.__ventana.destroy()
        Ventana()

    