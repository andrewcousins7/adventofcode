# read input.txt as follows
# The first line is a list of seeds, separated by spaces, after the semicolon.
# After the next semicolon, each line is an array of three numbers, until a blank line.
# Repeat this 6 times

seeds = []
arrays = []
with open('input.txt', 'r') as f:
    current_map = []
    for line in f:
        # if line contains a semi colon
        if ':' in line:
            line = line.split(':')
            if line[0] == "seeds":
                seeds = line[1].split(" ")
                seeds = [x.strip() for x in seeds if x]
            else:
                current_map = []
        else:
            if line == "\n":
                if current_map:
                    arrays.append(current_map)
            else:
                current_map.append(line.strip().split(" "))
    if current_map:
        arrays.append(current_map)

def convert_through_map(number, map):
    for line in map:
        convert_start = int(line[0])
        number_start = int(line[1])
        range = int(line[2])
        if number >= number_start and number < number_start + range:
            return convert_start + number - number_start
    return number

# Part 1
# locations = []
# for seed in seeds:
#     current_number = int(seed)
#     for array in arrays:
#         current_number = convert_through_map(current_number, array)
#     locations.append(current_number)
#
# print(locations)
# print(min(locations))

# Part 2

def advance_first_map(map1, map1_index, map2, map2_index):
    if map1_index >= len(map1) - 1:
        return False
    if map2_index >= len(map2) - 1:
        return True
    return map1[map1_index + 1][0] < map2[map2_index + 1][0]

def combine_maps(map1, map2):
    new_map = []
    location = 0
    map1_index = 0
    map2_index = 0
    while map1_index < len(map1) and map2_index < len(map2):
        map1_line = map1[map1_index]
        map2_line = map2[map2_index]
        location = max(map1_line[0], map2_line[0])
        new_map.append([location, map1_line[1] + map2_line[1]])
        if advance_first_map(map1, map1_index, map2, map2_index):
            map1_index += 1
        else:
            map2_index += 1

    return new_map

def setup_map(conversion_map):
    conversion_map.sort(key=lambda x: x[1])
    new_map = []
    last_location = 0
    for line in conversion_map:
        destination_start = int(line[0])
        source_start = int(line[1])
        range = int(line[2])

        if source_start > last_location:
            new_map.append([last_location, 0])

        offset = destination_start - source_start
        new_map.append([source_start, offset])
        last_location = source_start + range
    new_map.append([last_location, 0])
    return new_map

final_map = [[0, 0]]
# interate through arrays backward
for array in reversed(arrays):
    final_map = combine_maps(setup_map(array), final_map)

def convert_through_modified_map(seed, modified_map):
    index = 0
    while modified_map[index][0] < seed:
        index += 1
    return seed + modified_map[index][1], index

print(final_map)
i = 0
locations = []
while i < len(seeds):
    start = int(seeds[i])
    amount = int(seeds[i+1])
    print(start, start + amount)
    j = start
    while j <= start + amount:
        seed = start + j
        loc, index = convert_through_modified_map(seed, final_map)
        locations.append(loc)
        if index >= len(final_map) - 1:
            break
        minimum = final_map[index][0]
        if minimum > start + amount:
            break
        j = minimum
        print(j)
    i += 2


print(min(locations))
