targetXMin = 241
targetXMax = 273
targetYMin = -97
targetYMax = -63

# targetXMin = 20
# targetXMax = 30
# targetYMin = -10
# targetYMax = -5

drag = -1
gravity = -1


def adjustXVelocity(velocityX):
    if velocityX > 0:
        velocityX += drag
    elif velocityX < 0:
        velocityX -= drag
    return velocityX


def takeTheShot(velocityX, velocityY):
    positionX = 0
    positionY = 0
    positions = []
    while positionX <= targetXMax and positionY >= targetYMin:
        if positionX >= targetXMin and positionY <= targetYMax:
            return True, positions

        positionX += velocityX
        velocityX = adjustXVelocity(velocityX)

        positionY += velocityY
        velocityY += gravity

        positions.append([positionX, positionY])
    return False, positions


def printTheShot(positions):
    xMax = targetXMax
    yMax = max(targetYMax, 0)
    yMin = min(targetYMin, 0)
    for x, y in positions:
        if x > xMax:
            xMax = x
        if y > yMax:
            yMax = y
        if y < yMin:
            yMin = y

    for yMod in range(yMax - yMin + 1):
        y = yMax - yMod
        line = ''
        for x in range(xMax + 1):
            if y == 0 and x == 0:
                line += 'S'
            elif [x, y] in positions:
                line += '#'
            elif targetXMin <= x <= targetXMax and targetYMin <= y <= targetYMax:
                line += "T"
            else:
                line += '.'
        print(line)
    print("")


def isValidXVelocity(velocityX):
    xPos = 0
    while xPos <= targetXMax:
        if xPos >= targetXMin:
            return True
        elif velocityX == 0:
            return False
        xPos += velocityX
        velocityX = adjustXVelocity(velocityX)
    return False


def isValidYVelocity(velocityY):
    yPos = 0
    while yPos >= targetYMin:
        if yPos <= targetYMax:
            return True
        yPos += velocityY
        velocityY -= 1
    return False

possibleXVelocitys = []
for velocityX in range(1, targetXMax + 1):
    if isValidXVelocity(velocityX):
        possibleXVelocitys.append(velocityX)

possibleYVelocities = []
# Max initial y velocity = targetYMin? Any higher and the return would skip over the target window
for velocityY in range(targetYMin, -targetYMin):
    if isValidYVelocity(velocityY):
        possibleYVelocities.append(velocityY)

bestShotY = -1
bestShotSteps = []
possibleValidShotsCount = 0
for x in possibleXVelocitys:
    for y in possibleYVelocities:
        success, steps = takeTheShot(x, y)
        if success:
            possibleValidShotsCount += 1
            yMax = max(y for _, y in steps)
            if yMax > bestShotY:
                bestShotY = yMax
                bestShotSteps = steps

#printTheShot(bestShotSteps)
print("Part 1")
print("Max Height:", bestShotY)
print("Part 2")
print("Possible different shots:", possibleValidShotsCount)
