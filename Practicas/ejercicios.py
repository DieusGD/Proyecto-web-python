#lstrip es para leer datos desde la consola

def ej1():
    age = int(input("¿Cuál es tu edad? "))
    if age < 18: 
        print ("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")

def ej2():
    #lower
    #variable que pida contrase;a, la almacene y pregunte al usuario por esta
    #independientemente de mayus o minus
    pasword = str(input("contrasae;a: "))
    pasword.lower()
    pasword2 = str(input("escriba su contrase;a de nuevo:\n"))

    if pasword == pasword2.lower():
        print("es correcto")
    else:
        print("incorrecto")

def ej3():
    #pide 2 numeros y muestra su division. si es 0 el programa debe dar un error

    num1 = int(input("numero 1:\n"))
    num2 = int(input("numero 2:\n"))
    if (num1/num2) !=0:
        print(num1/num2)
    else:
        print("error")

def ej4():
    #un numero y muestra si es par o impar
    num = int(input("numero: \n"))
    

def ej5():
    #Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
    #Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla
    #si el usuario tiene que tributar o no.
    edad = int(input("escribe tu edad: "))
    ingr = int(input("escribe tus ingresos mensuales: "))
    if edad >= 16 and ingr >= 1000:
        datos = ["tienes, " + edad + " de edad, con " + ingr +22 " de ingresos"]
        print("debes de tributar, " + datos)
    else:
        print("aun no debes de tributar, " + datos)

ej5()
    
# def ej6():
#     #Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#     #El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
#     #Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.



    
# def ej7():
# #Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# #Renta	Tipo impositivo
# #Menos de 10000€	5%
# #Entre 10000€ y 20000€	15%
# #Entre 200000€ y 35000€	20%
# #Entre 350000€ y 60000€	30%
# #Más de 60000€	45%
# #Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
    
# def ej8():
#     #En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# #Nivel	Puntuación
# #Inaceptable	0.0
# #Aceptable	0.4
# #Meritorio	0.6 o más
# #Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
    
# def ej9():
#     #Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
#     #El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
#     #Si el cliente es menor de 4 años puede entrar gratis, 
#     #si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

    
# def ej10():
#     a 

# def ej11():
#     a
    
# def ej12():
#     a

# def ej13():
#     a
    
# def ej14():
#     a
    
# def ej15():
#     a 