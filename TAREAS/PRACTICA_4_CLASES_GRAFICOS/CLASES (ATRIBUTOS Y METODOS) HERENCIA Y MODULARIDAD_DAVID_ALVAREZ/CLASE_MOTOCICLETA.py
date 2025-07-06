######################CLASE HIJO MOTOCICLETA############################
import CLASE_PADRE as pad

class motocicleta(pad.vehiculo):
    def __init__ (self, jugador, marca, modelo, velocidad_maxima, aceleracion, manejo, casco, estabilidad):
        super().__init__(jugador, marca, modelo, velocidad_maxima, aceleracion, manejo)
        self.casco = casco
        self.estabilidad = estabilidad

    def caballito(self):
        print(f"{self.jugador} hace caballito con la motocileta para ganar velocidad.")
        MOTO.velocidad_maxima=MOTO.velocidad_maxima+MOTO.aceleracion

    def salto(self):
        print(f"{self.jugador} hace un salto con la motocileta por encima de un obstaculo.")
        MOTO.velocidad_maxima=MOTO.velocidad_maxima-10
        
MOTO=motocicleta("ruvik", "mortalica", "deportivo", 150, 20, "Cambios", "resistente","debil")