#PROYECTO FINAL DE PROGRAMACION ORIENTADA A OBJETOS OSCAR DAVID GALVAN ALVAREZ TUE0096
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

ventana = tk.Tk()  #MANDA A TRAER LA VENTANA
ventana.title("PROYECTO FINAL (DAVID ALVAREZ) CALCULADORA")
ventana.geometry("850x480") #ANCHO X ALTO
ventana.configure(bg="grey")
ventana.resizable(False, False)

import FUNCIONES as fun #Se puso aqui para que no ocurra un error con una variable en el otro archivo ya que requiere que la ventana se cree.

tk.Label(ventana, text= "CALCULADORA", font=("Arial",12),).place(x=50,y=50)#TITULO

#CUADRO DE ENTRADA DE DATOS QUE ESTA RELACIONADO CON UNA VARIABLE DINAMICA LA CUAL PUEDE SER MODIFICADA POR LOS BOTONES
tk.Entry(ventana, text=fun.entrada_text, font=("Arial", 20), width=15, justify="right").place(x=50,y=100)

#NUMEROS PARA PRESIONAR (Se utilza lambda en esta ocasion para ahorrar lineas de codigo ya que seria lo mismo si se escribiera el set.get en una funcion aparte)
tk.Button(ventana,text="9",font=("Arial",14),command=fun.nueve).place(x=130,y=160)
tk.Button(ventana,text="8",font=("Arial",14), command=fun.ocho).place(x=90,y=160)
tk.Button(ventana,text="7",font=("Arial",14),command=fun.siete).place(x=50,y=160)
tk.Button(ventana,text="6",font=("Arial",14),command=fun.seis).place(x=130,y=205)
tk.Button(ventana,text="5",font=("Arial",14),command=fun.cinco).place(x=90,y=205)
tk.Button(ventana,text="4",font=("Arial",14),command=fun.cuatro).place(x=50,y=205)
tk.Button(ventana,text="3",font=("Arial",14),command=fun.tres).place(x=130,y=250)
tk.Button(ventana,text="2",font=("Arial",14),command=fun.dos).place(x=90,y=250)
tk.Button(ventana,text="1",font=("Arial",14),command=fun.uno).place(x=50,y=250)
tk.Button(ventana,text="0",font=("Arial",14),command=fun.cero).place(x=90,y=295)

#OPERACIONES ARITMETICAS (se mandan a llamar las funciiones desde el otro archvio importandolo)
tk.Button(ventana,text="+",font=("Arial",14),command=fun.suma).place(x=180,y=160)
tk.Button(ventana,text="-",font=("Arial",14), command=fun.resta).place(x=183,y=205)
tk.Button(ventana,text="x",font=("Arial",14),command=fun.multiplicacion).place(x=180,y=250)
tk.Button(ventana,text="/",font=("Arial",14),command=fun.division).place(x=183,y=295)
tk.Button(ventana,text="√",font=("Arial",14),command=fun.raiz).place(x=220,y=160)
tk.Button(ventana,text="=",font=("Arial",14),command=fun.resultado).place(x=220,y=205)
tk.Button(ventana,text="c",font=("Arial",14),command=fun.limpiar).place(x=220,y=250)

#######################################################################################################################################
#SEGUNDA PARTE (GRAFICADOR DE 2 PUNTOS)
tk.Label(ventana, text= "GRAFICADOR", font=("Arial",12),).place(x=400,y=50)#TITULO DEL GRAFICADOR
tk.Label(ventana, text= "X", font=("Arial",12),).place(x=520,y=70)
tk.Label(ventana, text= "Y", font=("Arial",12),).place(x=650,y=70)
tk.Label(ventana, text= "Punto 1:", font=("Arial",12),).place(x=400,y=100)
puntox1= tk.Entry(ventana)
puntox1.place(x=470,y=100)
puntoy1=tk.Entry(ventana)
puntoy1.place(x=600,y=100)
tk.Label(ventana, text= "Punto 2:", font=("Arial",12),).place(x=400,y=130)
puntox2= tk.Entry(ventana)
puntox2.place(x=470,y=130)
puntoy2=tk.Entry(ventana)
puntoy2.place(x=600,y=130)

ancho=400
largo=300
espacio_grafica=tk.Frame(ventana, width=ancho,height=largo,bg="white")
espacio_grafica.place(x=400,y=160)

def graficar():
    x1=float(puntox1.get())
    y1=float(puntoy1.get())
    x2=float(puntox2.get())
    y2=float(puntoy2.get())

    for widget in espacio_grafica.winfo_children():
        widget.destroy()
        
    dpi=70
    ancho_pulg=ancho/dpi
    alto_pulg=largo/dpi

    fig= plt.figure(figsize=(ancho_pulg,alto_pulg),dpi=dpi)
    plt.plot([x1, x2], [y1, y2], marker="o", color="red")
    plt.title("GRAFICA DE 2 PUNTOS")
    plt.xlabel("EJE X")
    plt.ylabel("EJE Y")
    plt.grid(True)

    canvas= FigureCanvasTkAgg(fig, master=espacio_grafica)
    canvas.draw()
    canvas.get_tk_widget().place(x=0,y=0, width=ancho,height=largo)

tk.Button(ventana,text="Graficar", command=graficar).place(x=750,y=115)

ventana.mainloop() 