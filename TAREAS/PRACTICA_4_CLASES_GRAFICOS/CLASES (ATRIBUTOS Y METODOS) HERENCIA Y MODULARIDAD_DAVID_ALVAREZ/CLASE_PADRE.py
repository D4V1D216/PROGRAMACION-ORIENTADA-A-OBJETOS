#############Clase padre#########################
class vehiculo:
    def __init__(self, jugador, marca, modelo, velocidad_maxima, aceleracion, manejo):
        self.jugador = jugador
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.manejo = manejo

    def acelerar(self):
        print(f"{self.jugador} acelera.")
        
        
    def frenar(self):
        print(f"{self.jugador} frena lentamente.")
        
        
    def direccionizq(self):
        print(f"{self.jugador} se mueve a la izquierda.")
        
        
    def direccionder(self):
        print(f"{self.jugador} se mueve a la derecha.")