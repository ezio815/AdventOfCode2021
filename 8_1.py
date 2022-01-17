entry = input()
segments = []
while entry != ".":
    segments.extend(entry.split(" | ")[1].split(" "))
    entry = input()

unique = [2, 3, 4, 7]
result = 0

for i in segments:
    if len(i) in unique:
        result += 1

print(f"The result is: {result}")
