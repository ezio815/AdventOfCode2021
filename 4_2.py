from asyncio.windows_events import NULL
winner = NULL

entry = input()
numbers = entry.split(",")

text = ""

for i in range(0, 2):
    entry = input()

while entry != ".":
    text += f"{entry}\n"
    entry = input()

lines = text.splitlines()
boards = []

count = 0
count_2 = 0
boards.append([])
for i in range(0, len(lines)):
    if lines[i] == "":
        count += 1
        count_2 = 0
        boards.append([])

    else:
        places = lines[i].split(" ")
        while "" in places:
            places.pop(places.index(""))
        
        if count_2 == 0:
            boards[count] = [[], [], [], [], []]
        boards[count][count_2] = places
        count_2 += 1

lastNum = 0

for x in numbers:
    sum = 0
    count = 0
    for i in range(0, len(boards)):
        b = i - count
        for j in range(0, 5):
            while x in boards[b][j]:
                boards[b][j][boards[b][j].index(x)] = "x"
            for k in range(0, 5):
                if boards[b][j][k] == "x":
                    sum += 1
                else:
                    sum = 0
                    break

            if sum == 0:
                for k in range(0, 5):
                    if boards[b][k][j] == "x":
                        sum += 1
                    else:
                        sum = 0
                        break
            
            if sum == 5 and winner == NULL:
                winner = boards[b]

        if winner != NULL:
            if len(boards) > 1 and len(numbers) - numbers.index(x) > 1:
                #print(f"\n{winner}")
                boards.remove(winner)
                #print(len(boards), x)
                winner = NULL
                b -= 1
                count += 1
            else:
                print(boards.index(winner))
                lastNum = x
                break
    if lastNum != 0:
        break

print(f"\n{boards}")

if winner != NULL:
    result = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if winner[i][j] != "x":
                result += int(winner[i][j])
    result *= int(lastNum)
    print(result)