##################CLASE AUTOMOVIL##############################
import CLASE_PADRE as pad

class automovil(pad.vehiculo):
    def __init__(self, jugador, marca, modelo, velocidad_maxima, aceleracion, manejo, combustible, ModificadorVel):
        super().__init__(jugador, marca, modelo, velocidad_maxima, aceleracion, manejo)
        self.combustible = combustible
        self.ModificadorVel = ModificadorVel

    def aceleracion_por_objeto(self):
        print(f"{self.jugador} obtuvo 10 de aceleracion al agarrar Modificador de Velocidad.")
        AUTO.combustible=AUTO.combustible-500
        AUTO.velocidad_maxima=AUTO.velocidad_maxima+AUTO.aceleracion

    def tomar_combustible(self):
        print(f"{self.jugador} obtuvo 200 de gasolina al agarrar Lata de combustible.")
        AUTO.combustible=AUTO.combustible+200

AUTO=automovil("Felipe","KIA","Estandar",150,10,"Estandar",3000,20)