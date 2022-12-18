cubeList = []
cubeLookup = []
with open('input.txt') as data:
    for cubeData in data.readlines():
        cubeLookup.append(cubeData.strip())
        cubeList.append([int(value) for value in cubeData.strip().split(",")])


def get_cube_key(x, y, z):
    return str(x) + "," + str(y) + "," + str(z)


def get_non_adjacent_side_count(cube):
    x = cube[0]
    y = cube[1]
    z = cube[2]
    non_adjacent_side_count = 0
    for dir in [-1, 1]:
        if get_cube_key(x + dir, y, z) not in cubeLookup:
            non_adjacent_side_count += 1
        if get_cube_key(x, y + dir, z) not in cubeLookup:
            non_adjacent_side_count += 1
        if get_cube_key(x, y, z + dir) not in cubeLookup:
            non_adjacent_side_count += 1
    return non_adjacent_side_count


print("Part 1:")
count = 0
for cube in cubeList:
    count += get_non_adjacent_side_count(cube)
print(count)

print("Part 1:")
maxGraph = [0, 0, 0]
minGraph = [0, 0, 0]
for cube in cubeList:
    for i in range(3):
        maxGraph[i] = max(maxGraph[i], cube[i])
        minGraph[i] = min(minGraph[i], cube[i])

print(minGraph)
print(maxGraph)
searched = []
search_queue = [[0, 0, 0]]
adjacent_sides = 0


def is_valid_cell(x, y, z):
    if minGraph[0]-1 <= x <= maxGraph[0]+1:
        if minGraph[1]-1 <= y <= maxGraph[1]+1:
            if minGraph[2]-1 <= z <= maxGraph[2]+1:
                return True
    return False


def search_cell(x, y, z):
    if is_valid_cell(x, y, z):
        key = get_cube_key(x, y, z)
        if key in cubeLookup:
            return 1
        else:
            if key not in searched:
                search_queue.append([x, y, z])
                searched.append(key)
    return 0


while len(search_queue) > 0:
    cell = search_queue.pop()
    x = cell[0]
    y = cell[1]
    z = cell[2]
    for direction in [-1, 1]:
        adjacent_sides += search_cell(x + direction, y, z)
        adjacent_sides += search_cell(x, y + direction, z)
        adjacent_sides += search_cell(x, y, z + direction)

print(adjacent_sides)
