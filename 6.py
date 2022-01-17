entry = input()
fishes = entry.split(",")
for x in range(len(fishes)):
    fishes[x] = int(fishes[x])

result = 0
state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in fishes:
    state[i] += 1

for i in range(256):
    aux = state[0] 
    for j in range(8):
        state[j] = state[j + 1]
    state[6] += aux
    state[8] = aux

for i in state:
    result += i

print(f"The result is: {result}")