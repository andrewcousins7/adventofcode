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


print("Part 2")

depth = 0
distance = 0
aim = 0

for directionAndValue in directions:
    direction = directionAndValue["direction"]
    value = directionAndValue["value"]

    if direction == 'forward':
        distance += value
        depth += (aim * value)
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value

print("Distance: ", distance)
print("Depth: ", depth)
print("Aim: ", aim)
print(distance*depth)