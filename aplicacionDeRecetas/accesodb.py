from sqlite3 import *
from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.geometry()

def ingrsdat():
    crearObj = LabelFrame(ventana, height=10)
    crearObj.grid(column=1,row=1)

    tit = Label(crearObj, text='titulo del libro: ')
    tit.grid(column=1,row=1)
    
    titentr = Entry(crearObj, width=12)
    titentr.grid(column=2,row=1)

    autor = Label(crearObj, text='Autor del libro: ')
    autor.grid(column=1,row=2)

    nombre = Entry(crearObj, width=12)
    nombre.grid(column=2,row=2)

    def test():
        len(titentr.get()) !=0 and len(nombre.grid()) !=0

    def query():
        if test:
            print('si')
        else:
            print('no')
        
    boton = Button(ventana, command=query)
    boton.grid()


ingrsdat()

ventana.mainloop()