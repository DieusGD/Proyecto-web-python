#se busca hacer un arbol que demuestre la relacion y cantitidad de miembros de una familia
generaciones = int(input("Cuantas generaciones son de la familia? "))
numGen = 1
arborGen = {}
while generaciones >= numGen:
    print("cuantos miembros son de la generacion " +numGen)
    miembGen1 = int()
    cont = 1
    gen = []
    while miembGen1 >= cont:
        nom = str(input("escribe su nombre: "))
        edad = int(input("escribe su edad: "))
        miem = {cont, nom, edad}
        gen.append(miem)
        cont = cont + 1
    print(gen)




    