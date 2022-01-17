entry = input()
segments = []
while entry != ".":
    segments.append(entry.split(" | "))
    for i in range(len(segments)):
        for j in range(2):
            segments[i][j] = segments[i][j].split(" ")
    entry = input()

unique = [2, 3, 4, 7]
result = 0

for i in segments:
    segments_2 = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : []}
    for j in i[0]:
        if len(j) == 2:
            for k in j:
                if not k in segments_2[2]:
                    segments_2[2].append(k)
                if not k in segments_2[3]:
                    segments_2[3].append(k)
        if len(j) == 3:
            for k in j:
                if k in segments_2[2] or k in segments_2[3]:

    """for j in i[0]:
        if len(j) in unique:
            for k in j:
                if k not in segments_2:
                    segments_2.append(k)"""

print(f"The result is: {result}")

print(segments)

#[["ecbad fdeacg gaecbd gbae gfcdbea cadge fcagdb abc cfdbe ab", "beag bac dacgbe aegb"]]