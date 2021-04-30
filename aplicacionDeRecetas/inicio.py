from sqlite3 import *
from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.title("Diego")
ventana.geometry('500x380')

con = connect('baseDeDatos.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS prueba('id', 'nombre')")
con.commit()


def entradas():
    cuadro = LabelFrame(ventana, height=20, padding=5)
    cuadro.grid(column=0,row=0)

    Label(cuadro, text="identidad").grid(column=0,row=0)
    prim = Entry(cuadro, width=20)
    prim.grid(column=0, row=1)

    Label(cuadro, text="Nombre").grid(column=1,row=0)
    sec = Entry(cuadro, width=20)
    sec.grid(column=1,row=1)

    def agregar():
        res1 = prim.get()
        res2 = sec.get()
        if len(res1) !=0 and len(res2) !=0:
            Label(cuadro, text=res1).grid(column=0,row=2)
            Label(cuadro, text=res2).grid(column=1,row=2)
            def agregarval():
                entities:str = (res1, res2)
                connect('baseDeDatos.db')
                cursor.execute('''INSERT INTO prueba(id, nombre) VALUES(?, ?)''', entities)
                con.commit()
            bott = Button(cuadro, text='agregar siguientes valores?', command=agregarval)
            bott.grid(column=2,row=3)
            
        else: 
            errordatos = Label(ventana, text='Faltan datos')
            errordatos.grid(column=0,row=4)
        
    inicio.configure(text="agregar",command=agregar)
    cuadro.grid_anchor(anchor=NW)
    

inicio = Button(ventana, text='inicio', command= entradas)
inicio.grid(column=0,row=5)

ventana.mainloop()