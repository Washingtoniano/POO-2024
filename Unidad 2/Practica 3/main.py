from Menu import menu
#from Test import test
if __name__== '__main__':
    unmenu=menu()
    #test()
    print("Bienvenido\n")
    b= int(input("Hay una función test con valores aleatorios disponible. ¿Desea ejecutarla?\n 1-SI     2-NO\n"))
    band=False
    while b!=2 and band==False:
        if b==1:
            unmenu.test()
            print("Gracias por probar la función test\n")
            band=True
        else:
            print("Datos erroneo\n")
            b= int(input("Hay una función test con valores aleatorios disponible ¿Desea ejecutarla?\n 1-SI     2-NO\n"))

    if b==2:
        #unmenu.mostrar()
        unmenu.manejador()
    print("Adios")
