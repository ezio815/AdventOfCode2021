entrada_1 = input()
entrada_2 = input()
cantidad = 0

while entrada_2 != ".":
    if entrada_1 < entrada_2:
        cantidad += 1
    entrada_1 = entrada_2
    entrada_2 = input()

print("\nLa cantidad es:",cantidad)