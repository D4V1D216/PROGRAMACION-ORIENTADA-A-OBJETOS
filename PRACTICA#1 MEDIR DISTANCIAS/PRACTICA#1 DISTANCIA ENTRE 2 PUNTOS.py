#########################################
#PRACTICA1 TAREA (SUBIR A GITHUB)
import math
print("-------------------------------------------------")
print("Programa para obtener la de dos puntos en un plano")
print("-------------------------------------------------")
print("Introduzca las coordenadas del primer punto")
P1=input()
T1=tuple(map(int,P1.split(",")))
print(type(T1))
print(T1)
print("Introduzca las coordenadas del segundo punto")
P2=input()
T2=tuple(map(int,P2.split(",")))
print("¿Con que metodo medira distancia? Manhattan(1) Euclidiana(2)")
opcion=int(input())
if opcion==1:
    print("METODO MANHATTAN")
    def MAN(COR1,COR2):
        X1,X2=T1[0],T2[0]
        Y1,Y2=T1[1],T2[1]
        DX=X2-X1
        DY=Y2-Y1
        RM=DX+DY
        return(RM)
    RES1=MAN(T1,T2)
    print("La distancia entre los dos puntos es de:",RES1)
else:
    if opcion==2:
        print("METODO EUCLIDIANO")
        def EUC(COR1,COR2):
            X1,X2=T1[0],T2[0]
            Y1,Y2=T1[1],T2[1]
            DX=X2-X1
            DX2=DX**2
            DY=Y2-Y1
            DY2=DY**2
            EUCR=DX2+DY2
            REUCR=math.sqrt(EUCR)
            return(REUCR)
        RES2=EUC(T1,T2)
        print("La distancia entre los dos puntos es de:",RES2)
    else:
        print("NO ELIGIO NINGUNA OPCION")
