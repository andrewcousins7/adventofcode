dots = []
folds = []
isFolds = False
with open("data.txt") as data:
    for line in data.read().splitlines():
        if line == '':
            isFolds = True
        elif isFolds:
            xy, lineNumber = line.split(" ")[2].split("=")
            folds.append({'dir': xy, 'line': int(lineNumber)})
        else:
            dots.append([int(v) for v in line.split(",")])

grid = [[False for _ in range(max(y for x, y in dots)+1)] for _ in range(max(x for x, y in dots)+1)]

for dot in dots:
    grid[dot[0]][dot[1]] = True


# debug - but actually used for part 2.
def printGrid(grid):
    for y in range(len(grid[0])):
        line = ''
        for x in range(len(grid)):
            if grid[x][y]:
                line += '#'
            else:
                line += '.'
        print(line)


part1 = True
for fold in folds:
    xMax = len(grid)
    yMax = len(grid[0])
    line = fold['line']
    dir = fold['dir']
    foldedLines = 0
    if dir == 'x':
        foldedLines = (xMax - line)
        xMax -= foldedLines
    else:
        foldedLines = (yMax - line)
        yMax -= foldedLines
    newGrid = [[False for _ in range(yMax)] for _ in range(xMax)]

    # copy over old grid
    for x in range(xMax):
        for y in range(yMax):
            newGrid[x][y] = grid[x][y]

    # folded points
    if dir == 'x':
        for x in range(xMax + 1, xMax + foldedLines):
            for y in range(yMax):
                foldedX = line - (x - line)
                if grid[x][y]:
                    newGrid[foldedX][y] = True
    else:
        for x in range(xMax):
            for y in range(yMax + 1, yMax + foldedLines):
                foldedY = line - (y - line)
                if grid[x][y]:
                    newGrid[x][foldedY] = True

    grid = newGrid

    # count points
    count = 0
    for x in range(xMax):
        for y in range(yMax):
            if grid[x][y]:
                count += 1
    #printGrid(grid)
    if part1:
        print("Part 1")
        print(count)
        part1 = False

print("Part 2")
printGrid(grid)




