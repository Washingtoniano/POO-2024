from CajaDeAhorro import CajaDeAhorro
def test():
    N=input("Numerp de Cuenta")
    C=input("cuil")
    A=input("Apellido")
    No=input("Nombre")
    S=float(input("saldo"))

    caja=CajaDeAhorro(N,C,A,No,S)
    caja.mostrar()
    monto=float(input("Ingrese un monto a extraer"))
    ext=caja.extraer()
    if ext != -1:
        print("El monto actualizado es {}".format(ext))
    caja.depositar()
    caja.comprobar()
    #print("{}".format(caja))