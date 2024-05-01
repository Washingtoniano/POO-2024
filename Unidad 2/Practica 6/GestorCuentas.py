import numpy as np
import csv
from Cuenta import cuenta
class GestorCuentas():
    __cuentas:np.ndarray
    __dimension:int
    __incremento=10
    __cantidad:int
    def __init__(self,dimension):
        self.__dimension=dimension
        self.__cantidad=0
        self.__cuentas=np.empty(self.__dimension,dtype=cuenta)
        self.__incremento=10

    def agregar (self,cuenta):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__cantidad]=cuenta
        self.__cantidad+=1
    def inicializar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 6\\cuentasBilletera.csv","r")
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unacuenta=cuenta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregar(unacuenta)
        archivo.close()
    def NPorcentaje(self,p):
        cuenta.getporcentaje=p/365
    def mostrar(self):
        for i in range (len(self.__cuentas)):
            if self.__cuentas[i]!=None:
                print(self.__cuentas[i])
        cuenta.verPorcentaje()
    def buscarCVU(self,DNI):
        i=0
        band=False
        while i<len(self.__cuentas) and band==False:
            if self.__cuentas[i].getDNI()==DNI:
                band=[]
                band.append(i)
                band.append(self.__cuentas[i].getCVU())
                band.append(self.__cuentas[i].getSaldo())
            i+=1
        return band
    def mostrarI(self,i):
        print(self.__cuentas[i])
    def setsaldo(self,i,S):
        self.__cuentas[i].setSaldo(S)
    def actualizar(self):
        for i in range(len(self.__cuentas)):
            if self.__cuentas[i]!=None:
                sal=self.__cuentas[i].getSaldo()
                sal=sal+sal*cuenta.getporcentaje()
                self.__cuentas[i].setSaldo(sal)
    def buscarSaldo(self,CVU):
        i=0
        band=False
        while i<len(self.__cuentas) and band==False:
            if self.__cuentas[i].getCVU()==CVU:
                band=[]
                band.append(i)
                band.append(self.__cuentas[i].getSaldo())
            i+=1
        return band
    def escribir(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 6\\cuentasACTBilletera.csv","w", newline='')
        writer=csv.writer(archivo)
        writer.writerow(['apellido','nombre','DNI','Telefono','saldo','CVU'])
        for i in range(len(self.__cuentas)):
            if self.__cuentas[i]!=None:
                writer.writerow([f'{self.__cuentas[i].getApellido()}',f'{self.__cuentas[i].getNombre()}',f'{self.__cuentas[i].getDNI()}',f'{self.__cuentas[i].getTelefono()}',f'{self.__cuentas[i].getSaldo()}',f'{self.__cuentas[i].getCVU()}'])
        writer.writerow([f'Porcentaje{cuenta.getporcentaje()}%'])
        
        
        archivo.close()

        # with open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 2\\Practica 6\\cuentasACTBilletera.csv",mode= 'w',newline='') as f:
        #     writer=csv.writer(f)
        # writer.writerow(['apellido','nombre','DNI','Telefono','saldo','CVU'])
        # writer.writerows(self.__cuentas)
        # writer.close()
        # with open(archivo,mode='w',newline='') as f:
        #     escritor = csv.writer(f)
        # escritor.writerows(self.__Cuentas)