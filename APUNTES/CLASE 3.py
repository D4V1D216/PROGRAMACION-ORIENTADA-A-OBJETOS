###PRACTICA 2 MARTES 13 DE MAYO DEL 2025
###FUNCIONES
##def operacion(persona,numero):
##    si=persona!=str
##    mayor_edad=numero>18
##    if mayor_edad == True:
##        return("su nombre es")
##        return("si es mayor")
##    return()
##
##nombre="david"
##edad=22
##resultado=operacion(nombre,edad)
##print(resultado)
##def multiplicacion(numero1,numero2):
##    R=numero1*numero2
##    return(R)
##print("ingrese el primer numero")
##A= int(input())
##print("ingrese el segundo numero")
##B= int(input())
##res=multiplicacion(A,B)
#print("su resultado es:",res)
numeros = input("Ingresa números separados por comas: ")  # Ejemplo: 10,20,30
mi_tupla = tuple(map(int, numeros.split(',')))  # Convertir a tupla de enteros
print(mi_tupla)
