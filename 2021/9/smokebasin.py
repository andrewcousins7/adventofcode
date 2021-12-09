heightMap = []
with open("data.txt") as data:
    heightMap = [[int(height) for height in line] for line in data.read().splitlines()]

print("Part 1")
lowPoints = []
lowCoordinates = []
adjacentMods = [[1,0],[0,1],[-1,0],[0,-1]]
for row in range(len(heightMap)):
    for col in range(len(heightMap[row])):
        height = heightMap[row][col]
        adjecentValues = []
        for mod in adjacentMods:
            mRow = row + mod[0]
            mCol = col + mod[1]
            if 0 <= mRow < len(heightMap) and 0 <= mCol < len(heightMap[mRow]):
                adjecentValues.append(heightMap[mRow][mCol])
        if height < min(adjecentValues):
            lowPoints.append(height)
            lowCoordinates.append([row, col])

print(sum(lowPoints) + len(lowPoints))

print("Part 2")
basinSizes = []

counted = [[False for _ in range(len(heightMap[0]))] for _ in range(len(heightMap))]

def recursiveBasinSearch(row, col, heightMap):
    height = heightMap[row][col]
    basinSize = 1
    for mod in adjacentMods:
        mRow = row + mod[0]
        mCol = col + mod[1]
        if 0 <= mRow < len(heightMap) and 0 <= mCol < len(heightMap[mRow]):
            if not counted[mRow][mCol]:
                mHeight = heightMap[mRow][mCol]
                if 9 > mHeight > height:
                    counted[mRow][mCol] = True
                    basinSize += recursiveBasinSearch(mRow, mCol, heightMap)
    return basinSize


for coordinate in lowCoordinates:
    basinSizes.append(recursiveBasinSearch(coordinate[0], coordinate[1], heightMap))

basinSizes = sorted(basinSizes)
product = 1
for i in range(len(basinSizes) - 3, len(basinSizes)):
    product *= basinSizes[i]
print(product)
