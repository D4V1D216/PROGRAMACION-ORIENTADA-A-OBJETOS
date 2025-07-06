##########################CLASE DEPORTIVO#####################
import CLASE_PADRE as pad

class automovil_deportivo(pad.vehiculo):
    def __init__(self, jugador, marca, modelo, velocidad_maxima, aceleracion, manejo, modo_turbo, color):
        super().__init__(jugador, marca, modelo, velocidad_maxima, aceleracion, manejo)
        self.modo_turbo = modo_turbo
        self.color = color

    def activar_turbo(self):
        print(f"{self.jugador} activo el {self.modo_turbo}.")
        AUTODEP.velocidad_maxima=AUTODEP.velocidad_maxima+AUTODEP.aceleracion
        
    def drift(self):
        print(f"{self.jugador} hizo un drift.")
        AUTODEP.velocidad_maxima=AUTODEP.velocidad_maxima-50
        
    def pintura(self):
        print(f"{self.jugador} se metio a un taller de pintura.")
        AUTODEP.color="Verde"

AUTODEP=automovil_deportivo("Shadow","Ferrari","Deportivo",300,50,"Estandar","Oxido nitroso","Rojo")