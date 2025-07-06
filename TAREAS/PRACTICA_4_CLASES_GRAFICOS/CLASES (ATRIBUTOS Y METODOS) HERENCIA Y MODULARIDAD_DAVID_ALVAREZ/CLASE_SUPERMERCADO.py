#######################CLASE HIJO CARRO DE SUPERMERCADO###############
import CLASE_PADRE as pad

class carro_de_supermercado(pad.vehiculo):
    def __init__(self, jugador, marca, modelo, velocidad_maxima, aceleracion, manejo, capacidad_de_carga, debil):
        super().__init__(jugador, marca, modelo, velocidad_maxima, aceleracion, manejo)
        self.capacidad_de_carga = capacidad_de_carga
        self.debil = debil

    def lanzar_productos(self):
        print(f"{self.jugador} lanza una tortilla de harina.")
        SUP.capacidad_de_carga=SUP.capacidad_de_carga-1
        SUP.velocidad_maxima=SUP.velocidad_maxima+SUP.aceleracion

    def ruedas(self):
        print("Las ruedas del carrito rechinan")
        SUP.velocidad_maxima=SUP.velocidad_maxima-20

SUP=carro_de_supermercado("David","soriana","De metal",100,100,"Impulso",10,"resistente")