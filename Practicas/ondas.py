def saludar():
    saludar.hola = str(input("*Cual es tu nombre:  "))
    saludar.resp = saludar.hola
    print("Hola, " + saludar.resp + ", te estoy saludando desde la función saludar() " \
          "del módulo saludos")

class Saludo():
    def __init__(self):
        print("Hola, te estoy saludando desde el __init__"  \
              "de la clase Saludo")

saludar()