#FUNCIONES PARA LOS BOTONES DE OPERACION
import tkinter as tk
import math
#OPERACIONES ARITMETICAS
entrada_text = tk.StringVar()
def suma():
    entrada_text.set(entrada_text.get() + "+")
def resta():
    entrada_text.set(entrada_text.get() + "-")
def multiplicacion():
    entrada_text.set(entrada_text.get() + "*")
def division():
    entrada_text.set(entrada_text.get() + "/")
def raiz():
    try:
        numero=float(entrada_text.get())
        entrada_text.set(math.sqrt(numero))
    except:
        entrada_text.set("Error")
def resultado():
    try:
        entrada_text.set(str(eval(entrada_text.get())))
    except:
        entrada_text.set("Error")
def limpiar():
    entrada_text.set("")

#FUNCIONES DE LOS NUMEROS
def nueve():
    entrada_text.set(entrada_text.get() + "9")
def ocho():
    entrada_text.set(entrada_text.get() + "8")
def siete():
    entrada_text.set(entrada_text.get() + "7")
def seis():
    entrada_text.set(entrada_text.get() + "6")
def cinco():
    entrada_text.set(entrada_text.get() + "5")
def cuatro():
    entrada_text.set(entrada_text.get() + "4")
def tres():
    entrada_text.set(entrada_text.get() + "3")
def dos():
    entrada_text.set(entrada_text.get() + "2")
def uno():
    entrada_text.set(entrada_text.get() + "1")
def cero():
    entrada_text.set(entrada_text.get() + "0")