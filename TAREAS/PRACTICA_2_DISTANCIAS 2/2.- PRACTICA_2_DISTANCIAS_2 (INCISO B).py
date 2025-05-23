#DISTANCIAS 2 PRACTICA

#b)ingresar cuantas coordenadas
#agregar cada coordenada (x,y) manualmente (recomendacion almacenar en una lista)
#graficar puntos de coordenadas
#dist. euclidiana de cada linea
#sumatoria de distancias euclidianas
#PUNTOS EXTRA PARA EXAMEN
#Calcular area con una o dos funciones

import matplotlib.pyplot as plt
import numpy as np
print("PROGRAMA QUE DIBUJA FIGURAS EN UN PLANO CARTESIANO DE ACUERDO A LAS COORDENADAS")
print("----------------------------------------------------------------")
##def EUC(COR1,COR2):
##            X1,X2=coordenadas[0],coordenadas[0]
##            Y1,Y2=[1],T2[1]
##            DX=X2-X1
##            DX2=DX**2
##            DY=Y2-Y1
##            DY2=DY**2
##            EUCR=DX2+DY2
##            REUCR=math.sqrt(EUCR)
##            return(REUCR)
def EUC(COR1, COR2):
    return np.linalg.norm(np.array(COR1) - np.array(COR2))

n=int(input("Ingrese el número de coordenadas: "))
coordenadas=[]

for i in range(n):
    print("Ingrese la coordenada:")
    CO=input()
    T=tuple(map(int,CO.split(",")))
    coordenadas.append(T)

x,y=zip(*coordenadas)
plt.scatter(x,y,color='red')
J=len(coordenadas)

for i in range(J-1):
    plt.plot([coordenadas[i][0],coordenadas[i+1][0]],[coordenadas[i][1],coordenadas[i+1][1]],color="blue")

print("Distancias Euclidianas:")
for i in range(J-1):
    dist=EUC(coordenadas[i],coordenadas[i+1])
    CO1,CO2=coordenadas[i],coordenadas[i+1]
    print("Distancia entre coordenadas", CO1,",",CO2,":")
    print(dist)
    
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.title("FIGURA CON COORDENADAS")
plt.axhline(y=0,color="black")
plt.axvline(x=0,color="black")
plt.grid(True)
plt.show()

