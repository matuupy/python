#practica 20
notas = []
totalNotas = 0

for x in range(3):
    nota = 0
    while nota < 1 or nota >5:
        nota = int(input(f"ingrese la nota {x + 1}: "))
        notas.append(nota)
        totalNotas = totalNotas + nota

        promedio = totalNotas / 3

        print(f"El promedio de las notas: {notas} es {promedio}")
        








