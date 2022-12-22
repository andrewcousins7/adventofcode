mapRows = []
mapRowOffsets = []
steps = []
with open('input.txt') as data:
    readingMap = True
    for line in data.readlines():
        if readingMap:
            if line.strip() == "":
                readingMap = False
            else:
                row = []
                offsetAmount = 0
                for char in line:
                    if char == " ":
                        offsetAmount += 1
                    elif char != "\n":
                        row.append(char)
                mapRows.append(row)
                mapRowOffsets.append(offsetAmount)

        else:
            line = line.strip()
            step = ""
            for char in line:
                if char == "R" or char == "L":
                    if step != "":
                        steps.append(step)
                    steps.append(char)
                    step = ""
                else:
                    step += char
            if step != "":
                steps.append(step)


def get_tile(column, row):
    if row < 0 or row >= len(mapRows):
        return False
    row_data = mapRows[row]
    offset = mapRowOffsets[row]
    if column < offset or column >= offset + len(row_data):
        return False
    return row_data[column - offset]


def try_to_move(col, row, dir):
    if dir == 0 or dir == 2:
        if dir == 0:
            col += 1
        else:
            col -= 1

        row_data = mapRows[row]
        offset = mapRowOffsets[row]
        tile = get_tile(col, row)
        if tile is False:
            if col >= len(row_data) + offset:
                col = mapRowOffsets[row]
            if col < offset:
                col = len(row_data) + offset - 1
            tile = get_tile(col, row)
        if tile == ".":
            return col, row
        if tile == "#":
            return False
    else:
        if dir == 3:
            row -= 1
        else:
            row += 1

        tile = get_tile(col, row)
        while tile is False:
            if row >= len(mapRows):
                row = 0
            elif row < 0:
                row = len(mapRows) - 1
            elif dir == 3:
                row -= 1
            else:
                row += 1
            tile = get_tile(col, row)
        if tile == ".":
            print(col, row)
            return col, row
        if tile == "#":
            return False


print("Part 1:")
curr_row = 0
curr_col = 0
while (not get_tile(curr_col, curr_row)) and get_tile(curr_col, curr_row) != "#":
    curr_col += 1
facing = 0

for step in steps:
    print(curr_col, curr_row, facing, step)
    if step == "R":
        facing += 1
        if facing > 3:
            facing = 0
    elif step == "L":
        facing -= 1
        if facing < 0:
            facing = 3
    else:
        for i in range(int(step)):
            if try_to_move(curr_col, curr_row, facing):
                curr_col, curr_row = try_to_move(curr_col, curr_row, facing)

solution = (1000 * (curr_row + 1)) + (4 * (curr_col + 1)) + facing
print(solution)


def turn(dir, turn):
    if turn == "R":
        dir += 1
        if dir > 3:
            dir = 0
    elif turn == "L":
        dir -= 1
        if dir < 0:
            dir = 3
    return dir


cubeSize = 50


def try_to_cube(col, row, dir):
    if dir == 0 or dir == 2:
        if dir == 0:
            col += 1
        else:
            col -= 1

        tile = get_tile(col, row)
        if tile is False:
            if col < 0:
                if row < cubeSize*3:
                    row = cubeSize*3 - 1 - row
                    col = cubeSize
                    dir = 0
                else:
                    col = cubeSize + (row - cubeSize*3)
                    row = 0
                    dir = 1
            elif col < cubeSize:
                if row < cubeSize:
                    row = cubeSize*2 + (cubeSize - 1 - row)
                    col = 0
                    dir = 0
                elif row < cubeSize*2:
                    col = (row - cubeSize)
                    row = cubeSize*2
                    dir = 1
            elif col < cubeSize*2:
                if row < cubeSize*3:
                    print("ERROR", col, row, dir)
                else:
                    col = cubeSize + (row - cubeSize*3)
                    row = cubeSize*3 - 1
                    dir = 3
            elif col < cubeSize*3:
                if row < cubeSize:
                    print("ERROR", col, row, dir)
                elif row < cubeSize*2:
                    col = cubeSize*2 + (row - cubeSize)
                    row = cubeSize - 1
                    dir = 3
                elif row < cubeSize*3:
                    row = cubeSize*3 - 1 - row
                    col = cubeSize*3 - 1
                    dir = 2
            else:
                if row < cubeSize*3:
                    row = cubeSize*3 - 1 - row
                    col = cubeSize*2 - 1
                    dir = 2
                else:
                    print("ERROR", col, row, dir)
            tile = get_tile(col, row)
        if tile == ".":
            return col, row, dir
        if tile == "#":
            return False
    else:
        if dir == 3:
            row -= 1
        else:
            row += 1

        tile = get_tile(col, row)
        if tile is False:
            if row < 0:
                if col < cubeSize*2:
                    row = cubeSize*3 + (col - cubeSize)
                    col = 0
                    dir = 0
                elif col < cubeSize*3:
                    col = col - cubeSize*2
                    row = cubeSize*4 - 1
                    dir = 3
            elif row < cubeSize:
                print("ERROR", col, row, dir)
            elif row < cubeSize*2:
                if col < cubeSize:
                    row = cubeSize + col
                    col = cubeSize
                    dir = 0
                elif col < cubeSize*2:
                    print("ERROR", col, row, dir)
                elif col < cubeSize*3:
                    row = cubeSize + (col - cubeSize*2)
                    col = cubeSize*2 - 1
                    dir = 2
            elif row < cubeSize*3:
                print("ERROR", col, row, dir)
            elif row < cubeSize*4:
                if col < cubeSize:
                    print("ERROR", col, row, dir)
                elif col < cubeSize*2:
                    row = cubeSize*3 + (col - cubeSize)
                    col = cubeSize - 1
                    dir = 2
            else:
                col = cubeSize * 2 + col
                row = 0
                dir = 1
            tile = get_tile(col, row)
        if tile == ".":
            return col, row, dir
        if tile == "#":
            return False


print("Part 2:")
curr_row = 0
curr_col = 0
while (not get_tile(curr_col, curr_row)) and get_tile(curr_col, curr_row) != "#":
    curr_col += 1
facing = 0

for step in steps:
    if step == "R" or step == "L":
        facing = turn(facing, step)
    else:
        for i in range(int(step)):
            if try_to_cube(curr_col, curr_row, facing):
                curr_col, curr_row, facing = try_to_cube(curr_col, curr_row, facing)

solution = (1000 * (curr_row + 1)) + (4 * (curr_col + 1)) + facing
print(solution)

# for r in range(cubeSize*4):
#     for c in range(cubeSize*3):
#         if get_tile(c, r):
#             for f in range(4):
#                 if try_to_cube(c, r, f):
#                     dc, dr, df = try_to_cube(c, r, f)
#                 else:
#                     print("failed1", c, r, f)
#                 df = (df + 2) % 4
#                 if try_to_cube(dc, dr, df):
#                     dc, dr, df = try_to_cube(dc, dr, df)
#                 else:
#                     print("failed2", c, r, f)
#                 df = (df + 2) % 4
#                 if c != dc or r != dr or f != df:
#                     print("failed3", c, r, f)
