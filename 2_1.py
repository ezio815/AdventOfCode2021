texto = input()
aim = 0
profundidad = 0
distancia = 0
while texto != ".":
    cantidad = int(texto[-1])
    if "forward" in texto:
        distancia += cantidad
        profundidad += cantidad * aim
    if "down" in texto:
        aim += cantidad
    if "up" in texto:
        aim -= cantidad
    texto = input()
print(f"\nTeniendo {profundidad} de profundidad y {distancia} de distancia\nEl resultado final es: {profundidad * distancia}")