# load input.txt as lines
with open("input.txt", "r") as f:
    lines = f.readlines()

# Takes a string and returns the first int found
def get_int(string):
    return int("".join([char for char in string if char.isdigit()]))

def parse_line(line):
    game_number = get_int(line.split(":")[0])
    games = line.split(":")[1].split(";")
    game_list = []
    for game in games:
        colors = {}
        for color in game.split(","):
            color = color.strip()
            if color != "":
                color = color.split(" ")
                colors[color[1]] = int(color[0])
        game_list.append(colors)
    return game_number, game_list

max_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_valid(game):
    for color in game:
        if game[color] > max_dict[color]:
            return False
    return True

total = 0
for line in lines:
    game_number, game_list = parse_line(line)
    valid_bag = True
    for game in game_list:
        if not is_valid(game):
            valid_bag = False
    if valid_bag:
        total += game_number
print(total)

def get_minimums(game_list):
    minimums = {}
    for game in game_list:
        for color in game:
            if color not in minimums:
                minimums[color] = game[color]
            else:
                if game[color] > minimums[color]:
                    minimums[color] = game[color]
    return minimums

total = 0
for line in lines:
    game_number, game_list = parse_line(line)
    minimums = get_minimums(game_list)
    # power is product of all minimums
    power = 1
    for color in minimums:
        power *= minimums[color]
    total += power
print(total)
