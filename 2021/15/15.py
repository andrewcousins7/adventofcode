import math

lines = []
with open("data.txt") as data:
    lines = [[int(v) for v in line] for line in data.read().splitlines()]

# print("Part 1")

print("Part 2")
newLines = [[0 for _ in range(len(lines)*5)] for _ in range(len(lines)*5)]
for xMod in range(5):
    for yMod in range(5):
        for x in range(len(lines)):
            for y in range(len(lines)):
                newX = x + (len(lines) * xMod)
                newY = y + (len(lines) * yMod)
                newValue = lines[x][y] + xMod + yMod
                while newValue > 9:
                    newValue -= 9
                newLines[newX][newY] = newValue
lines = newLines

adjMod = [[1, 0], [0, 1], [-1, 0], [0, -1]]

frontierPoints = [[0,0]]
frontierCosts = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
frontierCosts[0][0] = lines[0][0]

rFrontierPoints = [[len(lines)-1, len(lines)-1]]
rFrontierCosts = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
rFrontierCosts[len(lines)-1][len(lines)-1] = lines[len(lines)-1][len(lines)-1]

def printGraph(graph):
    print("")
    for x in range(len(graph)):
        print(graph[x])


def getLowestPoint(points, costs, targetPoint):
    lowestCost = math.inf
    lowestPoint = []
    for x, y in points:
        cost = costs[x][y]
        #cost += abs(targetPoint[0] - x) + abs(targetPoint[1] - y)
        if cost < lowestCost:
            lowestPoint = [x,y]
            lowestCost = cost
    return lowestPoint


while True:
    lowestPoint = getLowestPoint(frontierPoints, frontierCosts, [len(lines), len(lines)])
    lowestCost = frontierCosts[lowestPoint[0]][lowestPoint[1]]
    adjPoints = []
    for mod in adjMod:
        modX = lowestPoint[0] + mod[0]
        modY = lowestPoint[1] + mod[1]
        if 0 <= modX < len(lines) and 0 <= modY < len(lines):
            if [modX, modY] not in frontierPoints:
                adjPoints.append([modX,modY])
    lowestAdjPoint = getLowestPoint(adjPoints, lines, [len(lines), len(lines)])
    if lowestAdjPoint:
        cost = lines[lowestAdjPoint[0]][lowestAdjPoint[1]]
        frontierPoints.append(lowestAdjPoint)
        frontierCosts[lowestAdjPoint[0]][lowestAdjPoint[1]] = cost + lowestCost
        if lowestAdjPoint in rFrontierPoints:
            print(frontierCosts[lowestPoint[0]][lowestPoint[1]] + rFrontierCosts[lowestAdjPoint[0]][lowestAdjPoint[1]])
            break
    if len(adjPoints) <= 1:
        frontierCosts[lowestPoint[0]][lowestPoint[1]] = math.inf

    # Bidir A Star
    lowestPoint = getLowestPoint(rFrontierPoints, rFrontierCosts, [0,0])
    lowestCost = rFrontierCosts[lowestPoint[0]][lowestPoint[1]]
    adjPoints = []
    for mod in adjMod:
        modX = lowestPoint[0] + mod[0]
        modY = lowestPoint[1] + mod[1]
        if 0 <= modX < len(lines) and 0 <= modY < len(lines):
            if [modX, modY] not in rFrontierPoints:
                adjPoints.append([modX, modY])
    lowestAdjPoint = getLowestPoint(adjPoints, lines, [0,0])
    if lowestAdjPoint:
        cost = lines[lowestAdjPoint[0]][lowestAdjPoint[1]]
        rFrontierPoints.append(lowestAdjPoint)
        rFrontierCosts[lowestAdjPoint[0]][lowestAdjPoint[1]] = cost + lowestCost
        if lowestAdjPoint in frontierPoints:
            print(frontierCosts[lowestAdjPoint[0]][lowestAdjPoint[1]] + rFrontierCosts[lowestPoint[0]][lowestPoint[1]])
            break
    if len(adjPoints) <= 1:
        rFrontierCosts[lowestPoint[0]][lowestPoint[1]] = math.inf




