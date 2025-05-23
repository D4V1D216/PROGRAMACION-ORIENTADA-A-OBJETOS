#DISTANCIAS 2 PRACTICA

#a) Graficar coordenadas cartesianas (X,Y) los 2 puntos(rojo) tanto inicial como final la recta(azul)
#entre los 2 puntos
#ejex-ejey-plt.legend
#activar rejilla

import matplotlib.pyplot as plt
##pide al usuario introducir las coordenadas
print("PROGRAMA QUE GRAFICA 2 PUNTOS EN UNA RECTA")
print("------------------------------------------")
print("Introduzca la coordenada del primer punto:")
A=input()
P1=tuple(map(int,A.split(",")))
print("Introduzca la coordenada del segundo punto:")
B=input()
P2=tuple(map(int,B.split(",")))

plt.plot((P1[0],P2[0]),(P1[1],P2[1]), color="blue")
plt.scatter(P1[0],P1[1], color="red")
plt.scatter(P2[0],P2[1], color="red")
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.grid(True)
plt.show()/
