notas = [8, 9, 7, 6,]
notas.append(10)
notas.remove(6)
print(7 in notas)
print(notas)

salon = [
    ["ana", "luis"],
    ["eva", "ivan"]
]
print (salon)
print(salon[1][0])
salon[0][1] = "carla"
print(salon)

for fila in range(3):
    for columna in range(3):
        print("*", end=" ")
    print()

for fila in range(1, 3):
    for columna in range(1, 3):
        print(fila, columna)

for i in range(1, 4):
    for j in range(1, 4):
        resultado = i * j
        print(i, "x", j, "=", resultado)
        