from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *

ini = Tk()
ini.geometry("360x360")

def coord():
    cuadro= LabelFrame(ini, text="coordenadas",padding=30, labelanchor=N)
    cuadro.grid()
    
    Label(cuadro, text="x1: ").grid(row=1,column=1)
    x1g = Entry(cuadro, width=10)
    x1g.grid(row=1,column=2)

    Label(cuadro, text="x2: ").grid(row=2, column=1)
    x2g = Entry(cuadro, width=10)
    x2g.grid(row=2,column=2)
    
    Label(cuadro, text="y1: ").grid(row=1, column=3)
    y1g = Entry(cuadro, width=10)
    y1g.grid(row=1,column=4)
    
    Label(cuadro, text="y2: ").grid(row=2, column=3)
    y2g = Entry(cuadro, width=10)
    y2g.grid(row=2,column=4)
    
    Label(cuadro, text="z1: ").grid(row=1, column=5)
    z1g = Entry(cuadro, width=10)
    z1g.grid(row=1,column=6)
    
    Label(cuadro, text="z2: ").grid(row=2, column=5)
    z2g = Entry(cuadro, width=10)
    z2g.grid(row=2,column=6)

    def verificar():
        len(x1g.get()) !=0,len(x2g.get()) !=0,len(y1g.get()) !=0,len(y2g.get()) !=0,len(z1g.get()) !=0,len(z2g.get()) !=0

    def leer(): 
        if verificar == True:
            x1 = x1g.getint()
            x2 = x2g.getint()
            y1 = y1g.getint()
            y2 = y2g.getint()
            z1= z1g.getint()
            z2= z2g.getint()
            esTo="gola"
            Label(ini, text=esTo)
        else:
            Label(ini, text="no se han dado los suficientes datos").grid(column=0,row=4)

    bot.configure(command=leer)
    


bot = Button(ini, command=coord)
bot.grid(row=2,column=2)

ini.mainloop()
