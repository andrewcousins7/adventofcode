motions = []
with open('input.txt') as data:
    for line in data.readlines():
        line.strip()
        direction, stepCount = line.split(" ")
        motions.append([direction, int(stepCount)])

dirs = {
    'L': [-1, 0],
    'R': [1, 0],
    'D': [0, -1],
    'U': [0, 1]
}

print("Part 1:")
headLocation = [0, 0]
tailLocation = [0, 0]


def print_state():
    print("\n\n")
    for r in reversed(range(5)):
        output = ""
        for c in range(6):
            if headLocation == [c, r]:
                output += "H"
            elif tailLocation == [c, r]:
                output += "T"
            elif [0, 0] == [c, r]:
                output += "s"
            else:
                output += "."
        print(output)


def update_tail_location():
    x_distance = abs(headLocation[0] - tailLocation[0])
    y_distance = abs(headLocation[1] - tailLocation[1])

    move_x = True
    move_y = True
    if x_distance <= 1 and y_distance <= 1:
        move_x = False
        move_y = False
    if x_distance == 0:
        move_x = False
    if y_distance == 0:
        move_y = False

    if move_x:
        if tailLocation[0] < headLocation[0]:
            tailLocation[0] += 1
        else:
            tailLocation[0] -= 1
    if move_y:
        if tailLocation[1] < headLocation[1]:
            tailLocation[1] += 1
        else:
            tailLocation[1] -= 1


tailOccupiedSpaces = {}
for motion in motions:
    direction = dirs[motion[0]]
    for i in range(motion[1]):
        headLocation[0] += direction[0]
        headLocation[1] += direction[1]
        update_tail_location()

        tailOccupiedSpaces["" + str(tailLocation[0]) + "," + str(tailLocation[1])] = True
        # print_state()

# print(tailOccupiedSpaces)
print(len(tailOccupiedSpaces.keys()))

print("Part 2:")


def update_knot_location(follow_location, current_location):
    x_distance = abs(follow_location[0] - current_location[0])
    y_distance = abs(follow_location[1] - current_location[1])

    move_x = True
    move_y = True
    if x_distance <= 1 and y_distance <= 1:
        move_x = False
        move_y = False
    if x_distance == 0:
        move_x = False
    if y_distance == 0:
        move_y = False

    if move_x:
        if current_location[0] < follow_location[0]:
            current_location[0] += 1
        else:
            current_location[0] -= 1
    if move_y:
        if current_location[1] < follow_location[1]:
            current_location[1] += 1
        else:
            current_location[1] -= 1


knotLocations = [[0,0] for i in range(10)]
tailOccupiedSpaces = {}
for motion in motions:
    direction = dirs[motion[0]]
    for i in range(motion[1]):
        for i in range(len(knotLocations)):
            knotLocation = knotLocations[i]
            if i == 0:
                knotLocation[0] += direction[0]
                knotLocation[1] += direction[1]
            else:
                update_knot_location(knotLocations[i-1], knotLocation)

        tailOccupiedSpaces["" + str(knotLocations[len(knotLocations) - 1][0]) + "," + str(knotLocations[len(knotLocations) - 1][1])] = True

print(len(tailOccupiedSpaces.keys()))
