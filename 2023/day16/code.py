layout = []
for line in open("input.txt").readlines():
    line = line.strip()
    layout.append([c for c in line])

energized = [[[] for j in range(len(layout[0]))] for i in range(len(layout))]


def print_layout(layout, energized):
    energized_count = 0
    for row in range(len(layout)):
        printstr = ""
        for col in range(len(layout[0])):
            if layout[row][col] != ".":
                printstr += layout[row][col]
            elif energized[row][col]:
                if len(energized[row][col]) > 1:
                    printstr += "#"
                else:
                    printstr += energized[row][col][0]
            else:
                printstr += layout[row][col]
            if energized[row][col]:
                energized_count += 1
        print(printstr)
    print(energized_count)


beam_dir_maps = {
    ".": {
        ">": [">"],
        "<": ["<"],
        "^": ["^"],
        "v": ["v"],
    },
    "\\": {
        ">": ["v"],
        "<": ["^"],
        "^": ["<"],
        "v": [">"],
    },
    "/": {
        ">": ["^"],
        "<": ["v"],
        "^": [">"],
        "v": ["<"],
    },
    "|": {
        ">": ["^", "v"],
        "<": ["^", "v"],
        "^": ["^"],
        "v": ["v"],
    },
    "-": {
        ">": [">"],
        "<": ["<"],
        "^": ["<", ">"],
        "v": ["<", ">"],
    },
}
beam_dir_mods = {
    ">": [0, 1],
    "<": [0, -1],
    "^": [-1, 0],
    "v": [1, 0],
}
beams = [[0, 0, ">"]]


def move_beam(beam_list, energized_map):
    beam = beam_list.pop(0)
    beam_dir = beam[2]
    row = beam[0]
    col = beam[1]
    if beam_dir in energized_map[row][col]:
        return beam_list, energized_map
    energized_map[row][col].append(beam_dir)
    new_beam_dirs = beam_dir_maps[layout[row][col]][beam_dir]
    for new_beam_dir in new_beam_dirs:
        mod = beam_dir_mods[new_beam_dir]
        new_row = row + mod[0]
        new_col = col + mod[1]
        if new_row >= 0 and new_col >= 0:
            if new_row < len(layout) and new_col < len(layout[0]):
                beam_list.append([new_row, new_col, new_beam_dir])
    return beam_list, energized_map


while beams:
    beams, energized = move_beam(beams, energized)

print_layout(layout, energized)


def test_layout(initial_x, initial_y, initial_dir):
    energized_map = [[[] for j in range(len(layout[0]))] for i in range(len(layout))]
    beams = [[initial_x, initial_y, initial_dir]]
    while beams:
        beams, energized_map = move_beam(beams, energized_map)
    energized_count = 0
    for row in range(len(layout)):
        for col in range(len(layout[0])):
            if energized_map[row][col]:
                energized_count += 1
    return energized_count

max_energized = 0
for i in range(len(layout)):
    max_energized = max(max_energized, test_layout(i, 0, ">"))
    max_energized = max(max_energized, test_layout(i, len(layout[0])-1, "<"))
for i in range(len(layout[0])):
    max_energized = max(max_energized, test_layout(0, i, "v"))
    max_energized = max(max_energized, test_layout(len(layout)-1, i, "^"))

print(max_energized)
