from menu import menu
from lista import lista
from ObjectENcoder import ObjectEncoder
import csv
def test(unalista,unobject):
    archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 6\\Personal.csv",'r')
    reader=csv.reader(archivo,delimiter=';')
    band=False
    if band==False:
        band=True
    else:
        

if __name__ == '__main__':
    unalista=lista()
    unobject=ObjectEncoder()
    unmenu=menu()
    test(unalista,unobject)
    unmenu.inicializar(unalista,unobject)