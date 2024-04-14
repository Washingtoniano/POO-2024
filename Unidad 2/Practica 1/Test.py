from CajaDeAhorro import CajaDeAhorro

def test():
    N=input("Numero de Cuenta ")
    C=input("cuil ")
    A=input("Apellido ")
    No=input("Nombre ")
    S=input("saldo ")

    caja=CajaDeAhorro(N,C,A,No,S)

    # partes=(input("Ingrese el cuil a verificar(No olvide los -)"))
    # partes=partes.split('-')
    # for i in range (len(partes)):
    #     print("{}".format(partes[i]))
    # for j in range (len(partes[1])):
    #     print("{}".format(partes[1][j]))
    caja.mostrar()
    monto=(input("Ingrese un monto a extraer "))
    # if monto=='':
    #     monto=0.0
    # else:
    #     float(monto)
    # ext=caja.extraer(monto)
    ext=caja.extraer(
        
        float(monto))
    if ext != -1:
        print("El monto actualizado es {}".format(ext))
    else:
        print("saldo Insuficiente")
    monto=input("Ingrese un monto a depositar ")
    # if monto=='':
    #     monto=0.0
    # else:
    #     float(monto)
    # val=caja.depositar(monto)
    val=caja.depositar(float(monto))
    print("El monto actualizado es {}".format(val))
    
    p=caja.comprobar(input("Ingrese el cuil a verificar(No olvide los -) "))
    if p==False:
        print("Cuil invalido")
    else:
        print("cuil valido")
    
    #print("{}".format(caja))