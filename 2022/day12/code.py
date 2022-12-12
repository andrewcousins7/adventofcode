heightmap = []
with open('input.txt') as data:
    heightmap = [[tile for tile in line.strip()] for line in data.readlines()]

dirs = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]

numCols = len(heightmap)
numRows = len(heightmap[0])
print("Part 1:")
status_map = [["u" for i in range(numRows)] for j in range(numCols)]
search_queue = []
for r in range(numCols):
    for c in range(numRows):
        if heightmap[r][c] == "S":
            search_queue.append([r, c])
            status_map[r][c] = 0


def get_adjacent_locations(graph, location):
    adjacents = []
    for dir in dirs:
        new_coords = [location[0] + dir[0], location[1] + dir[1]]
        if 0 <= new_coords[0] < numCols and 0 <= new_coords[1] < numRows:
            adjacents.append(new_coords)
    return adjacents


def is_valid_movement(start, dest):
    if start == "S":
        start = "a"
    if dest == "E":
        dest = "z"
    return ord(dest) <= ord(start) + 1


def print_map(toprint):
    for line in toprint:
        print(line)


while len(search_queue) > 0:
    search_start = search_queue.pop(0)
    currentHeight = heightmap[search_start[0]][search_start[1]]
    stepCount = status_map[search_start[0]][search_start[1]] + 1
    for adjacent_location in get_adjacent_locations(heightmap, search_start):
        if status_map[adjacent_location[0]][adjacent_location[1]] == "u":
            if is_valid_movement(currentHeight, heightmap[adjacent_location[0]][adjacent_location[1]]):
                if heightmap[adjacent_location[0]][adjacent_location[1]] == "E":
                    print(stepCount)
                    break
                status_map[adjacent_location[0]][adjacent_location[1]] = stepCount
                search_queue.append(adjacent_location)

print("Part 2:")
status_map = [["u" for i in range(numRows)] for j in range(numCols)]
search_queue = []
for r in range(numCols):
    for c in range(numRows):
        if heightmap[r][c] == "S" or heightmap[r][c] == "a":
            search_queue.append([r, c])
            status_map[r][c] = 0

while len(search_queue) > 0:
    search_start = search_queue.pop(0)
    currentHeight = heightmap[search_start[0]][search_start[1]]
    stepCount = status_map[search_start[0]][search_start[1]] + 1
    for adjacent_location in get_adjacent_locations(heightmap, search_start):
        if status_map[adjacent_location[0]][adjacent_location[1]] == "u":
            if is_valid_movement(currentHeight, heightmap[adjacent_location[0]][adjacent_location[1]]):
                if heightmap[adjacent_location[0]][adjacent_location[1]] == "E":
                    print(stepCount)
                    break
                status_map[adjacent_location[0]][adjacent_location[1]] = stepCount
                search_queue.append(adjacent_location)