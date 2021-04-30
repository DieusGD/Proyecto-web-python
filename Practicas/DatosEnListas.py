
def datSim():   #esta es una lista  DatoSimple
    cuenta = int(input("cuantos datos deseas procesar? \n"))
    datos = []
    conteo=1
    while conteo <= cuenta:
        dato = input("dato a procesar: \n")
        datos.append(dato)
        conteo = conteo + 1

    else:
        print(datos)


def datMed():   #este es un diccionario.Define solo el valor
    dato = {}

    cuenta = int(input("cantidad de datos: \n"))
    conteo=1
    key= 1
    while conteo <= cuenta:
        valor = input("dato: ")
        dato[key] = valor
        key = key + 1
        conteo = conteo + 1
    else:
        print(dato)

def datDob(): #Define el ide y el valor del dato
    cant = int(input("cuantos datos se procesaran?"))
    cont = 0
    datos = ([])
    while cont < cant:
        ide = str(input("ingresa el id: \n"))
        val = str(input("ingresa el valor del dato: "))
        cont = cont + 1
        dato = [ide, val]
        datos.append(dato)
    print(datos)
    
def datCarac(): #Da distintos valores a un mismo dato
    nom = str(input("Valor del Dato: "))
    cant = int(input("cantidad de caracteristicas: "))
    cont = 0
    caracts = []
    while cont < cant:
        caract = str(input("caracteristica:"))
        caracts.append(caract)
        cont = cont + 1
    product = {
        "name":nom,
        "datos":caracts
    }
    print(product.values())

def a1():
    locations = {
    (56.334, 5776):"Tokyo",
    (30.6, 45634,6):"USA"
    }
    busq = str(input("tokio o Usa?: \n"))
    if busq.lower() == "tokio":
        print(locations)


# %%
