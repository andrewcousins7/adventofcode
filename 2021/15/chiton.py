import math
import queue

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

points = queue.PriorityQueue()
points.put([0, [0, 0], 0])
visited = [[False for _ in range(len(lines))] for _ in range(len(lines))]
visited[0][0] = True


def printGraph(graph):
    for x in range(len(graph)):
        line = ""
        for y in range(len(graph)):
            if graph[x][y]:
                line += "x"
            else:
                line += "0"
        print(line)
    print("")


while not points.empty():
    lowestWeightCost, lowestPoint, lowestCost = points.get()
    #printGraph(visited)
    adjPoints = queue.PriorityQueue()
    nextPoint = None
    nextWeightCost = math.inf
    for mod in adjMod:
        modX = lowestPoint[0] + mod[0]
        modY = lowestPoint[1] + mod[1]
        if 0 <= modX < len(lines) and 0 <= modY < len(lines):
            if not visited[modX][modY]:
                travelCost = lines[modX][modY]
                heuristic = math.sqrt((len(lines) - modX) + (len(lines) - modY))
                weightedCost = travelCost + heuristic
                if weightedCost < nextWeightCost:
                    nextPoint = [modX, modY]
                    nextWeightCost = weightedCost
    if nextPoint is not None:
        nextActualCost = lowestCost + lines[nextPoint[0]][nextPoint[1]]
        points.put([nextWeightCost+lowestCost, nextPoint, nextActualCost])
        visited[nextPoint[0]][nextPoint[1]] = True
        if nextPoint == [len(lines)-1, len(lines)-1]:
            print(nextActualCost)
            break
    if nextPoint is not None:
        points.put([lowestWeightCost, lowestPoint, lowestCost])




