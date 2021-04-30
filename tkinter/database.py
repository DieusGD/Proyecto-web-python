from sqlite3 import *
from tkinter import *
con = connect('empresa.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS folios('No.', 'A nombre de: ', 'Banco: ', 'Monto: ')")
con.commit()
con.close()

369
371
