pairs = []
with open('input.txt') as data:
    pairs = [[[int(value) for value in assignment.split("-")] for assignment in line.split(",")] for line in data.readlines()]

print("Part 1:")

containedCount = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if elf1[0] > elf2[0]:
        elf1 = pair[1]
        elf2 = pair[0]
    elif elf1[0] == elf2[0] and elf2[1] > elf1[1]:
        elf1 = pair[1]
        elf2 = pair[0]
    if elf2[1] <= elf1[1]:
        containedCount += 1

print(containedCount)

print("Part 2:")

containedCount = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if elf1[0] > elf2[0]:
        elf1 = pair[1]
        elf2 = pair[0]
    if elf1[1] >= elf2[0]:
        containedCount += 1

print(containedCount)
