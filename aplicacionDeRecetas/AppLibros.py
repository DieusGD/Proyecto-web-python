from tkinter import *
from tkinter.ttk import *

ventana=Tk()
ventana.geometry("360x400")


class menu():
    menubar = Menu(ventana)
    ventana.configure(menu=menubar)

    filemenu = Menu(menubar)
    filemenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label='Archivo', menu=filemenu)
    filemenu.add_command(label ="Nuevo")

    

ventana.mainloop()