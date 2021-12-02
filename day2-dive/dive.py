directions = []
with open('data.txt') as data:
    for line in data.readlines():
        direction, value = str.split(line)
        directions.append({"direction": str(direction), "value": int(value)})

print("Part 1")

depth = 0
distance = 0

for directionAndValue in directions:
    direction = directionAndValue["direction"]
    value = directionAndValue["value"]

    if direction == 'forward':
        distance += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value


print("Distance: ", distance)
print("Depth: ", depth)
print(distance*depth)