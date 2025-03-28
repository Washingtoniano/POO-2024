from paciente import paciente

class ambulatorio(paciente):
    __historial:str
    __alergia:str
    __obrasocial:str
    def __init__(self, **kwards) -> None:
        super().__init__(**kwards)
        self.__alergia=kwards["alergia"]
        self.__historial=kwards["his"]
        self.__obrasocial=kwards["obra"]
    def getAlergia(self):
        return self.__alergia
    def getObra(self):
        return self.__obrasocial
    def getHistorial(self):
        return self.__historial
    def calculo(self):
        plus=0
        if self.__obrasocial=="Obra Social Provincia":
            plus=5000
        elif self.__obrasocial== " Obra Social OSDE ":
            plus=2000
        else:
            plus=10000
        resultado=(self.getValorcon()*-1)+plus
        return resultado
    def mostrar(self):
        super().mostrar()
        print("Historial: {} Alergia: {} Obra Social: {}".format(self.__historial,self.__alergia,self.__obrasocial))