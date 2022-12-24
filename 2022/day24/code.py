import copy


class Cell:
    def __init__(self, starting_value):
        self.blizzards = []
        self.is_wall = starting_value == "#"
        if starting_value != "." and starting_value != "#":
            self.blizzards.append(starting_value)

    def get_char(self):
        if self.is_wall:
            return "#"
        if len(self.blizzards) == 0:
            return "."
        if len(self.blizzards) == 1:
            return self.blizzards[0]
        return str(len(self.blizzards))

    def has_blizzards(self):
        return len(self.blizzards) > 0

    def get_next_blizzard(self):
        blizzard = self.blizzards.pop()
        return blizzard

    def add_blizzard(self, blizzard):
        self.blizzards.append(blizzard)

valley = []
with open('input.txt') as data:
    for line in data.readlines():
        valley.append([Cell(c) for c in line.strip()])


def print_grid(grid):
    for line in grid:
        o = ""
        for c in line:
            o += c.get_char()
        print(o)


def move_blizzard(grid, blizz, c, r):
    dir_mod = {
        "^": [0, -1],
        "v": [0, 1],
        "<": [-1, 0],
        ">": [1, 0]
    }
    c += dir_mod[blizz][0]
    r += dir_mod[blizz][1]
    print(blizz, c, r)
    if grid[r][c].is_wall:
        print("is wall")
        if blizz == "^":
            r = len(grid)-2
        if blizz == "v":
            r = 1
        if blizz == "<":
            c = len(grid[r])-2
        if blizz == ">":
            c = 1
    grid[r][c].add_blizzard(blizz)


def copy_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            value = "."
            if cell.is_wall:
                value = "#"
            new_row.append(Cell(value))
        new_grid.append(new_row)
    return new_grid


def simulate_blizzards(grid):
    future_grid = copy_grid(grid)
    for r in range(len(grid)):
        row = grid[r]
        for c in range(len(row)):
            cell = row[c]
            while cell.has_blizzards():
                blizzard = cell.get_next_blizzard()
                move_blizzard(future_grid, blizzard, c, r)
    return future_grid


print("Part 1:")
print_grid(valley)




next_step_moves = []
for i in range(18):
    print("Minute", i+1)
    valley = simulate_blizzards(valley)
    print_grid(valley)
