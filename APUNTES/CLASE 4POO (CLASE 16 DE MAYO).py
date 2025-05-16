#Clase 16 de mayo del 2025 POO

#Funcion try
try:
    x=int(input("ingresa un dato numerico"))
except ValueError:
    print("eso no es un numero")



##############################################
from random import random, uniform
import matplotlib.pyplot as plt

##x=[10,20,30,40,50,60,70,80,90]
y=[i*-2 for i in range(0,11)]
x=[i*2 for i in range(0,11)]
y2=[i*1 for i in range(0,11)]
x2=[i*1 for i in range(0,11)]

cuantos_ejex= len(x)
cuantos_ejey=len(y)
assert cuantos_ejex == cuantos_ejey
#grafica las lineas en el rango establecido (linewidth)
plt.plot(x,y,color="yellow", label="linea1")#llama a la libreria de matplotlib y le introducimos los ejes 
plt.plot(x2,y2, label="linea2")
plt.scatter(x,y,color="red",s=10)
plt.scatter(x2,y2,color="green",s=10)
plt.axhline(y=0,color="black")
plt.axvline(x=0,color="black")
#agrega nombre a los ejes y un titulo
plt.title("GRAFICA")
plt.xlabel("ejex")
plt.ylabel("ejey")
plt.legend()
plt.grid(True)
##plt.savefig("grafica_clase1")
plt.show()#muestra el grafico
##################################################
#GRAFICA DE BARRAS
import matplotlib.pyplot as plt
##nombre=["ana", "luis","pedro","laura"]
##edades=[25, 40, 15, 20]
##plt.bar(nombre, edades, color="violet")
##plt.title("grafica de barras")
##plt.ylabel("edad")
##plt.show()
###################################################
#grafica de pasteles
etiquetas=["manzana","pera","banana"]
cantidades=[30,40,25]
plt.pie(cantidades, labels=etiquetas, autopct="%1.1f%%")
plt.title("frutas vendidas")
plt.show()
#################################################
#histogramas

################################################
#boxplot

################################################
#pandas
