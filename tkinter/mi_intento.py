import tkinter
from tkinter.ttk import *
from inicio import ini
 

def fila():
    datos = LabelFrame(ini, text="introduce los datos")
    Frame(datos, text="x1").grid(column=1,row=1)
    x1g= Label(datos,width=3)

    Frame(datos, text="y1").grid(column=2,row=1)
    y1g= Label(datos,width=3)

    Frame(datos, text="z1").grid(column=1,row=2)
    z1g= Label(datos,width=3)

    Frame(datos, text="x2").grid(column=2,row=2)
    x2g= Label(datos,width=3)

    Frame(datos, text="y2").grid(column=1,row=3)
    y2g= Label(datos,width=3)

    Frame(datos, text="z2").grid(column=2,row=3)
    z2g= Label(datos,width=3)

    def datosFinales():
        principio = x1g.getint() and y1g.getint() and z1.getint()
        fin = x2g.getint() and y2g.getint() and z2g.getint()
        distx = x1g.getint() - x2g.getint() 
        disty = y1g.getint() - y2.getint()
        distz = z1g.getint() - z2g.getint()
        datFin = LabelFrame(ini ,height=20).grid(column=2,row=2)
        principio = Label(datFin).grid(row=3,column=3)
    totalDeCuadros = distx + disty + distz
    Button(datos,command=datosFinales).grid(column=-1,row=-1)

def rectangulos(x1, y1, z1, x2, y2, z2):
    def rectanguloEnX(x1, y1, x2, y2,):
        x1 and y1, x2 and y2
        distx = x1 - x2
        disty = y1 - y2
        totalDeCuadrados = distx + disty
    
    def rectanguloEnXZ(x1, z1, x2, z2):
        inicio = x1 and z1
        final = x2 and z2
        distx = x1 - x2
        distz = z1 - z2
        totalDeCuadrados = distx + distz
    
    def rectanguloEnXY(y1, z1,y2, z2):
        inicio = y1 and z1
        final = y2 and z2
        disty = y1 - x2
        distz = y1 - z2
        totalDeCuadrados = disty + distz
