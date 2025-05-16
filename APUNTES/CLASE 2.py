#PRACTICA_1 DE PROGRAMACION ORIENTADA A OBJETOS#
################################################################################################
#Declaracion de variables
a=10 #asi se declara una variable
b=10.5
numero="hola" #tambien se puede hacer que se imprima un texto guardandolo en una variable o imprimiendolo directo con el print
c= (1,2) #se pueden guardar un conjunto de datos asi como tambien listas de datos.
d= [1,2,3,4,5,6,7,8,9,10] #la lista se utiliza entre corchetes.
e= 2+3j #numeros complejos almacenados en variables
f= True #valor booleano que puede ser True o False
g= range (1,10)#rangos de datos.
i= {"alumno1":10, "alumno2":6}#se utiliza para almacenar un tipo de dato con otro, apareciendo juntos.

#type sirve para mostrar que tipo de dato estamos manejando ya sean numeros, caracteres, listas, conjuntos de datos entre otros.
print (a)#print sirve para poder imprimir en la consola un resultado pudiendo ser caracteres o numeros.
print (type (b))
print (type (numero))
print (type (c))#en este caso se muestra la clase tuple o tupla lo cual significa que es un conjunto de datos de 2 o mas.
print (type (d))
print (type (e))
print (type (f))
print (type (g))
print (type (i))
###############################################################################################
#librerias
from math import sqrt

raiz=64
print(sqrt(raiz))
##############################################################################################
#Crear vectores o listas
lista=[1,2,3,4,5,6,7,8,9,10,11,12]
largo=len(lista)#sirve para contar la cantidad de datos en una lista
print(largo)
minimo= min(lista)#va a buscar el numero mas pequeño de la lista
print(minimo)
maximo=max(lista)#ayuda a encontrar el valor maximo de una lista
print(maximo)
sumatoria=sum(lista)#suma todos los elementos dentro de una lista
print(sumatoria)
indice=lista[11]#el indice ayuda consultar algun elemento de la lista contando desde el 0 a un numero antes de los elementos totales de la lista.
print(indice)
reorden=lista[::-1]#reordena el orden de los datos
print (reorden)
ordenar=sorted(lista)#ordena la lista de menor a mayor
print(ordenar)
datos=lista[2:11:2]#[inicio:final:saltos]
print(datos)
repetir=[10]*5#crea una lista de un solo valor
print(repetir)
##################################################################################################
#matrices
M=[[1,2,3],[4,5,6]]#matrices M=[cual lista(0,n)][cual cual dato(0,n)]
position=M[1][1]
print(position)
J=[[1,2,3],[4,5,6],[7,8,9]]
position2=J[1][1]
#########################################################################################
#operaciones aritmeticas
suma=5+10#suma 2 numeros
resta=10-5#resta 2 numeros
multiplicacion=2*2#multiplica 2 numeros
potencia=2**2#la potencia n de un numero n
division=40/3#divide un numero
div_entera=40//3#arroja un valor entero en una division
residuo=40%3#indica el residuo de una division
redondeo=round(25.42)#redondea un valor
#otra forma de redondear
from math import ceil, floor
abajo=floor(5.9)
print(abajo)
arriba=ceil(5.9)
print(arriba)
##################################################################################################
#ciclos
for i in range(1,11):
    print(i)
lista2=[]
for i in lista:
    lista2.append(i-2)#.append sirve para almacenar un dato en una lista vacia
print(lista2)
lista3=[i+2 for i in lista]
print(lista3)
###############################################################################################
#condicionales
lista=[1,2,3,4,5,6,7,8]
if 9 in lista:
    print("si esta en la lista")
else:
    print("no esta en la lista")
###############################################################################################
#comparadores
valor=lista[5]
if 30< valor:
    print("si es mayor")
else:
    print("no es mayor")

if 6== valor:# un igual se asigna un valor 2 iguales se comparan 2 valores (!=) para indicar que es diferente
    print("igual")
else:
    print("diferente")
#########################################################################################################
#numeros random
from random import random, choice, uniform, randint, shuffle
numero= random()#te da un valor random con decimales
dec_alea=uniform(0.5,20)#te da valores random entre rangos con decimales
ent_alea=randint(1,50)#te da valores random enteros
lista_alea=choice(lista)#te da valores random en una lista
print(ent_alea)





