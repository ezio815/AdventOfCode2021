aumentos = 0
cantidad_1 = 0
entrada = input()
lista = []
while entrada != ".":
    lista.append(int(entrada))
    entrada = input()

for i in range(0, 3):
    cantidad_1 += lista[i]
i = 1
while len(lista) > i + 2:
    cantidad_2 = 0
    for j in range(0, 3):
        cantidad_2 += lista[i + j]
    if cantidad_2 > cantidad_1:
        aumentos += 1
    cantidad_1 = cantidad_2
    i += 1

print("\nLa cantidad de aumentos es:",aumentos)