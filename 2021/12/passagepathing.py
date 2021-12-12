lines = []
with open("data.txt") as data:
    lines = [line for line in data.read().splitlines()]

connections = {}

for line in lines:
    start, end = line.split("-")
    if not connections.get(start):
        connections[start] = []
    if not connections.get(end):
        connections[end] = []
    if end not in connections[start]:
        connections[start].append(end)
    if start not in connections[end]:
        connections[end].append(start)

print("Part 1")
paths = []

def searchForPaths(currentNode, visitedNodes):
    visitedNodes.append(currentNode)
    if currentNode == 'end':
        paths.append(visitedNodes)
    else:
        nextNodes = connections[currentNode]
        for node in nextNodes:
            isSmallCave = node == node.lower()
            isAlreadyVisited = node in visitedNodes
            if not (isSmallCave and isAlreadyVisited):
                searchForPaths(node, visitedNodes.copy())


searchForPaths('start', [])
print(len(paths))


print("Part 2")


def searchForPaths2(currentNode, visitedNodes, visitedTwice):
    visitedNodes.append(currentNode)
    if currentNode == 'end':
        paths.append(visitedNodes)
    else:
        nextNodes = connections[currentNode]
        for node in nextNodes:
            isStart = node == 'start'
            isSmallCave = node == node.lower()
            isAlreadyVisited = node in visitedNodes

            if not isStart:
                if not isSmallCave:
                    searchForPaths2(node, visitedNodes.copy(), visitedTwice)
                elif not isAlreadyVisited:
                    searchForPaths2(node, visitedNodes.copy(), visitedTwice)
                elif not visitedTwice:
                    searchForPaths2(node, visitedNodes.copy(), True)


paths = []
searchForPaths2('start', [], False)
print(len(paths))
