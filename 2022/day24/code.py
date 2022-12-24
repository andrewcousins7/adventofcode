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


def print_grid(grid, moves):
    for r in range(len(grid)):
        row = grid[r]
        o = ""
        for c in range(len(row)):
            cell = row[c]
            if [c, r] in moves:
                o += "E"
            else:
                o += cell.get_char()
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
    if grid[r][c].is_wall:
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


def location_in_grid(location, grid):
    if 0 <= location[1] < len(grid):
        if 0 <= location[0] < len(grid[location[1]]):
            return True
    return False


def get_next_moves(location, grid):
    dir_mod = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
        [0, 0]
    ]
    moves = []
    for mod in dir_mod:
        new_c = location[0] + mod[0]
        new_r = location[1] + mod[1]
        if location_in_grid([new_c, new_r], grid):
            cell = grid[new_r][new_c]
            if not (cell.is_wall or cell.has_blizzards()):
                moves.append([new_c, new_r])
    return moves


def is_exit(location, end_location):
    return location[0] == end_location[0] and location[1] == end_location[1]


def find_time_to_exit(valley, start_location, end_location):
    #print_grid(valley, [start_location])
    next_step_moves = [start_location]
    current_step = 1
    while len(next_step_moves) > 0:
        #print(next_step_moves)
        #print("Searching for moves during", current_step, "minute...")
        valley = simulate_blizzards(valley)
        moves_to_search = copy.deepcopy(next_step_moves)
        next_step_moves = []
        for move in moves_to_search:
            valid_moves = get_next_moves(move, valley)
            for future_move in valid_moves:
                if is_exit(future_move, end_location):
                    print("Exited:", current_step)
                    return current_step, valley
                if future_move not in next_step_moves:
                    next_step_moves.append(future_move)
        #print_grid(valley, next_step_moves)
        current_step += 1


print("Part 1:")
exit_row = len(valley) - 1
exit_col = len(valley[exit_row]) - 2
start_row = 0
start_col = 1
there, valley = find_time_to_exit(valley, [start_col, start_row], [exit_col, exit_row])
back, valley = find_time_to_exit(valley, [exit_col, exit_row], [start_col, start_row])
andThereAgain, valley = find_time_to_exit(valley, [start_col, start_row], [exit_col, exit_row])
print(there + back + andThereAgain)
