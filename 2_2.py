texto = input()
profundidad = 0
distancia = 0
while texto != ".":
    cantidad = int(texto[-1])
    if "forward" in texto:
        distancia += cantidad
    if "down" in texto:
        profundidad += cantidad
    if "up" in texto:
        profundidad -= cantidad
    texto = input()
print(f"\nTeniendo {profundidad} de produndidad y {distancia} de distancia\nEl resultado final es: {profundidad * distancia}")