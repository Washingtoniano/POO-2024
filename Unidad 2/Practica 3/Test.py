from GestordeVenta import GestorVentas
import random
ungestor=GestorVentas()
def test():
        for i in range (5):
            for j in range (7):
                d=random.randrange(1,7,1)
                s=random.randrange(1,5,1)
                m=random.randrange(20,27000,6)
                ungestor.acumular(d,s,m)
        ungestor.mostrar()
        ungestor.maximo(1)
        ungestor.minimo()