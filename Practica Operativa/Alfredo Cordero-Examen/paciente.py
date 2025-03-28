
class paciente():
    __nombre:str
    __apellido:str
    __email:str
    __numero:int
    __valorCon=15000
    def __init__(self,**kwards) -> None:
        self.__valorCon=15000

        self.__nombre=kwards["nom"]
        self.__apellido=kwards["ape"]
        self.__email=kwards["email"]
        self.__numero=int(kwards["num"])
    @classmethod
    def getValorcon(cls):
        return cls.__valorCon
    @classmethod
    def setValorCon(cls,val):
        cls.__valorCon=val
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEmail(self):
        return self.__email
    def getNume(self):
        return self.__numero
    def importecobrado(self):
        return self.getValorcon()+self.calculo()
    def calculo(self):
        return 0
    def mostrar(self):
        print("\nNombre: {} Apellido: {} email: {} numero: {} Importe Cobrado: ${}".format(self.__nombre,self.__apellido,self.__email,self.__numero,self.importecobrado()))