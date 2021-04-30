
#Fisica, Buscamos usar Formulas establecidas:
print("Programa de formulas:\n")
print("Formula de V = 1 \n Formula de D = 2 \n Formula de T = 3")

resp = int(input("Que Formula quieres usar?"))
if resp ==1:
    dist = float(input("Introduce el valor de la Distancia"))
    tiem = float(input("Introduce el valor del Tiempo"))
    vel = dist/tiem
    print("El valor de la Velocidad es de: ")
    print(vel)

if resp==2:
    vel = float(input("Valor de la Velocidad: "))
    tiem = float(input("Valor del Tiempo: "))
    dis = vel*tiem
    print("Valor de la Distancia: ")
    print(dis)

if resp==3:
    dist = float(input("Valor de la Distancia: "))
    vel = float(input("Valor de la Velocidad: "))
    tiem= dist/vel
    print("Valor del Tiempo: ")
    print(tiem)
