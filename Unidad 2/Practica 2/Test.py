#from Contenedor import contenedor
def test(uncontenedor):
    
    op=int(input("Selecciona la opcion que desea\n 1-Agregar Caja De Ahorro\n 2-Mostrar lista\n 3-Buscar Cuil\n 0-Finalizar\n"))
    while(int(op)>0 and int(op)<4):
        if (op==1):
            N=input("Numero de Cuenta ")
            C=input("cuil ")
            A=input("Apellido ")
            No=input("Nombre ")
            S=input("saldo ")
            uncontenedor.agregar(N,C,A,No,S)
        elif (op==2):
            uncontenedor.mostrar()
        elif(op==3):
            cu=input("Ingrese Cuil a buscar\n")
            b=uncontenedor.buscar(cu)
            print("{}".fromat(b))
        else:
            print("Opcion no valida\n")
        op=int(input("Selecciona la opcion que desea\n 1-Agregar Caja De Ahorro\n 2-Mostrar lista\n 3-Buscar Cuil\n"))
