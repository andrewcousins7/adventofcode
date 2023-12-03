# read input.txt as a 2d array
input = []
for line in open('input.txt', 'r').readlines():
    input.append(list(line.strip()))

# checks if a character is a symbol
# a symbol is any character that is not a number and is not a .
def is_symbol(char):
    return not char.isdigit() and char != '.'

# Checks if a cell has an adjacent symbol
def has_adjacent_symbol(input, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            if x+i < 0 or y+j < 0: continue
            if x+i >= len(input) or y+j >= len(input[0]): continue
            if is_symbol(input[x+i][y+j]): return True
    return False

# Checks if a part is valid
# takes coordinates, and then checks if that coordinate or any following number is a symbol
def is_part_number(input, x, y):
    while input[x][y].isdigit():
        if has_adjacent_symbol(input, x, y):
            return True
        y += 1
        if y >= len(input[x]):
            return False

def get_part_number(input, x, y):
    part_number = ''
    while input[x][y].isdigit():
        part_number += input[x][y]
        y += 1
        if y >= len(input[x]):
            break
    return part_number

total = 0
for line in input:
    i = 0
    while i < len(line):
        if line[i].isdigit():
            if is_part_number(input, input.index(line), i):
                part_number = get_part_number(input, input.index(line), i)
                total += int(part_number)
                i += len(part_number) - 1
        i += 1

print(total)


# Part 2
# gears is a 3d array matching the input array
gears = []
for i in range(len(input)):
    gears.append([])
    for j in range(len(input[i])):
        gears[i].append([])

def has_get_gears(input, x, y):
    adjacent_gears = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            if x+i < 0 or y+j < 0: continue
            if x+i >= len(input) or y+j >= len(input[0]): continue
            if input[x+i][y+j] == "*": adjacent_gears.append((x+i, y+j))
    return adjacent_gears

def add_to_gears(input, x, y, part_number):
    all_gears = []
    while input[x][y].isdigit():
        adjacent_gears = has_get_gears(input, x, y)
        for gear in adjacent_gears:
            if gear not in all_gears:
                all_gears.append(gear)
        y += 1
        if y >= len(input[x]):
            break
    for gear in all_gears:
        gears[gear[0]][gear[1]].append(part_number)

for line in input:
    i = 0
    while i < len(line):
        if line[i].isdigit():
            if is_part_number(input, input.index(line), i):
                part_number = get_part_number(input, input.index(line), i)
                add_to_gears(input, input.index(line), i, part_number)
                i += len(part_number) - 1
        i += 1

total = 0
for i in range(len(gears)):
    for j in range(len(gears[i])):
        if len(gears[i][j]) == 2:
            gear_ration = int(gears[i][j][0]) * int(gears[i][j][1])
            total += gear_ration
print(total)
