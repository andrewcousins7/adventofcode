rocks = []
for line in open("input.txt").readlines():
    line = line.strip()
    rocks.append([c for c in line])


def print_rocks(rocks):
    for rock in rocks:
        print("".join(rock))
    print()


def roll_rocks_north(rocks):
    for i in range(1, len(rocks)):
        for j in range(len(rocks[i])):
            if rocks[i][j] == "O":
                previous_row = i - 1
                while rocks[previous_row][j] == ".":
                    rocks[previous_row][j] = "O"
                    rocks[previous_row + 1][j] = "."
                    previous_row -= 1
                    if previous_row < 0:
                        break
    return rocks


rocks = roll_rocks_north(rocks)
print_rocks(rocks)


def count_weight_load(rocks):
    weight_load = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            if rocks[i][j] == "O":
                weight_load += len(rocks) - i
    return weight_load


print(count_weight_load(rocks))
