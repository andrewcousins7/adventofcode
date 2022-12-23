class Elf:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.planned_col = None
        self.planned_row = None

    def plan_move(self, direction_list):
        self.planned_col = self.col
        self.planned_row = self.row
        is_alone = True
        for dir in ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]:
            if not is_empty_in_direction(self.col, self.row, dir):
                is_alone = False
                break
        if is_alone:
            return
        for dir in direction_list:
            if is_empty_in_general_direction(self.col, self.row, dir):
                #print(self.col, self.row, "planning to move", dir)
                self.planned_col = self.col + direction_modifiers[dir][0]
                self.planned_row = self.row + direction_modifiers[dir][1]
                return

    def execute_move(self, planned_locations):
        if self.col != self.planned_col or self.row != self.planned_row:
            loc = loc_to_str(self.planned_col, self.planned_row)
            if planned_locations[loc] == 1:
                #print("moving from", self.col, self.row, "to", self.planned_col, self.planned_row)
                elf_locations.remove(loc_to_str(self.col, self.row))
                elf_locations.append(loc)
                self.col = self.planned_col
                self.row = self.planned_row
                return True
        return False


def loc_to_str(col, row):
    return str(col) + "," + str(row)


elves = []
elf_locations = []
with open('input.txt') as data:
    row = 0
    for line in data.readlines():
        col = 0
        for char in line:
            if char == "#":
                elves.append(Elf(col, row))
                elf_locations.append(loc_to_str(col, row))
            col += 1
        row += 1


direction_modifiers = {
    "N": [0, -1],
    "S": [0, 1],
    "E": [1, 0],
    "W": [-1, 0]
}


def is_elf_in_space(elf, col, row):
    if elf.col == col and elf.row == row:
        return True
    return False


def is_empty_in_direction(col, row, dir):
    mod = [0, 0]
    for d in dir:
        for i in range(2):
            mod[i] += direction_modifiers[d][i]
    target_col = col + mod[0]
    target_row = row + mod[1]
    if loc_to_str(target_col, target_row) in elf_locations:
        return False
    return True


def is_empty_in_general_direction(col, row, dir):
    general_directions = {
        "N": ["NE", "N", "NW"],
        "S": ["SE", "S", "SW"],
        "E": ["NE", "E", "SE"],
        "W": ["NW", "W", "SW"]
    }
    for d in general_directions[dir]:
        if not is_empty_in_direction(col, row, d):
            return False
    return True






print("Part 1:")
ordered_directions = ["N", "S", "W", "E"]
for s in range(10):
    planned_moves = {}
    for elf in elves:
        elf.plan_move(ordered_directions)
        loc = loc_to_str(elf.planned_col, elf.planned_row)
        if loc not in planned_moves:
            planned_moves[loc] = 0
        planned_moves[loc] += 1
    for elf in elves:
        elf.execute_move(planned_moves)
    ordered_directions.append(ordered_directions.pop(0))

minCol = elves[0].col
maxCol = minCol
minRow = elves[0].row
maxRow = minRow
for elf in elves:
    # print(elf.col, elf.row)
    minCol = min(minCol, elf.col)
    minRow = min(minRow, elf.row)
    maxCol = max(maxCol, elf.col)
    maxRow = max(maxRow, elf.row)
areaSize = (maxCol - minCol + 1) * (maxRow - minRow + 1)
print(areaSize - len(elves))

for r in range(maxRow - minRow + 1):
    line = ""
    for c in range(maxCol - minCol + 1):
        space = "."
        for elf in elves:
            if is_elf_in_space(elf, c+ minCol, r+minRow):
                space = "#"
        line += space
    print(line)

print("Part 2:")
elf_moved = True
roundCount = 10
while elf_moved:
    print(roundCount)
    elf_moved = False
    roundCount += 1
    planned_moves = {}
    for elf in elves:
        elf.plan_move(ordered_directions)
        loc = loc_to_str(elf.planned_col, elf.planned_row)
        if loc not in planned_moves:
            planned_moves[loc] = 0
        planned_moves[loc] += 1
    for elf in elves:
        if elf.execute_move(planned_moves):
            elf_moved = True
    ordered_directions.append(ordered_directions.pop(0))
print(roundCount)
