entry = input()
text = ""
while entry != ".":
    text += f"{entry}\n"
    entry = input()

lines = text.splitlines()
lines_2 = []
for i in lines:
    lines_2.append(i.split(" -> "))
lines = lines_2

for i in range(0, len(lines)):
    for j in range(0, 2):
        lines[i][j] = lines[i][j].split(",")

numbers = {}

for i in lines:
    if i[0][0] == i[1][0]:
        base = i[0][0]
        if int(i[0][1]) < int(i[1][1]):
            smaller = int(i[0][1])
            greater = int(i[1][1])
        else:
            smaller = int(i[1][1])
            greater = int(i[0][1])

        for j in range(0, greater - smaller + 1):
            if f"{base},{smaller + j}" in numbers:
                numbers[f"{base},{smaller + j}"] += 1  
            else: numbers[f"{base},{smaller + j}"] = 1

    elif i[0][1] == i[1][1]:
        base = i[0][1]
        if int(i[0][0]) < int(i[1][0]):
            smaller = int(i[0][0])
            greater = int(i[1][0])
        else:
            smaller = int(i[1][0])
            greater = int(i[0][0])

        for j in range(0, greater - smaller + 1):
            if f"{smaller + j},{base}" in numbers:
                numbers[f"{smaller + j},{base}"] += 1  
            else: numbers[f"{smaller + j},{base}"] = 1

result = 0
for i in numbers.keys():
    if numbers[i] >= 2:
        result += 1

print(f"\nThe result is: {result}")