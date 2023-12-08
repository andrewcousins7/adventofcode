lines = []
for line in open("input.txt"):
    line = line.split(":")[1]
    line = line.split(" ")
    line = [int(x) for x in line if x]
    lines.append(line)

race_durations = lines[0]
race_distances = lines[1]

ways_to_win = []

def get_ways_to_win(duration, distance):
    win_count = 0
    for i in range(duration):
        if i * (duration - i) > distance:
            win_count += 1
    return win_count

for i in range(len(race_durations)):
    duration = race_durations[i]
    distance = race_distances[i]
    ways_to_win.append(get_ways_to_win(duration, distance))


def product(list):
    product = 1
    for i in list:
        product *= i
    return product

print(product(ways_to_win))

print(get_ways_to_win(49979494, 263153213781851))
