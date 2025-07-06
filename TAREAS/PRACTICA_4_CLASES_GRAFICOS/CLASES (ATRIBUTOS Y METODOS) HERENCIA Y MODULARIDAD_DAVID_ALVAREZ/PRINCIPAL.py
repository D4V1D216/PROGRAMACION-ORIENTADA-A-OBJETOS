############################ MAIN ############################################
import matplotlib.pyplot as plt
from CLASE_MOTOCICLETA import MOTO
from CLASE_SUPERMERCADO import SUP
from CLASE_AUTOMOVIL import AUTO
from CLASE_DEPORTIVO import AUTODEP
#############################################################################################################
print(MOTO.__class__.__name__)

print("Velocidad:",MOTO.velocidad_maxima)

MOTO.caballito()
print("Velocidad:",MOTO.velocidad_maxima)
MOTO.acelerar()
MOTO.direccionder()
MOTO.direccionizq()
MOTO.salto()
print("Velocidad:",MOTO.velocidad_maxima)
MOTO.frenar()

print("--------------------------------------------------------------------------")
#########################################CARRO DE SUPERMERCADO###############################################
print(SUP.__class__.__name__)

print("Productos en el carrito:",SUP.capacidad_de_carga)
print("Velocidad:",SUP.velocidad_maxima)

SUP.lanzar_productos()
print("Productos en el carrito:",SUP.capacidad_de_carga)
print("Velocidad:",SUP.velocidad_maxima)
SUP.acelerar()
SUP.direccionder()
SUP.direccionizq()
SUP.ruedas()
print("Velocidad:",SUP.velocidad_maxima)
SUP.frenar()

print("--------------------------------------------------------------------------")
###########################################AUTOMOVIL###########################################################
print(AUTO.__class__.__name__)

print("Velocidad:",AUTO.velocidad_maxima)
print("Combustible:",AUTO.combustible)

AUTO.aceleracion_por_objeto()
print("Velocidad:",AUTO.velocidad_maxima)
print("Combustible:",AUTO.combustible)
AUTO.direccionder()
AUTO.tomar_combustible()
print("Combustible:",AUTO.combustible)
AUTO.direccionizq()
AUTO.frenar()
print("Combustible:",AUTO.combustible)

print("--------------------------------------------------------------------------")
###########################################AUTOMOVIL DEPORTIVO#################################################
print(AUTODEP.__class__.__name__)

print("Velocidad:",AUTODEP.velocidad_maxima)
print("Color:",AUTODEP.color)

AUTODEP.activar_turbo()
print("Velocidad:",AUTODEP.velocidad_maxima)
AUTODEP.acelerar()
AUTODEP.direccionder()
AUTODEP.drift()
print("Velocidad:",AUTODEP.velocidad_maxima)
AUTODEP.direccionizq()
AUTODEP.pintura()
print("Color:",AUTODEP.color)
AUTODEP.frenar()

##GRAFICA EN MATPLOTLIP
AUTOS=[MOTO,SUP,AUTO,AUTODEP]
nombre=[]
velocidad=[]
for i in AUTOS:
    NAME=i.marca
    nombre.append(NAME)
    VEL=i.velocidad_maxima
    velocidad.append(VEL)

plt.bar(nombre,velocidad,color="blue",width=0.6)
plt.title("VELOCIDADES DE LOS AUTOS")
plt.xlabel("AUTOS")
plt.ylabel("VELOCIDAD")
plt.show()