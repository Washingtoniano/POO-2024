from Personal import personal
class apoyo(personal):
    __categoria:int
    __porcentaje:dict

    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad,**kwards) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,**kwards)
        self.__categoria=kwards['categoria']
        self.__porcentaje=dict({'1_10':10,'11_20':20,'21_22':30})
        
    def calcular(self):
        #Porcentaje por categoría: 10% si la categoría es de 1 a 10, 20 % si la categoría es de 11 a 20,  30% si la categoría es de 21 a 22.
        sueldo=self.getSueldo()
        if 1<=self.__categoria and self.__categoria<=10:
            sueldo=sueldo*self.__porcentaje['1_10']/100
        elif 11<=self.__categoria and self.__categoria<=20:
            sueldo=sueldo*self.__porcentaje['11_20']/100
        elif 21<=self.__categoria and self.__categoria<=22:
            sueldo=sueldo*self.__porcentaje['21_22']/100
        else:
            print("categoria desconocida encontrada")
            sueldo=0
        return sueldo+(self.getSueldo()*self.getAntiguedad())/100
    def setPorcentaje(self,monto):
        self.__porcentaje=monto
    
    """""
    def setPorcentaje(self,op):
        monto=float(input("ingrese el monto"))

        if op=='1':
            self.__porcentaje['1_10']=monto
        elif op=='2':
            self.__porcentaje['11_20']=monto
        elif op=='3':
            self.__porcentaje['21_22']=monto

    """""


    def getCategoria(self):
        return self.__categoria
    def tojson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldo=super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                categoria=self.getCategoria()


            )
        )
        return d
    
    def mostrar(self):
        super().mostrar()
        print("Categoria: {}".format(self.__categoria))