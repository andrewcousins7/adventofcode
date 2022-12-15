import re

sensors = []
with open('input.txt') as data:
    for line in data.readlines():
        sensors.append(re.findall("-?[0-9]+", line))

print("Part 1:")
# yRow = 2000000
# blockedYLocations = {}
# beaconsOnRow = {}
# for coordinates in sensors:
#     sensorX = int(coordinates[0])
#     sensorY = int(coordinates[1])
#     beaconX = int(coordinates[2])
#     beaconY = int(coordinates[3])
#     distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)
#
#     if beaconY == yRow:
#         key = str(beaconX) + "," + str(beaconY)
#         beaconsOnRow[key] = True
#     if sensorY == yRow:
#         key = str(sensorX) + "," + str(sensorY)
#         beaconsOnRow[key] = True
#
#     xStart = min(sensorX, beaconX) - distance
#     xEnd = max(sensorX, beaconX) + distance
#     for x in range(xStart, xEnd):
#         checkDistance = abs(sensorX - x) + abs(sensorY - yRow)
#         if checkDistance <= distance:
#             key = str(x) + "," + str(yRow)
#             blockedYLocations[key] = True
#
# for beacon in beaconsOnRow.keys():
#     blockedYLocations.pop(beacon)
# print(len(blockedYLocations.keys()))

print("Part 2:")
sensorRanges = []
for coordinates in sensors:
    sensorX = int(coordinates[0])
    sensorY = int(coordinates[1])
    beaconX = int(coordinates[2])
    beaconY = int(coordinates[3])
    distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)
    sensorRanges.append([sensorX, sensorY, distance])

searchRange = 4000000  #20
solution = None
y = 0
while y <= searchRange and solution is None:
    x = 0
    while x <= searchRange and solution is None:
        found = True
        for sensor in sensorRanges:
            distance = abs(sensor[0] - x) + abs(sensor[1] - y)
            if distance <= sensor[2]:
                found = False
                jumpLocation = sensor[0] + sensor[2] - abs(sensor[1] - y) + 1
                x = jumpLocation
                break
        if found:
            solution = x * 4000000 + y
            break
    y += 1

print("solution:")
print(solution)
