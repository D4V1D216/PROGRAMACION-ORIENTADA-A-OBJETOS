import matplotlib.pyplot as plt
import numpy as np
import random

#####VARIABLES#######
dimension=[50,100,200,500]
######LISTA DE COLORES#####
#Color=["green","red","purple","orange","yellow"]
#################Listas de dimensiones#################################
dimension_1=[]
dimension_2=[]
dimension_3=[]
dimension_4=[]
borde1=0
borde2=0
borde3=0
borde4=0

for j in range(0,4): 
    ####################Listas donde se almacenan las coordenadas de los puntos#############################
    Puntos=[]
    Puntos_x=[]
    Puntos_y=[]
    cuadro=dimension[j]
    
    ########################Almacena la primer coordenada que es el punto central#############################
    Primera=cuadro/2
    Puntos_x.append(Primera)
    Puntos_y.append(Primera)
    
    #######################Ciclo for que limita el rango de iteraciones###################
    for i in range(0,1000):
        P_x=random.randint(0,cuadro)
        P_y=random.randint(0,cuadro)
        Puntos_x.append(P_x)
        Puntos_y.append(P_y)
    largo=len(Puntos_x)

    #########################GRAFICA LOS PUNTOS##############################
    #cuadro_x,cuadro_y=[0,0,cuadro,cuadro,0],[0,cuadro,cuadro,0,0]
    #################Ciclo for que se utilia para recorrer cada dato de una lista####################
    for i in range(largo):
                
        ######Almacena los resultados de cada dimension en una lista y evalua si llega a 100 datos#################    
        X=(Puntos_x[i],Puntos_y[i])
        Puntos.append(X)
        ###########################################################################################################
        if j==0:
            if (len(dimension_1))==100:
                break
            else:
                dimension_1.append(Puntos[i]) 
            if Puntos_x[i]==cuadro or Puntos_y[i]==cuadro:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde1=borde1+1
    
            if Puntos_x[i]==0 or Puntos_y[i]==0:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde1=borde1+1
        ############################################################################################################
        if j==1:
            if (len(dimension_2))==100:
                break
            else:
                dimension_2.append(Puntos[i])
            if Puntos_x[i]==cuadro or Puntos_y[i]==cuadro:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde2=borde2+1
    
            if Puntos_x[i]==0 or Puntos_y[i]==0:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde2=borde2+1         
        #############################################################################################################
        if j==2:
            if (len(dimension_3))==100:
                break
            else:
                dimension_3.append(Puntos[i])
            if Puntos_x[i]==cuadro or Puntos_y[i]==cuadro:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde3=borde3+1
    
            if Puntos_x[i]==0 or Puntos_y[i]==0:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde3=borde3+1
        ########################################################################################################### 
        if j==3:
            if (len(dimension_4))==100:
                break
            else:
                dimension_4.append(Puntos[i])
            if Puntos_x[i]==cuadro or Puntos_y[i]==cuadro:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde4=borde4+1
    
            if Puntos_x[i]==0 or Puntos_y[i]==0:
                #print(f"Variable de dimension {dimension[j]}x{dimension[j]} se detuvo en la iteracion {i+1}.")
                borde4=borde4+1 
            
###################impresion de los valores#############################################33
print("Total de coordenadas almacenadas en una lista por cada dimension")
#print(dimension_1)
print(f"{dimension[0]}x{dimension[0]}: {len(dimension_1)} datos.")
print(f"Numero de veces que llego al borde: {borde1} veces.")
#print(dimension_2)
print(f"{dimension[1]}x{dimension[1]}: {len(dimension_2)} datos.")
print(f"Numero de veces que llego al borde: {borde2} veces.")
#print(dimension_3)
print(f"{dimension[2]}x{dimension[2]}: {len(dimension_3)} datos.")
print(f"Numero de veces que llego al borde: {borde3} veces.")
#print(dimension_4)
print(f"{dimension[3]}x{dimension[3]}: {len(dimension_4)} datos.")
print(f"Numero de veces que llego al borde: {borde4} veces.")
#NOTA: Si no se imprimen los valores de los bordes y solo aparecen de una sola dimension significa que no alcanzaron el borde en las 100 iteraciones.
##borde se refiere a las numero de veces que llego al borde entre los 100 datos de cada dimension

##########vectores que se utilizan en al grafica de barras#############
Vector_d=[f"{dimension[0]}x{dimension[0]}",f"{dimension[1]}x{dimension[1]}",f"{dimension[2]}x{dimension[2]}",f"{dimension[3]}x{dimension[3]}"]
Vector_L=[(len(dimension_1)),(len(dimension_2)),(len(dimension_3)),(len(dimension_4))]
Vector_b=[(borde1),(borde2),(borde3),(borde4)]
Vector_d_largo=np.arange(len(Vector_d))
Ancho=0.3

############GRAFICO DE BARRAS#####################
plt.bar(Vector_d_largo-Ancho/2,Vector_L,color="red",label="Num.DATOS X DIMENNSION",width=Ancho)
plt.bar(Vector_d_largo+Ancho/2,Vector_b,color="blue",label="Num.veces que toco el borde",width=Ancho)
plt.xticks(Vector_d_largo,Vector_d)
plt.title("RANGO DE ITERACIONES POR DIMENSIONES EN UNA CAMINATA")
plt.xlabel("DIMENSIONES")
plt.ylabel("RANGO DE DATOS DE LA DIMENSION")
plt.legend()
plt.show()