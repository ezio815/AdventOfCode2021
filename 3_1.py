lista = []
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

print(f"Gamma: {gamma}, Epsilon: {epsilon}, Power Consumption: {gamma * epsilon}")