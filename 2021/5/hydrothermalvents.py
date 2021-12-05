data = []
with open('data.txt') as data:
    data = [[[int(a) for a in pair.split(",")] for pair in value.split(" -> ")] for value in data.read().splitlines()]

ventsSize = max(max(max(coordinates) for coordinates in pair) for pair in data) + 1

print("Part 1")

vents = [[0] * ventsSize for _ in range(ventsSize)]
count = 0

for ventLine in data:
    x1 = ventLine[0][0]
    y1 = ventLine[0][1]
    x2 = ventLine[1][0]
    y2 = ventLine[1][1]

    if x1 == x2 or y1 == y2:
        while True:
            vents[x1][y1] += 1
            if vents[x1][y1] == 2:
                count += 1

            if x1 == x2 and y1 == y2:
                break

            if x2 > x1:
                x1 += 1
            elif x2 < x1:
                x1 -= 1
            if y2 > y1:
                y1 += 1
            elif y2 < y1:
                y1 -= 1


print(count)

print("Part 2")

vents = [[0] * ventsSize for _ in range(ventsSize)]
count = 0

for ventLine in data:
    x1 = ventLine[0][0]
    y1 = ventLine[0][1]
    x2 = ventLine[1][0]
    y2 = ventLine[1][1]

    while True:
        vents[x1][y1] += 1
        if vents[x1][y1] == 2:
            count += 1

        if x1 == x2 and y1 == y2:
            break

        if x2 > x1:
            x1 += 1
        elif x2 < x1:
            x1 -= 1
        if y2 > y1:
            y1 += 1
        elif y2 < y1:
            y1 -= 1

print(count)
