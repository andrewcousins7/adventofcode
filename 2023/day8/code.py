import math
lines = open("input.txt", "r").readlines()
directions = lines[0]
nodes = {}
for lines in lines[2:]:
    name = lines[0:3]
    left = lines[7:10]
    right = lines[12:15]
    nodes[name] = [left, right]

def is_done(current, end_node):
    if end_node:
        return current == end_node
    else:
        return current[2] == "Z"

def get_length(current, end_node = None):
    index = 0
    steps = 0
    while not is_done(current, end_node):
        direction = directions[index]
        if direction == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        steps += 1
        index += 1
        if index >= len(directions) - 1:
            index = 0
    return steps

# Part 1
print(get_length("AAA", "ZZZ"))

# Part 2
node_lengths = []

for node in nodes.keys():
    if node[2] == "A":
        node_lengths.append(get_length(node))

print(node_lengths)

print(math.lcm(*node_lengths))
