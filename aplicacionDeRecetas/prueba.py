from sqlite3 import *
from tkinter import *
from tkinter.ttk import *
from tkinter import Menu

ventana = Tk()
ventana.geometry("350x520")

def crearTablas():
    con = connect('baseDeDatos.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clientes('id' INTEGER, 'nombre' TEXT, 'telefono' INTEGER, correo TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS productos('id', 'nombre', 'costo', 'stock')")
    con.commit()
    cur.close()


def entradas():
    cuadro = LabelFrame(ventana, height=5,padding=20)
    cuadro.grid(column=1,row=1)

    Label(cuadro,text='nombre').grid(column=0,row=0)
    val1 = Entry(cuadro, width=15)
    val1.grid(column=1,row=0)
    
    def validacion():
        return len(val1) !=0
    def datosdb():
        if validacion:
            con = connect('baseDeDatos.db')
            cur = con.cursor()
            cur.execute('SELECT nombre FROM clientes')
            con.commit()
            rows = cur.fetchone()
            nombre = val1.get()
            for row in rows:
                if row == nombre:
                    Label(ventana,text=nombre+' esta en la lista').grid(column=1,row=4)
                else:
                    Label(ventana,text='agregar ' + nombre + ' a base de datos?').grid(column=1,row=4)
            con.close()
    
    Button(cuadro, text='datos', command=datosdb).grid()

Button(ventana, text="entrada", command=entradas).grid()

def listaUsuarios():
    listaUs = Combobox(ventana)
    listaUs.grid(column=1)
    Entry(listaUs, state='disabled')
    con = connect('baseDeDatos.db')
    cur = con.cursor()
    cur.execute('SELECT nombre FROM clientes')
    con.commit()
    rows = cur.fetchone()
    listaUs['values'] = (rows)
    con.close()
    

listaUsuarios()
ventana.mainloop()