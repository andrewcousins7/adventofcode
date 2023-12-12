space = []
with open("input.txt", "r") as f:
    for line in f:
        space.append(list(line.strip()))


# # expand space_grid
# def expand_space(space_grid):
#     expandable_x_indexes = []
#     expandable_y_indexes = []
#     for x in range(len(space_grid)):
#         row = space_grid[x]
#         if "#" not in row:
#             expandable_x_indexes.append(x)
#
#     for y in range(len(space_grid[0])):
#         column = [row[y] for row in space_grid]
#         if "#" not in column:
#             expandable_y_indexes.append(y)
#
#     # iterate backwards through expandable indexes
#     # so that the indexes don't change as we insert
#     expandable_x_indexes.reverse()
#     expandable_y_indexes.reverse()
#
#     for x in expandable_x_indexes:
#         space_grid.insert(x, ["." for _ in range(len(space_grid[0]))])
#
#     for y in expandable_y_indexes:
#         for row in space_grid:
#             row.insert(y, ".")
#
#     return space_grid
#
#
# expanded_space = expand_space(space.copy())
#
# galaxies = []
# for x in range(len(expanded_space)):
#     for y in range(len(expanded_space[0])):
#         if expanded_space[x][y] == "#":
#             galaxies.append([x, y])
#
#
#
#
#
# total_distance = 0
# for g in range(len(galaxies)):
#     for h in range(g + 1, len(galaxies)):
#         # print(g+1, h+1, get_distance(galaxies[g], galaxies[h]))
#         total_distance += get_distance(galaxies[g], galaxies[h])
#
# print(total_distance)

expandable_x_indexes = []
expandable_y_indexes = []
for x in range(len(space)):
    row = space[x]
    if "#" not in row:
        expandable_x_indexes.append(x)

for y in range(len(space[0])):
    column = [row[y] for row in space]
    if "#" not in column:
        expandable_y_indexes.append(y)



def get_galaxy_location(x, y):
    multiplier = 1000000-1
    x_multiplier = 0
    for x_index in expandable_x_indexes:
        if x_index < x:
            x_multiplier += multiplier
    y_multiplier = 0
    for y_index in expandable_y_indexes:
        if y_index < y:
            y_multiplier += multiplier
    return [x + x_multiplier, y + y_multiplier]


galaxies = []
for x in range(len(space)):
    for y in range(len(space[0])):
        if space[x][y] == "#":
            galaxies.append(get_galaxy_location(x, y))


def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


total_distance = 0
for g in range(len(galaxies)):
    for h in range(g + 1, len(galaxies)):
        total_distance += get_distance(galaxies[g], galaxies[h])

print(total_distance)
