entry = list(map(int, input().split(",")))

greatest = "x"
smallest = "x"
for i in entry:
    if greatest == "x" and smallest == "x":
        greatest = i
        smallest = i
    elif i < smallest: 
            smallest = i
    elif i > greatest:
            greatest = i

min = "x"
for i in range(smallest, greatest + 1):
    sum = 0
    for j in entry:
        sum += abs(j - i)
    if min == "x":
        min = sum
    elif sum < min:
        min = sum
    
print(f"The least fuel cost is: {min}")
