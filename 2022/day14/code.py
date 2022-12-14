wallPaths = []
with open('input.txt') as data:
    for line in data.readlines():
        points = line.strip().split(" -> ")
        wallPaths.append([coordinate.split(",") for coordinate in points])

leftMostPoint = 500
rightMostPoint = 500
lowestPoint = 0
for lines in wallPaths:
    for point in lines:
        y = int(point[0])
        x = int(point[1])
        if y < leftMostPoint:
            leftMostPoint = y
        if y > rightMostPoint:
            rightMostPoint = y
        if x > lowestPoint:
            lowestPoint = x


def print_grid(g):
    i = 0
    for line in g:
        output = str(i) + " "
        i += 1
        for c in line:
            output += c
        print(output)


def get_x(x, left_most_point):
    return x - left_most_point


def add_wall(wall_points, g, left_most_point):
    curr_x = None
    curr_y = None
    for point in wall_points:
        x = get_x(int(point[0]), left_most_point)
        y = int(point[1])
        if curr_x is None:
            curr_x = x
            curr_y = y
        else:
            while x != curr_x or y != curr_y:
                g[curr_y][curr_x] = "#"
                if curr_x < x:
                    curr_x += 1
                if curr_x > x:
                    curr_x -= 1
                if curr_y < y:
                    curr_y += 1
                if curr_y > y:
                    curr_y -= 1
            g[curr_y][curr_x] = "#"


def add_sand(g, ox, oy):
    oy += 1
    if oy >= len(g):
        return False
    if g[oy][ox] == ".":
        return add_sand(g, ox, oy)
    if ox - 1 < 0:
        return False
    if g[oy][ox - 1] == ".":
        return add_sand(g, ox - 1, oy)
    if ox + 1 >= len(g[oy]):
        return False
    if g[oy][ox + 1] == ".":
        return add_sand(g, ox + 1, oy)
    g[oy - 1][ox] = "o"
    return True


print("Part 1:")
lowestPoint += 1
grid = [["." for i in range(rightMostPoint - leftMostPoint + 1)] for j in range(lowestPoint)]

originX = get_x(500, leftMostPoint)
originY = 0
grid[originY][originX] = "+"

for wall in wallPaths:
    add_wall(wall, grid, leftMostPoint)

print_grid(grid)

sandAdded = 0
while add_sand(grid, originX, originY):
    sandAdded += 1
print_grid(grid)
print(sandAdded)

print("Part 2:")
leftMostPoint = 0
rightMostPoint = 1000
lowestPoint += 2

grid = [["." for i in range(rightMostPoint - leftMostPoint + 1)] for j in range(lowestPoint)]

originX = get_x(500, leftMostPoint)
originY = 0
grid[originY][originX] = "+"

for wall in wallPaths:
    add_wall(wall, grid, leftMostPoint)
add_wall([[leftMostPoint, lowestPoint - 1], [rightMostPoint, lowestPoint - 1]], grid, leftMostPoint)

print_grid(grid)

sandAdded = 0
while grid[originY][originX] != "o":
    add_sand(grid, originX, originY)
    sandAdded += 1
print_grid(grid)
print(sandAdded)
