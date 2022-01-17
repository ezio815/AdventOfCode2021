"""lista = []
gamma = 0
epsilon = 0
entrada = input()
for letra in entrada:
    lista.append({"ceros" : 0, "unos" : 0})

while entrada != ".":
    for i in range(0, len(lista)):
        if entrada[i] == "0":
            lista[i]["ceros"] += 1
        else:
            lista[i]["unos"] += 1
    entrada = input()

contador = len(lista)-1
for lugar in lista:
    if lugar["ceros"] < lugar["unos"]:
        gamma += 2**contador
    else:
        epsilon += 2**contador
    contador -= 1

print(f"Gamma: {gamma}, Epsilon: {epsilon}, Power Consumption: {gamma * epsilon}")"""

lista = []
entrada = input()
while entrada != ".":
    lista.append(entrada)
    entrada = input()

def calcular(lista, tipo):
    for i in range(0, len(entrada)):
        contador = 0
        for numero in lista:
            if numero[i] == 1:
                contador += 1

        if contador >= len(lista):
            mas = "1"
            menos = "0"
        else:
            mas = "0"
            menos = "1"

        if tipo == 1:
            for indice in range(0, len(lista)):
                if lista[indice][i] != mas and len(lista) > 1:
                    lista.pop(indice)
                else:
                    break
        else:
            for indice in range(0, len(lista)):
                if len(lista) > 1:
                    if lista[indice][i] != menos:
                        lista.pop(indice)
                else:
                    break

    return lista[0]

mas = calcular(lista, 1)
menos = calcular(lista, 0)

print(f"Oxygen: {mas}, CO2: {menos}")